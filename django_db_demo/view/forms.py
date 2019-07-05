from django import forms
from django_db_demo.controller.crud_subject import query_has_same_name
from django_db_demo.controller.crud_component import has_same_component_name
from django_db_demo.controller.crud_vulnerability import has_same_vulnerability_name, has_same_vulnerability_public_id
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re


class SubjectForm(forms.Form):
    name = forms.CharField(label='Name: ', required=True, strip=True)
    description = forms.CharField(label='Description: ', required=False, strip=True)

    def clean_name(self):
        name = self.cleaned_data['name']

        # check the name has not existed in database
        if query_has_same_name(name):
            raise ValidationError(_('%s already exists in database') % name)

        return name


# TODO: 如果用户啥也没干 不算duplicated
class UpdateSubjectForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.subject_name = kwargs.pop('subject_name')
        self.subject_description = kwargs.pop('subject_description')
        self.subject_id = kwargs.pop('subject_id')
        super(UpdateSubjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'value': self.subject_name})
        self.fields['description'].widget = forms.TextInput(attrs={'value': self.subject_description})

    name = forms.CharField(label='Name: ', required=True, strip=True,
                           widget=forms.TextInput(attrs={'placeholder': ''}))
    description = forms.CharField(label='Description: ', required=False, strip=True)

    def clean_name(self):
        name = self.cleaned_data['name']

        # check the name has not existed in database
        if query_has_same_name(name, self.subject_id):
            raise ValidationError(_("' %s ' already exists in database") % name)

        return name


class ComponentForm(forms.Form):
    name = forms.CharField(label='Name: ', required=True, strip=True)
    version = forms.CharField(label='Version: ', required=True, strip=True)

    def clean_name(self):
        name = self.cleaned_data['name']

        # check the name has not existed in database
        if has_same_component_name(name):
            raise ValidationError(_('%s already exists in database') % name)

        return name

    def clean_version(self):
        version = self.cleaned_data['version']
        is_match = re.match("^v[0-9*].[0-9*].[0-9*]", version)
        if is_match:
            return version
        else:
            raise ValidationError(_('wrong version style, make sure you input like v1.0.0'))


class UpdateComponentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.component_name = kwargs.pop('component_name')
        self.component_version = kwargs.pop('component_version')
        super(UpdateComponentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'value': self.component_name})
        self.fields['version'].widget = forms.TextInput(attrs={'value': self.component_version})

    name = forms.CharField(label='Name: ', required=True, strip=True,
                           widget=forms.TextInput(attrs={'placeholder': ''}))
    version = forms.CharField(label='Version: ', required=True, strip=True)

    def clean_name(self):
        name = self.cleaned_data['name']

        # check the name has not existed in database
        if query_has_same_name(name):
            raise ValidationError(_('%s already exists in database') % name)

        return name

    def clean_version(self):
        version = self.cleaned_data['version']
        is_match = re.match("^v[0-9*].[0-9*].[0-9*]", version)

        if not is_match:
            raise ValidationError(_('wrong version style, make sure you input like v1.0.0'))

        return version


class VulnerabilityForm(forms.Form):
    name = forms.CharField(label='Name: ', strip=True, required=True)
    public_id = forms.IntegerField(required=True, label='Public Id: ')
    description = forms.CharField(strip=True, label='Description: ')

    def clean_name(self):
        name = self.cleaned_data['name']

        # check the name has not existed in database
        if has_same_vulnerability_name(name):
            raise ValidationError(_('%s already exists in database') % name)

        return name

    def clean_public_id(self):
        public_id = self.cleaned_data['public_id']

        if has_same_vulnerability_public_id(public_id):
            raise ValidationError(_(' %s already exists in database' % public_id))

        return public_id
