from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'book.views.index'),
    (r'^book/(?P<book_id>\d+)/$', 'book.views.book'),
)
