from django.contrib import admin
from django.urls import path
from softapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Page routes
    path('soft/', views.soft_view, name='soft'),
    path('about/', views.about_view, name='about'),
    path('menu/', views.menu_view, name='menu'),
    path('contact/', views.contact_view, name='contact'),
]

# ✅ Allow static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

