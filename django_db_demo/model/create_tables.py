from django.db.models import Model
from django.db import models


class Subject(Model):
    id = models.AutoField(null=False, primary_key=True)
    name = models.TextField('asdas')
    description = models.TextField('sds')
    created = models.DateTimeField('2019-06-20')
    modified = models.DateTimeField('2019-06-20')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'
