"""django_db_demo URL Configuration

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
from django.urls import re_path
from django_db_demo.view.views import show_subjects, show_delete_subject, show_add_subject_form

urlpatterns = [
    re_path(r'^subjects/$', show_subjects),
    re_path(r'^delete_subject/$', show_delete_subject),
    re_path(r'^create_new_subject/$', show_add_subject_form)
]
