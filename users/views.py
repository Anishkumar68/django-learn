from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserRegisterForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout


# Create your views here.
def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Your account has been created  {username}!, Now you can login.",
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def logout_view(request):
    logout(request)

    return render(request, "users/logout.html", {"title": "logged_out"})
