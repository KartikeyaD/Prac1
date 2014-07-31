from django.conf.urls import patterns, url
from listing import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
    url(r'^add_product/$', views.add_product, name='add_product'),
    url(r'^product/(?P<product_name_url>\w+)$', views.product, name='product'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.customer_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    )