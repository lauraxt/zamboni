from django.conf.urls.defaults import patterns, url

from . import views

urlpatterns = patterns('',
    url('^$', views.landing, name='ecosystem.landing'),

    # These are temporarily hardcoded for now until MDN can support live
    # Javascript content and the information accessible through there.
    url('^docs/design/building_blocks$', views.building_blocks,
        name='ecosystem.building_blocks'),
    url('^docs/xtags/(?P<xtag>\w+)$', views.building_xtag,
        name='ecosystem.building_xtag'),

    url('^partners$', views.partners, name='ecosystem.partners'),
    url('^support$', views.support, name='ecosystem.support'),
    url('^docs/design/(?P<page>\w+)?$', views.documentation,
        name='ecosystem.documentation_design'),
    url('^docs/(?P<page>\w+)?$', views.documentation,
        name='ecosystem.documentation'),
)
