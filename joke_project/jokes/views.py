
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Joke
import requests

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('joke_home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def joke_home(request):
    user_joke, created = Joke.objects.get_or_create(user=request.user)
    if created or not user_joke.text:
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        if response.status_code == 200:
            joke = response.json()
            user_joke.text = f"{joke['setup']} - {joke['punchline']}"
            user_joke.save()
    return render(request, 'home.html', {'joke': user_joke.text})


