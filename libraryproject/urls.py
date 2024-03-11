"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from library import views as library_views
from library.views import *

from django.conf.urls.static import static
from django.conf import settings

from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', library_views.home, name='home'),
    path('about/', library_views.about),
    path('book_description/<int:book_id>/', book_details, name='book_description'),
    path('book_details/<int:book_id>/', book_details, name='book_details'),  # Nueva URL para book_details
    path('change_availability/<int:book_id>/', views.change_availability, name='change_availability'),
    path('reserve_book/<int:book_id>/', views.reserve_book, name='reserve_book'),
    path('change_real_availability/<int:book_id>/', views.change_real_availability, name='change_real_availability'),
    path('verify_availability/<int:book_id>/', views.verify_availability, name='verify_availability'),
    path('adminrent/<int:book_id>/', views.adminrent, name='adminrent'),
    path('rate-book/', views.rate_book, name='rate_book'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('form/', views.add_book, name='add_book'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
