# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from .forms import FileupForm
from .models import Fileup


class BasicUploadView(View):
    def get(self, request):
        file_list = Fileup.objects.all()
        return render(self.request, 'fileapp/index.html', {'files': file_list})

    def post(self, request):
        form = FileupForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            files = form.save()
            data = {'is_valid': True, 'name': files.file.name,
                    'url': files.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for files in Fileup.objects.all():
        files.file.delete()
        files.delete()
    return redirect(request.POST.get('next'))
