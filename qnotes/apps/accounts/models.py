from django.db import models
from django.db.utils import DatabaseError
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.core.management import call_command
from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign
from userena.models import UserenaLanguageBaseProfile


# class AccountProfile(FacebookProfileModel, UserenaLanguageBaseProfile):
class UserProfile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('User'),
                                related_name='account_profile')

    # define necessarry fields below & migrate
    #
    # extra_field = models.CharField(_('Extra Field'), max_length=255)


# register a handler for the User model's django.db.models.signals.post_save signal and,
# in the handler, if created is True, create the associated user profile:
@receiver(post_save, sender=User, dispatch_uid='user.created')
def create_profile(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    """ Adds 'change_profile' permission to created user object """
    try:
        if created:
            profile, new = UserProfile.objects.get_or_create(user=instance)
            assign('change_profile', instance, instance.get_profile())
            call_command('check_permissions')
    except DatabaseError:
        pass
