from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.signup, name = "signup"),
    path('donationplea/', views.donationplea, name="donationplea"),
    path('donate/', views.donate, name="donate"),
    path('cards/', views.cards, name = "cards"), 
    path('pleas/', views.pleas, name = "pleas")

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
