from drinking.models import Profile
from django.contrib.auth.models import User

def create_profile(user, *args, **kwargs):
        try:
            profile = user.profile
        except:
            profile = Profile(user_id=user.id)
            profile.save()

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = user.profile
        profile.gender = response.get('gender')
        profile.save()
