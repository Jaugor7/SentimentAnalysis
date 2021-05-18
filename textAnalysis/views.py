from django.shortcuts import render, redirect
from django.contrib import messages
import pickle

with open('svmModel2.pkl', 'rb') as file:
    svmModel = pickle.load(file)

with open('tf2.pkl', 'rb') as file:
    tf = pickle.load(file)


# Create your views here.

def index(request):
    return render(request, 'index.html')

def giveMePredictionsBudyy(comment):

    review_vector = tf.transform([comment])
    pred =  svmModel.predict(review_vector)
    print(pred)

    return pred

def predict(request):
    if(request.method == "POST"):
        comment = request.POST.get('myComment')

        pred = giveMePredictionsBudyy(comment)
        # if(pred[0][0] <= 0.33):
        #     prediction = "Negative"
        # elif pred[0][0] <= 0.66:
        #     prediction = "Neutral"
        # else:
        #     prediction = "Positive" 
        
        # print(prediction)

        messages.success(request, str(pred))

    return redirect('/')
