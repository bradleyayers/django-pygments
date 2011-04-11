from django.conf.urls.defaults import patterns


urlpatterns = patterns(
    'django_pygments.views',
    (r'^demo/$', 'demo'),
)
