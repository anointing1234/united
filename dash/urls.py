from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.static import serve 



urlpatterns = [
    path('',views.home_page,name='home'),
    path('home/',views.home_page,name='home'),
    path('about/',views.about_page,name='about'),
    path('services/',views.services_page,name='services'),
    path('home_insurance/',views.home_insurance_page,name='home_insurance'),
    path('business_insurance/',views.business_insurance_page,name='business_insurance'),
    path('health_insurance/',views.health_insurance_page,name='health_insurance'),
    path('news/',views.news_page,name='news'),
    path('contact/',views.contact_page,name='contact'),





    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


 
 

