from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    form = StudentRegistration() 
    return render(request, 'enroll/userregistration.html',
                  {'form': form})
