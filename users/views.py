from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserRegisterForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


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


@login_required  # decorator wrap
def profile(request):
    """Profile View for user"""
    if request.method == "POST":
        u_form = UserUpdateForm(
            request.POST,
            instance=request.user,
        )
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile,
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form, "title": "Profile"}
    return render(request, "users/profile.html", context)
