from django.shortcuts import render
from django.db.models import Q
from PDTinv.models import Tire
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

# Create your views here.


class TireCreate(CreateView):
    model = Tire
    fields = ['width', 'sidewall', 'rim']

    def get_success_url(self):
        return '/list'


class TireList(ListView):
    model = Tire

    def get_queryset(self):
        w = self.request.GET.get('width')
        s = self.request.GET.get('sidewall')
        r = self.request.GET.get('rim')
        object_list = Tire.objects.all()

        if (w == s == r == None):
            return object_list
        else:
            if (w != None):
                object_list.filter(width=w)
            if (s != None):
                object_list.filter(sidewall=s)
            if (r != None):
                object_list.filter(rim=r)
            return object_list

        # if w == s == r == None:
        #     return Tire.objects.all()
        # elif w == s == None:
        #     print("r")
        #     return Tire.objects.filter(rim=r)
        # elif s == r == None:
        #     print("w")
        #     return Tire.objects.filter(width=w)
        # elif w == r == "":
        #     print("s")
        #     return Tire.objects.filter(sidewall=s)
        # elif w == "":
        #     print("s r")
        #     return Tire.objects.filter(rim=r).filter(rim=r)
        # elif r == "":
        #     print("w s")
        #     return Tire.objects.filter(width=w).filter(sidewall=s)
        # elif s == "":
        #     print("w r")
        #     return Tire.objects.filter(width=w).filter(rim=r)
        # else:
        #     print("w s r")
        #     return Tire.objects.filter(width=w).filter(rim=r).filter(sidewall=s)


class TireUpdate(UpdateView):
    model = Tire
    fields = ['width', 'sidewall', 'rim']

    def get_success_url(self):
        return '/list'


class TireDelete(DeleteView):
    model = Tire

    success_url = reverse_lazy('tire_list')
