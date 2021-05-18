from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def giveMePredictionsBudyy(comment):

    ###

    return "Positive"

def predict(request):
    if(request.method == "POST"):
        comment = request.POST.get('myComment')

        prediction = giveMePredictionsBudyy(comment)
        if(prediction == 'Positive'):
            messages.success(request, prediction)
        elif(prediction == 'Neutral'):
            messages.warning(request, prediction)
        else:
            messages.error(request, prediction)

    return redirect('/')
