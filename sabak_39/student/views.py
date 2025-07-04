from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from student.forms import TempForm, UserRegistratinForm,  UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from student.models import Student
# Create your views here.


def temp_view(request):
    print("t")

    # session
    request.session['teksheruu'] = "Teksherip atam"

    # cookie
    temp = request.COOKIES.get('temp', 'jok')


    if request.method == "POST":
        form = TempForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['text']

            messages.success(request, f"We got your inputs! {email} and {message}")

            return redirect("main_page")
    else:
        form = TempForm()

    return render(request, 'templates/temp_template.html', {"form": form, "cookie": temp})


@login_required(login_url='login')
def main_page(request):

    count = request.session.get('visit', 0 )

    request.session['visit'] = count + 1

    request.session.set_expiry(60)

    login = request.session.get('logged', False)
    big_information = request.session['some_data'] ={
        'info':[
            3,4324,23,4,324,32,423,42
        ]
    }

    # cookie 
    temp = request.COOKIES.get('temp', 'jok')
    temp2 = request.COOKIES.get('browser', 'jok')
    if not login:
        request.session['logged'] = True
    else:
        print(' you are logged')

    return render(request, 'templates/main_page.html', {"count":count + 1, 'logged': login, "cookie": temp2})


# cookies

def temp_cookies(request):
    response = HttpResponse("Bizdin cookie response")

    response.set_cookie('temp', 'Hello', max_age=120)

    response.set_cookie('dark_mode', '1', max_age=60)

    return response



# authenticate

def register(request):
    if request.method == 'POST':
        form = UserRegistratinForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password'])

            user.save()

            messages.success(request, "Siz registration boldunuz! Log in bolunuz!")
            return redirect('login')
    else:
        form = UserRegistratinForm()
    
    return render(request, 'templates/register.html', {'form': form})

def login_view(request):
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user) 
                messages.success(request, "Siz login boldunuz! ")
                request.session['logged']=True
                return redirect('main_page')
            else:
                messages.error(request, "tuura emes username jana password")
    else:
        form = UserLoginForm()
    return render(request, 'templates/login.html', {'form': form})

def logout_view(request):
    
    logout(request)
    request.session.flush()
    messages.info(request, "Log out boldunuz")

    return redirect('login')


from django.contrib.auth.decorators import permission_required


@permission_required("auth.view_user", raise_exception=True)
def admin_page_view(request):
    return render(request,'templates/admin_page.html')

from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

class AdminPageView(PermissionRequiredMixin, TemplateView):
    template_name = 'templates/admin_page.html'

    permission_required = 'auth.view_user'

    raise_exception = True


# student list

@permission_required("auth.view_user", raise_exception=True)
def list_students(request):

    students = Student.objects.all()

    return render(request,'templates/student_list.html', {'students': students})