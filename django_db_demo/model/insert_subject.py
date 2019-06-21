from django_db_demo.model.create_tables import Subject
import time


def test():
    s1 = Subject(name='first project', create=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    s1.save()
