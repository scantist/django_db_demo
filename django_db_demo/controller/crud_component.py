from django_db_demo.model.models import Component, Subject
import time
from django.core.exceptions import ObjectDoesNotExist


''' insert new Component'''
def insert(name, version, subject_id_fk):
    s1 = Component(name=name,
                   version=version,
                   created=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                   modified=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                   subject_id_fk=subject_id_fk)
    s1.save()
    print(">>>>>>>>>> insert success!")


# TODO: 加入更多query类型
''' return all components info in database '''
def query_components_info():
    all_components_info = Component.objects.all()
    return all_components_info


def query_component(component_id):
    component = Component.objects.get(component_id=component_id)
    return component


''' return components of the subject in database '''
def query_components_by_subject(subject_id):
    subject = Subject.objects.get(subject_id=subject_id)
    components = subject.component_set.all()
    return components

def has_same_component_name(name):
    try:
        Component.objects.get(name=name)
        return True
    except ObjectDoesNotExist:
        return False

def delete_component_by_id(component_id):
    component = Component.objects.get(component_id=component_id)
    component.delete()
    print(">>>>>>>> delete success!")
