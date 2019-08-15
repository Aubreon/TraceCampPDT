"""PDTinventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
import PDTinv.views as views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.TireCreate.as_view()),
    path('list/', views.TireList.as_view(), name='tire_list'),
    path('list/update/<int:pk>/', views.TireUpdate.as_view()),
    path('list/delete/<int:pk>/', views.TireDelete.as_view()),
    # path('search/', views.SearchResultsView.as_view(), name='search_results')
    # path('PDTinv/',include(PDTinv.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)