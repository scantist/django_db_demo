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
from django.urls import re_path, path
from django_db_demo.view.views import subjects_list, show_delete_subject, add_subject_form

urlpatterns = [
    re_path(r'^subjects/$', subjects_list, name='show_subjects'),
    path('delete_subject/<int:subject_id>', show_delete_subject, name='show_delete_subject'),
    re_path(r'^create_new_subject/$', add_subject_form, name='add_subject_form'),
]
