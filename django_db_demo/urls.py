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
from django_db_demo.view.views import subjects_list, show_delete_subject, show_add_subject_form, \
                                      show_update_subject_form, show_component_list, show_add_component_form,\
                                      show_delete_component, show_update_component, show_vulnerability_list, \
                                      show_add_vulnerability_form, show_delete_vulnerability

urlpatterns = [
    re_path(r'^subjects/$', subjects_list, name='show_subjects'),
    path('delete_subject/<int:subject_id>', show_delete_subject, name='show_delete_subject'),
    re_path(r'^create_new_subject/$', show_add_subject_form, name='add_subject_form'),
    path('update_subject/<int:subject_id>', show_update_subject_form, name='update_subject_form'),
    path('components/<int:subject_id>', show_component_list, name='show_component_list'),
    path('create_new_component/<int:subject_id>', show_add_component_form, name='add_component_form'),
    path('delete_component/<int:component_id>', show_delete_component, name='show_delete_component'),
    re_path(r'^update_component/(?P<component_id>\d+)/(?P<subject_id>\d+)/$', show_update_component,
            name='show_update_component'),
    re_path(r'^vulnerabilities/(?P<component_id>\d+)/(?P<subject_id>\d+)/$', show_vulnerability_list,
            name='show_vulnerability_list'),
    re_path(r'^create_new_vulnerabilities/(?P<component_id>\d+)/(?P<subject_id>\d+)/$', show_add_vulnerability_form,
            name='add_vulnerability_form'),
    re_path(r'^delete_vulnerability/(?P<component_id>\d+)/(?P<subject_id>\d+)/(?P<vulnerability_id>\d+)/$',
            show_delete_vulnerability, name='show_delete_vulnerability')
]
