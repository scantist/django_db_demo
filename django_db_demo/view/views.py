from django.shortcuts import render, reverse
from django_db_demo.controller.crud_subject import query_all_info, insert_subject, delete_subject, query_id, \
                                                    update_subject
from django_db_demo.controller.crud_component import query_components_by_subject, insert_component,\
                                                     delete_component_by_id, query_component, update_component
from django_db_demo.controller.crud_vulnerability import query_vulnerability_by_component, insert_vulnerability,\
                                                         delete_vulnerability_by_id
from .forms import SubjectForm, UpdateSubjectForm, ComponentForm, UpdateComponentForm, VulnerabilityForm
from django.http import HttpResponseRedirect
from django.urls import reverse


''' Subject '''
def subjects_list(request):
    subjects = query_all_info
    context = {'subject_list': subjects}
    return render(request, 'list_subjects.html', context)


def show_delete_subject(request, subject_id):
    delete_subject(subject_id)
    return HttpResponseRedirect('/subjects/')


def show_add_subject_form(request):
    if request.method == 'POST':
        subject_form = SubjectForm(request.POST)

        if subject_form.is_valid():
            name = subject_form.cleaned_data['name']
            description = subject_form.cleaned_data['description']

            insert_subject(name, description=description)

            return HttpResponseRedirect('/subjects/')
    else:
        subject_form = SubjectForm()

    return render(request, 'add_subject.html', {'form': subject_form})


def show_update_subject_form(request, subject_id):
    subject = query_id(subject_id)

    if request.method == 'POST':
        update_subject_form = UpdateSubjectForm(request.POST, subject_name='', subject_description='',
                                                subject_id=subject_id)

        if update_subject_form.is_valid():
            name = update_subject_form.cleaned_data['name']
            description = update_subject_form.cleaned_data['description']

            update_subject(subject_id, name=name, description=description)

            return HttpResponseRedirect('/subjects/')
    else:
        update_subject_form = UpdateSubjectForm(subject_name=subject.name, subject_description=subject.description,
                                                subject_id=subject_id)

    return render(request, 'update_subject.html', {'form': update_subject_form})


''' Component '''
def show_component_list(request, subject_id):
    subject = query_id(subject_id)
    subject_name = subject.name
    component_list = query_components_by_subject(subject_id)
    context = {'subject_name': subject_name, 'component_list': component_list, 'subject_id': subject_id}
    return render(request, 'list_components.html', context)


def show_add_component_form(request, subject_id):
    if request.method == 'POST':
        component_form = ComponentForm(request.POST)

        if component_form.is_valid():
            name = component_form.cleaned_data['name']
            version = component_form.cleaned_data['version']
            insert_component(name, version, query_id(subject_id))

            return HttpResponseRedirect('/components/' + str(subject_id))
    else:
        component_form = ComponentForm()

    return render(request, 'add_component.html', {'form': component_form, 'subject_id': subject_id})


# TODO: 删除后前进，会报错
def show_delete_component(request, component_id):
    subject_id = query_component(component_id).subject_id_fk.subject_id
    delete_component_by_id(component_id)
    return HttpResponseRedirect('/components/' + str(subject_id))


def show_update_component(request, component_id, subject_id):
    component = query_component(component_id)

    if request.method == 'POST':
        update_component_form = UpdateComponentForm(request.POST, component_name='', component_version='')

        if update_component_form.is_valid():
            name = update_component_form.cleaned_data['name']
            version = update_component_form.cleaned_data['version']

            update_component(component_id, name, version)

            url = reverse('show_component_list', args=subject_id)
            return HttpResponseRedirect(url)
    else:
        update_component_form = UpdateComponentForm(component_name=component.name, component_version=component.version)

    return render(request, 'update_component.html', {'form': update_component_form, 'subject_id': subject_id})


''' Vulnerability '''


def show_vulnerability_list(request, component_id, subject_id):
    subject = query_id(subject_id)
    subject_name = subject.name
    component = query_component(component_id)
    component_name = component.name
    vulnerability_list = query_vulnerability_by_component(component_id)
    context = {'component_name': component_name, 'vulnerability_list': vulnerability_list, 'subject_name': subject_name,
               'subject_id': subject_id, 'component_id': component_id}
    return render(request, 'list_vulnerability.html', context)


def show_add_vulnerability_form(request, subject_id, component_id):
    if request.method == 'POST':
        vulnerability_form = VulnerabilityForm(request.POST)

        if vulnerability_form.is_valid():
            name = vulnerability_form.cleaned_data['name']
            public_id = vulnerability_form.cleaned_data['public_id']
            description = vulnerability_form.cleaned_data['description']

            insert_vulnerability(name, public_id, query_component(component_id), description)

            url = reverse('show_vulnerability_list', args=[component_id, subject_id])

            return HttpResponseRedirect(url)
    else:
        vulnerability_form = VulnerabilityForm()

    context = {'component_id': component_id, 'subject_id': subject_id, 'form': vulnerability_form}
    return render(request, 'add_vulnerability.html', context)


def show_delete_vulnerability(request, component_id, subject_id, vulnerability_id):
    delete_vulnerability_by_id(vulnerability_id)

    url = reverse('show_vulnerability_list', args=[component_id, subject_id])
    return HttpResponseRedirect(url)
