from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'book.views.index'),
    (r'^book/(?P<book_id>\d+)/$', 'book.views.book'),
    (r'^tag/(?P<tag_slug>[\w_]+\w)/$', 'book.views.tag'),
    (r'^genre/(?P<genre_slug>[\w_]+\w)/$', 'book.views.genre'),
    (r'^suggest/$', 'book.views.suggest'),
    (r'^suggest/(?P<book_id>\d+)/$', 'book.views.suggest'),
)
