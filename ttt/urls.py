from django.conf.urls import patterns, include, url

from ttt.views import hello
from ttt.views import index
from ttt.views import uuu
from ttt.views import chart
from ttt.views import ajax
from ttt.views import line
from ttt.views import aj
from ttt.views import linechart
from ttt.views import piechart
from ttt.views import combined
from ttt.views import lctest
from ttt.views import ratiometer
from ttt.views import histogram
from ttt.views import dash
from ttt.views import product
from ttt.views import consumer
from ttt.views import slider
from ttt.views import upload_file
from ttt.views import performance
from ttt.views import add_to_cart
from ttt.views import view
from ttt.views import buy
from ttt.views import tt_admin
from ttt.views import pie_cat
from ttt.views import upload
from ttt.views import upload_file
from ttt.views import success

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ttt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^index/$', index),
    url(r'^uuu/$', uuu),
    url(r'^chart/$', chart),
    url(r'^ajax/$', ajax),
	url(r'^line/$', line),
	url(r'^aj/$', aj),
	url(r'^linechart/$', linechart),
	url(r'^piechart/$', piechart),
	url(r'^combined/$', combined),
	url(r'^lctest/$', lctest),
	url(r'^ratiometer/$', ratiometer),
	url(r'^histogram/$', histogram),
	url(r'^dash/$', dash),
	url(r'^consumer/$', consumer),
	url(r'^product/$', product),
	url(r'^slider/$', slider),
	url(r'^upload_file/$', upload_file),
	url(r'^performance/$', performance),
	url(r'^add_to_cart/$', add_to_cart),
	url(r'^buy/$', buy),
	url(r'^view/$', view),
	url(r'^tt_admin/$', tt_admin),
	url(r'^pie_cat/$', pie_cat),
	url(r'^upload/$', upload),
	url(r'^upload_file/$', upload_file),
	url(r'^success/$', success),
)

