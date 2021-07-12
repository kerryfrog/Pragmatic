from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.views.generic import CreateView

from accountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, "accountapp/hello_world.html", context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User          #장고에서 기본 제공하는 유져
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')  #reverse_lazy 클래스에서 사용하려면 reverse_lazy 사용해야함
    template_name = 'accountapp/create.html'   #어떤 html 파일을 이용해서 볼것인지