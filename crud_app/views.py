from .models import Staff
from .forms import StaffForm, RegisterUserForm, LoginUserForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import CreateView
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.conf import settings
from .filters import StaffFilters



def create_view(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StaffForm()
        context = {
            'form': form
        }
        if not request.user.is_staff:
            return redirect('listview')
        return render(request, 'crud_app/create.html', context)

def listview(request):
    staff = Staff.objects.all().order_by('-id')

    paginator = Paginator(staff, 3)
    page_number = request.GET.get('page')
    dataset = paginator.get_page(page_number)
    if len(staff) == 0:
        raise Http404()
    myFilter = StaffFilters(request.GET, queryset=staff)
    dataset = myFilter.qs
    return render(request, 'crud_app/listview.html', {'staff': staff,'dataset': dataset, 'myFilter': myFilter})


def staff_detail_view(request, id):
    try:
        data = Staff.objects.get(id=id)
    except Staff.DoesNotExist:
        raise Http404('Такого сотрудника не существует')
    return render(request, 'crud_app/detailview.html', {'data': data})



def update_view(request, id):
    try:
        old_data = get_object_or_404(Staff, id=id)
        data = Staff.objects.get(id=id)

    except Exception:
        raise Http404('Такого сотрудника не существует')
    if request.method =='POST':
        form = StaffForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/{id}')
    else:
        form = StaffForm(instance = old_data)
        context ={
            'form':form,
            'data': data
        }
        if not request.user.is_staff:
            return redirect('listview')
        return render(request, 'crud_app/update.html', context)


def delete_view(request, id):
    try:
        data = get_object_or_404(Staff, id=id)
    except Exception:
        raise Http404('Такого сотрудника не существует')

    if request.method == 'POST':
        data.delete()
        return redirect('/')
    else:
        if not request.user.is_staff:
            return redirect('listview')
        return render(request, 'crud_app/delete.html')



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'crud_app/register.html'
    success_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'crud_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('login')


def logout_user(request):
    logout(request)
    return redirect('login')
