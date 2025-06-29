from django.contrib import messages
from django.shortcuts import redirect, render

from student.forms import TempForm

# Create your views here.


def temp_view(request):
    print("t")

    # session
    request.session['teksheruu'] = "Teksherip atam"

    if request.method == "POST":
        form = TempForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['text']

            messages.success(request, f"We got your inputs! {email} and {message}")

            return redirect("main_page")
    else:
        form = TempForm()

    return render(request, 'templates/temp_template.html', {"form": form})

def main_page(request):

    count = request.session.get('visit', 0 )

    request.session['visit'] = count + 1

    request.session.set_expiry(60)

    login = request.session.get('logged', False)

    if not login:
        request.session['logged'] = True
    else:
        print(' you are logged')

    return render(request, 'templates/main_page.html', {"count":count + 1, 'logged': login})