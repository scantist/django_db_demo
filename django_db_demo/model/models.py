from django.db import models


class Subject(models.Model):
    subject_id = models.AutoField(null=False, primary_key=True)
    name = models.TextField(null=False, blank=False, unique=True)
    description = models.TextField()
    created = models.DateTimeField(null=False)
    modified = models.DateTimeField(null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'


class Component(models.Model):
    component_id = models.AutoField(null=False, primary_key=True)
    name = models.TextField(null=False, blank=False, unique=True)
    version = models.TextField(null=False)
    created = models.DateTimeField(null=False)
    modified = models.DateTimeField(null=False)
    subject_id_fk = models.ForeignKey(Subject, to_field='subject_id', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'component'


class Vulnerability(models.Model):
    vulnerability_id = models.AutoField(null=False, primary_key=True)
    name = models.TextField(null=False, blank=False, unique=True)
    public_id = models.IntegerField(null=False, blank=False, unique=True)
    description = models.TextField()
    created = models.DateTimeField()
    component_id_fk = models.ForeignKey(Component, to_field='component_id', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'vulnerability'


class Foo(models.Model):
    foo_id = models.AutoField(null=False, primary_key=True)
    name = models.TextField()
