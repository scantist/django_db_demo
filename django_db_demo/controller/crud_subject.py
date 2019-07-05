from django_db_demo.model.models import Subject
import time
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


''' insert new Subject W'''
def insert_subject(name, **kwargs):
    if 'description' in kwargs:
        s1 = Subject(name=name, description=kwargs['description'],
                     created=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                     modified=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    else:
        s1 = Subject(name=name,
                     created=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                     modified=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    s1.save()
    print(">>>>>>>>>> insert success!")


# TODO: 加入更多query类型
''' return all subjects info in database '''
def query_all_info():
    all_subjects_info = Subject.objects.all()
    return all_subjects_info


''' query if the name already exists, the name should be unique '''
def query_has_same_name(name, subject_id=-1):
    try:
        subject = Subject.objects.get(name=name)

        # not modify the subject's name
        if subject.subject_id == subject_id:
            return False
        else:
            return True
    except ObjectDoesNotExist:
        return False


''' query specific subject by id '''
def query_id(subject_id):
    return Subject.objects.get(subject_id=subject_id)


''' update subject's basic info '''
def update_subject(subject_id, name, description=''):
    subject = Subject.objects.get(subject_id=subject_id)

    subject.name = name
    subject.description = description
    subject.modified = timezone.now()

    subject.save()


# TODO: 加入更多删除选项
''' delete subject by Id '''
def delete_subject(subject_id):
    subject = Subject.objects.get(subject_id=subject_id)
    subject.delete()
    print(">>>>>>>> delete success!")
