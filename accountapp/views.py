from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render


# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from django.urls import reverse, reverse_lazy

from articleapp.models import Article

has_ownership = [ account_ownership_required , login_required]


#로그인 했는지 안했는지 확인해주는 데코레이터


class AccountCreateView(CreateView):
    model = User          #장고에서 기본 제공하는 유져
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')  #reverse_lazy 클래스에서 사용하려면 reverse_lazy 사용해야함
    template_name = 'accountapp/create.html'   #어떤 html 파일을 이용해서 볼것인지

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

#일반 function에서 사용하는걸 메서드에서도 사용할 수 있게 해주는 데코레이터
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User          #장고에서 기본 제공하는 유져
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')  #reverse_lazy 클래스에서 사용하려면 reverse_lazy 사용해야함
    template_name = 'accountapp/update.html'   #어떤 html 파일을 이용해서 볼것인지


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User          #장고에서 기본 제공하는 유져
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')  #reverse_lazy 클래스에서 사용하려면 reverse_lazy 사용해야함
    template_name = 'accountapp/delete.html'   #어떤 html 파일을 이용해서 볼것인지
