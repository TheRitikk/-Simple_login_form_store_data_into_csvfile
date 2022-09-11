from dataclasses import field
from tkinter import Variable
from django.shortcuts import render
import csv

from home.models import datalogin

# Create your views here.
def index(request):
    queryDict=dict(request.GET)
    # fieldnames = {'name','email','phone'}
    with open('mycsvfile.csv', 'a', newline='') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.writer(f)
        w.writerow(queryDict.values())
    return render(request,'index.html')
