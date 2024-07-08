from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.views import View
from account.forms import UserForm


class UserCreate(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'account/register.html', context={'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'account/register.html', context={'form': form})



