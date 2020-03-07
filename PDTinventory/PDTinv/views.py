from django.shortcuts import render
from django.db.models import Q
from PDTinv.models import Tire
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class TireHome(TemplateView):
    template_name = "index.html"


class TireCreate(CreateView):
    model = Tire
    fields = ['width', 'sidewall', 'rim']

    def get_success_url(self):
        return '/list'


class TireList(ListView):
    model = Tire

    def get_queryset(self):
        w = self.request.GET.get('width', '')
        s = self.request.GET.get('sidewall', '')
        r = self.request.GET.get('rim', '')
        object_list = Tire.objects.all()

        if (w == s == r == ''):
            pass
        else:
            if (w != ''):
                object_list = object_list.filter(width=w)
            if (s != ''):
                object_list = object_list.filter(sidewall=s)
            if (r != ''):
                object_list = object_list.filter(rim=r)
        print(object_list)
        return object_list

class TireUpdate(UpdateView):
    model = Tire
    fields = ['width', 'sidewall', 'rim']

    def get_success_url(self):
        return '/list'


class TireDelete(DeleteView):
    model = Tire

    success_url = reverse_lazy('tire_list')
