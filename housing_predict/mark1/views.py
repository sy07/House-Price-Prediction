from django.shortcuts import render
from django.http import HttpResponse
import joblib

def homepageview(request):
    return render(request,'home.html')

def result(request):

    lm = joblib.load('final_model.sav')

    lis = []

    lis.append(request.GET['income'])
    lis.append(request.GET['age'])
    lis.append(request.GET['room'])
    lis.append(request.GET['bedroom'])
    lis.append(request.GET['pop'])

    #print(lis)

    ans = lm.predict([lis])

    return render(request,'result.html',{'ans':ans,'lis':lis})