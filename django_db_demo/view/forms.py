from django import forms
from django_db_demo.controller.crud_subject import query_has_same_name
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class SubjectFrom(forms.Form):
    name = forms.CharField(label='Name: ', required=True, strip=True)
    description = forms.CharField(label='Description: ', required=False, strip=True)

    def clean_name(self):
        name = self.cleaned_data['name']

        # check the name has not existed in database
        if query_has_same_name(name):
            raise ValidationError(_('%s already exists in database') % name)

        return name
