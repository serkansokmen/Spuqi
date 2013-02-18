from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from qnotes.apps.accounts.models import UserProfile
from userena.models import UserenaSignup
# from userena.utils import get_profile_model


# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


class UserenaSignupInline(admin.StackedInline):
    model = UserenaSignup
    max_num = 1
    verbose_name = 'registration'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = [UserProfileInline, UserenaSignupInline]
    inline_classes = ('grp-collapse grp-open',)

    def queryset(self, request):
        """Alter the queryset to exclude Django Userena's AnonymousUser"""
        qs = super(UserAdmin, self).queryset(request)
        # if not request.user.is_superuser:
        return qs.filter(pk__gt=-1)
        #return qs

# Re-register UserAdmin
admin.site.unregister(UserProfile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# admin.site.register(get_profile_model())
