from drinking.models import Profile
from django.contrib.auth.models import User
from requests import request, HTTPError
from django.core.files.base import ContentFile

def create_profile(user, *args, **kwargs):
        try:
            profile = user.profile
        except:
            profile = Profile(user_id=user.id)
            profile.save()

def save_profile(backend, user, response, *args, **kwargs):
    import ipdb; ipdb.set_trace()
    if backend.name == 'facebook':
        profile = user.profile
        profile.gender = response.get('gender')
        profile.save()




def get_profile_picture(backend, strategy, details, response,
        user=None, *args, **kwargs):
    url = None
    profile = user.profile
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
        profile.avatar = url
        profile.save()

    elif backend.name == 'google-oauth2':
        url = response['picture']
        profile.avatar = url
        profile.save()