from .models import Estudiante
from social.pipeline.partial import partial

@partial
def get_user_avatar(strategy, response, details, uid, user=None, is_new=False, *args, **kwargs):
    url = None
    username_url = None

    if strategy.backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
        social_url = 'http://facebook.com/%s' % details['username']
 
    elif strategy.backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal', '')
        social_url = 'http://twitter.com/%s' % details['username']

    if url:
        est, created = Estudiante.objects.get_or_create(uid=user)
        if created:
            est.name = details['fullname']
            est.avatar = url
            est.social_network = strategy.backend.name
            est.social_url = social_url
            est.email = details['email']
            est.save()

