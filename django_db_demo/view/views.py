from django.shortcuts import render, reverse
from django_db_demo.controller.crud_subject import query_all_info, insert_subject, delete_subject, query_id, \
                                                    update_subject
from django_db_demo.controller.crud_component import query_components_info, query_components_by_subject, insert,\
                                                     delete_component_by_id, query_component
from .forms import SubjectForm, UpdateSubjectForm, ComponentForm
from django.http import HttpResponseRedirect


''' Subject '''
def subjects_list(request):
    subjects = query_all_info
    components = query_components_info()
    context = {'subject_list': subjects, 'component_list': components}
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
            if not description:
                insert_subject(name)
            else:
                insert_subject(name, description=description)

            return HttpResponseRedirect('/subjects/')
    else:
        subject_form = SubjectForm()

    return render(request, 'add_subject.html', {'form': subject_form})


def show_update_subject_form(request, subject_id):
    subject = query_id(subject_id)

    if request.method == 'POST':
        update_subject_form = UpdateSubjectForm(request.POST, subject_name='', subject_description='')

        if update_subject_form.is_valid():
            name = update_subject_form.cleaned_data['name']
            description = update_subject_form.cleaned_data['description']

            if not description:
                update_subject(subject_id, name=name)
            else:
                update_subject(subject_id, name=name, description=description)

            return HttpResponseRedirect('/subjects/')
    else:
        update_subject_form = UpdateSubjectForm(subject_name=subject.name, subject_description=subject.description)

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
            insert(name, version, query_id(subject_id))

            return HttpResponseRedirect('/components/' + str(subject_id))
    else:
        component_form = ComponentForm()

    return render(request, 'add_component.html', {'form': component_form, 'subject_id': subject_id})


# TODO: 删除后前进，会报错
def show_delete_component(request, component_id):
    subject_id = query_component(component_id).subject_id_fk.subject_id
    delete_component_by_id(component_id)
    return HttpResponseRedirect('/components/' + str(subject_id))

