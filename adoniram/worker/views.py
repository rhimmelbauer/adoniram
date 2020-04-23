from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.views.generic import CreateView, DetailView, UpdateView


def home(request):
    users = User.objects.all()
    for user in users:
        user.user_type = User.USER_TYPES[user.user_type - 1][1]

    
    return render(request, 'admin_home.html', {'users': users})


def create_user(request):
    page = {
        "title": "Create User",
        "subtitle": "User Information"
    }

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=True)
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, 'create.html', {'page': page, 'form': form})



class CreateWorkViewFrom(CreateView):
    model = Work
    form_class = CreateWorkForm
    pk_url_kwarg = 'iduser'
    template_name = "create.html"
    context_object_name = "work"
    page = {
        "title": "Report Work",
        "subtitle": "Work Information"
    }

    def form_valid(self, form):
        reported_work = form.save(commit=False)
        reported_work.iduser = User.objects.get(pk=1)
        reported_work.save()
        return redirect("home")