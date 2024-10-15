from django.urls import path
from .views import  HomepageView, AboutpageView, ContactpageView, ServicespageView


urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('home/', HomepageView.as_view(), name = 'home'),
    path('about/', AboutpageView.as_view(),name = 'about'),
    path('contact/', ContactpageView.as_view(),name = 'contact'),
    path('services/', ServicespageView.as_view(), name='services'),
]