from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import EmailMessageForm


def home(request):
    return render(request, 'appp/home.html')



def colleges(request):
    return render(request, 'appp/colleges.html')



def students(request):
    students_data = [
        {'sno':'1','name': 'Mamatha', 'branch': 'CSE', 'age': 19},
        {'sno':'2','name': 'Navya', 'branch': 'IT', 'age': 18},
        {'sno':'3','name': 'Teju', 'branch': 'AI',  'age': 20},
    ]
    return render(request, 'appp/students.html', {'students': students_data})

def address(request):
    return render(request, 'appp/address.html')



def send_email(request):
    if request.method == "POST":
        form = EmailMessageForm(request.POST)
        if form.is_valid():
            email_obj = form.save()  
            send_mail(
                subject=email_obj.subject,
                message=email_obj.message,
                from_email="adarimamatha561@gmail.com",
                recipient_list=["24b01a1201@svecw.edu.in"],
                fail_silently=False,
                    )
            return HttpResponse("<h1>Succesfully sent mail  </h1>")
    else:
        form = EmailMessageForm()
    return render(request, "appp/send_email.html", {"form": form})




