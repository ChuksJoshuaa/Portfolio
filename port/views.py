from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Project, Contact, About
from django.core.mail import send_mail
from django.contrib import messages


def home_view(request):
    project = Project.objects.order_by('list_date')
    paginator = Paginator(project, 3)
    page = request.GET.get('page')
    page_project = paginator.get_page(page)
    if request.method == "POST":
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        if email and name and message:
            send_mail(
                'Job Request Form',
                message,
                email,
                ['chuksmbanasoj@gmail.com'],
                fail_silently=True
            )
            messages.success(request, f"Message sent successfully, i will get back to you shortly!! {name}")
            return redirect("home")
        else:
            messages.warning(request, f"Please fill in the form completely before submitting")
            return redirect("home")
    context = {
        'main': page_project,
    }
    return render(request, 'home.html', context)


def about_view(request):
    about = About.objects.all()

    context = {
        'about': about
    }

    return render(request, 'about.html', context)


def search_view(request):
    query = request.GET['query']
    post = Project.objects.filter(tool1__icontains=query) or Project.objects.filter(title__icontains=query)
    context = {
        "page": post
    }
    return render(request, 'search.html', context)



def all_project(request):
    project = Project.objects.order_by('list_date')

    paginator = Paginator(project, 6)
    page = request.GET.get('page')
    page_project = paginator.get_page(page)

    context = {
        'page': page_project
    }

    return render(request, 'main.html', context)
