from django.urls import path
from Myapp import views

urlpatterns = [
    path('welcome/', views.karibu),
    path('', views.homepage, name='my_homepage'),
    path('aboutus/', views.aboutus, name='my_about'),
    path('contactus/', views.contactus, name='my_contact'),
    path('gallery/', views.gallery, name='my_gallery'),
    path('services/', views.services, name='my_services')



]
