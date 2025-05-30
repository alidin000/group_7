from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def simple_html(request):
    html = """"<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Majestic Hooves - Horse Sales</title>
</head>
<body>
  <header>
    <h1>Majestic Hooves</h1>
    <p>Premium Horses for Sale</p>
  </header>

  <nav>
    <ul>
      <li><a href="#about">About Us</a></li>
      <li><a href="#horses">Our Horses</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>

  <section id="about">
    <h2>About Us</h2>
    <p>We breed and sell top-quality horses for riding, racing, and companionship. Trusted by horse lovers across the country.</p>
  </section>

  <section id="horses">
    <h2>Our Horses</h2>
    <ul>
      <li><strong>Storm</strong> - Arabian, 5 years old, fast and elegant</li>
      <li><strong>Blaze</strong> - Mustang, 3 years old, wild spirit with strong endurance</li>
      <li><strong>Luna</strong> - Friesian, 7 years old, graceful and calm</li>
    </ul>
  </section>

  <section id="contact">
    <h2>Contact Us</h2>
    <p>Email: sales@majestichooves.com</p>
    <p>Phone: +1 234 567 8901</p>
  </section>

  <footer>
    <p>&copy; 2025 Majestic Hooves. All rights reserved.</p>
  </footer>
</body>
</html>
    """
    html2 = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Majestic Hooves - Horse Sales</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
      color: #333;
    }

    header {
      background-color: #8b4513;
      color: white;
      padding: 20px;
      text-align: center;
    }

    nav {
      background-color: #deb887;
      padding: 10px;
      text-align: center;
    }

    nav ul {
      list-style-type: none;
      padding: 0;
    }

    nav li {
      display: inline;
      margin: 0 15px;
    }

    nav a {
      text-decoration: none;
      color: #333;
      font-weight: bold;
    }

    section {
      padding: 20px;
      max-width: 800px;
      margin: auto;
      background-color: white;
      margin-top: 10px;
      border-radius: 8px;
    }

    footer {
      background-color: #8b4513;
      color: white;
      text-align: center;
      padding: 10px;
      margin-top: 20px;
    }

    h1, h2 {
      margin-top: 0;
    }
  </style>
</head>
<body>
  <header>
    <h1>Majestic Hooves</h1>
    <p>Premium Horses for Sale</p>
  </header>

  <nav>
    <ul>
      <li><a href="#about">About Us</a></li>
      <li><a href="#horses">Our Horses</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>
  </nav>

  <section id="about">
    <h2>About Us</h2>
    <p>We breed and sell top-quality horses for riding, racing, and companionship. Trusted by horse lovers across the country.</p>
  </section>

  <section id="horses">
    <h2>Our Horses</h2>
    <ul>
      <li><strong>Storm</strong> – Arabian, 5 years old, fast and elegant</li>
      <li><strong>Blaze</strong> – Mustang, 3 years old, wild spirit with strong endurance</li>
      <li><strong>Luna</strong> – Friesian, 7 years old, graceful and calm</li>
    </ul>
  </section>

  <section id="contact">
    <h2>Contact Us</h2>
    <p>Email: sales@majestichooves.com</p>
    <p>Phone: +1 234 567 8901</p>
  </section>

  <footer>
    <p>&copy; 2025 Majestic Hooves. All rights reserved.</p>
  </footer>
</body>
</html>

"""
    return  HttpResponse(html2)

def main_page(request):
    return HttpResponse("<h1>Main page</h1>")


from django.views import View

class TempView(View):
    def get(self,response):
        return HttpResponse("<h1>Main page  (class based view)</h1>")
    


def json(request):
    json_text = {
        "name":"Alidin",
        "age":"34"
    }
    return JsonResponse(json_text)

def temp(request):
    t = json(None)
    print(t)
    # name = t.getvalue("name")
    name = ":"

    return HttpResponse(name)

def get_id(request, id):
    print(f"I got this id")
    return HttpResponse(f"This id was returned-{id}")

def get_name(request, name):
    return HttpResponse(f"This name was returned {name}")


from .models import Student
from django.shortcuts import get_object_or_404, get_list_or_404


def get_student(request):
    students = Student.objects.all() # select * from students
    student = Student.objects.get(id=2)
    student2 = get_list_or_404(Student, group="7")

    print(student2)

    t = "<ul>"

    for st in student2:
        t = t + f"<li>{st}</li>"
    t = t + "</ul>"
    return HttpResponse(t)