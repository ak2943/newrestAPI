from django.shortcuts import render
from  .forms import InputForm

# Create your views here.
def myView(request):
    context={ }
    context['form']= InputForm()
    return render(request, "home.html", context)

