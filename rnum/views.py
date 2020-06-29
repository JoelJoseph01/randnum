from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'rnum/home.html')

def number(request):
    n=list('1234567890')
    length=int(request.GET.get('length',9))

    randomnumber=''
    for x in range(length):
        randomnumber+=random.choice(n)
    return render(request,'rnum/number.html',{'number':randomnumber})
