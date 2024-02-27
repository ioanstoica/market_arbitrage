from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth import logout

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = (
        "login"  # Redirecționează către pagina de login după înregistrare cu succes
    )
    template_name = (
        "account/signup.html"  # Specifică calea către template-ul pentru înregistrare
    )


def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            # Mesaj de eroare în caz că autentificarea eșuează
            return HttpResponse("Autentificare eșuată")

    return render(request, "account/login.html", {})

def LogOutView(request):
    logout(request)
    return render(request, "account/logout.html")