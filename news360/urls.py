# news360/urls.py
# Improved version with better structure & comments

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

# Core URL configuration for the project
urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirect root URL to stories section
    path('', RedirectView.as_view(url='/stories/', permanent=False)),

    # App-specific routes
    path('accounts/', include('accounts.urls')),
    path('stories/', include('stories.urls')),
    path('feedback/', include('feedback.urls')),

    # Authentication routes
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='/stories/'),
        name='logout',
    ),
]

# Serving static & media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
