"""Management utilities."""

import os

from fabric.contrib.console import confirm
from fabric.api import abort, env, local, settings, task

from spuqi.settings.common import LOCAL_APPS

########## GLOBALS
env.run = 'heroku run python manage.py'

env.git_repo = local('git config --get remote.origin.url', capture=True)
env.project_name = env.git_repo.split('/')[-1].split('.')[0]  # use git file name
env.project_folder_name = env.project_name.lower()
env.project_dir = os.path.realpath(os.path.dirname(env.real_fabfile))


HEROKU_ADDONS = (
    'cloudamqp:lemur',
    'heroku-postgresql:dev',
    'scheduler:standard',
    'memcache:5mb',
    'newrelic:standard',
    'pgbackups:auto-month',
    'sentry:developer',
)
HEROKU_CONFIGS = (
    'DJANGO_SETTINGS_MODULE=spuqi.settings.prod',
    'SECRET_KEY=5d_d-d@s-z$zc9vljs4oruq=)o3uvoo#8zgs78jr78ov2=bcdx'
    'AWS_ACCESS_KEY_ID=xxx',
    'AWS_SECRET_ACCESS_KEY=xxx',
    'AWS_STORAGE_BUCKET_NAME=xxx',
)
########## END GLOBALS


########## HELPERS
def cont(cmd, message):
    """Given a command, ``cmd``, and a message, ``message``, allow a user to
    either continue or break execution if errors occur while executing ``cmd``.

    :param str cmd: The command to execute on the local system.
    :param str message: The message to display to the user on failure.

    .. note::
        ``message`` should be phrased in the form of a question, as if ``cmd``'s
        execution fails, we'll ask the user to press 'y' or 'n' to continue or
        cancel exeuction, respectively.

    Usage::

        cont('heroku run ...', "Couldn't complete %s. Continue anyway?" % cmd)
    """
    with settings(warn_only=True):
        result = local(cmd, capture=True)

    if message and result.failed and not confirm(message):
        abort('Stopped execution per user request.')
########## END HELPERS


########## DATABASE MANAGEMENT
@task
def setupdb():
    """Run a syncdb."""
    local('%(run)s syncdb --all --noinput' % env)
    local('%(run)s migrate accounts --fake --noinput' % env)
    local('%(run)s migrate authors --fake --noinput' % env)
    local('%(run)s migrate sources --fake --noinput' % env)
    local('%(run)s migrate quotes --fake --noinput' % env)
    local('%(run)s migrate collections --fake --noinput' % env)
    local('%(run)s migrate --fake --noinput' % env)


@task
def syncdb():
    """Run a syncdb."""
    local('%(run)s syncdb --noinput' % env)


@task
def migrate(app=None):
    """Apply one (or more) migrations. If no app is specified, fabric will
    attempt to run a site-wide migration.

    :param str app: Django app name to migrate.
    """
    if app:
        local('%s migrate %s --noinput' % (env.run, app))
    else:
        local('%(run)s migrate --noinput' % env)
########## END DATABASE MANAGEMENT


########## FILE MANAGEMENT
@task
def collectstatic():
    """Collect all static files, and copy them to S3 for production usage."""
    local('%(run)s collectstatic --noinput' % env)
########## END FILE MANAGEMENT


########## HEROKU MANAGEMENT
@task
def bootstrap():
    """Bootstrap your new application with Heroku, preparing it for a production
    deployment. This will:

        - Create a new Heroku application.
        - Install all ``HEROKU_ADDONS``.
        - Sync the database.
        - Apply all database migrations.
        - Initialize New Relic's monitoring add-on.
    """
    cont('heroku create', "Couldn't create the Heroku app, continue anyway?")

    for addon in HEROKU_ADDONS:
        cont(
            'heroku addons:add %s' % addon,
            "Couldn't add %s to your Heroku app, continue anyway?" % addon)

    for config in HEROKU_CONFIGS:
        cont(
            'heroku config:add %s' % config,
            "Couldn't add %s to your Heroku app, continue anyway?" % config)

    cont(
        'git push heroku master',
        "Couldn't push your application to Heroku, continue anyway?")

    syncdb()
    migrate()

    cont(
        '%(run)s newrelic-admin validate-config - stdout' % env,
        "Couldn't initialize New Relic, continue anyway?")


@task
def deploy():
    """ Deploy to Heroku """
    syncdb()
    migrate()
    collectstatic()


@task
def destroy():
    """Destroy this Heroku application. Wipe it from existance.

    .. note::
        This really will completely destroy your application. Think twice.
    """
    local('heroku apps:destroy')
########## END HEROKU MANAGEMENT
