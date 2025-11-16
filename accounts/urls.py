from django.urls import path
from . import views

app_name = 'accounts'  # helps with namespacing URLs

urlpatterns = [
    
    # path('signup/', views.signup_view, name='signup'),
    path('signup/', views.signup, name='signup'), # add this
]