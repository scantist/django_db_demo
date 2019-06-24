from django.shortcuts import render
from django_db_demo.controller.crud_subject import query_all_info, insert
from .forms import SubjectFrom
from django.http import HttpResponseRedirect


def show_subjects(request):
    subjects = query_all_info
    context = {'subject_list': subjects}
    return render(request, 'list_subjects.html', context)


def show_delete_subject(request):
    pass


def show_add_subject_form(request):
    if request.method == 'POST':
        subject_form = SubjectFrom(request.POST)

        if subject_form.is_valid():
            name = subject_form.cleaned_data['name']
            description = subject_form.cleaned_data['description']
            if not description:
                insert(name)
            else:
                insert(name,description=description)

            return HttpResponseRedirect('/subjects/')
    else:
        subject_form = SubjectFrom()

    return render(request, 'add_subject.html', {'form': subject_form})
