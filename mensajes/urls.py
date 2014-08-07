from django.conf.urls import patterns, include, url

urlpatterns = patterns('mensajes.views',
    url(r'^$', 'mensajes', name='mensajes'),
)
