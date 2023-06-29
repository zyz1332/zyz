from django.shortcuts import HttpResponse
from django.http import JsonResponse
from zyz import models
import json
# Create your views here.

def add(request):
    isbn=request.GET.get("isbn")
    bookname=request.GET.get("bookname")
    publishertime=request.GET.get("publishertime")
    models.Food.objects.create(isbn=isbn,bookname=bookname,publishertime=publishertime)
    return HttpResponse({"code":0,"message":"add sucessfully"})
    
def delete(request):
    isbn=request.GET.get("isbn")
    models.Food.objects.filter(isbn=isbn).delete()
    return HttpResponse({"code": 0, "message": "delete successfully"})

def update(request):
    isbn=request.GET.get("isbn")
    bookname=request.GET.get("bookname")
    publishertime=request.GET.get("publishertime")
    models.Food.objects.filter(isbn=isbn).update(bookname=bookname, publishertime=publishertime)
    return HttpResponse({"code": 0, "message": "update successfully"})

def get(request):
    isbn=request.GET["isbn"]
    info = models.Food.objects.filter(isbn=isbn).values()
    list=[]
    for i in info:
        list.append(i)
    return HttpResponse(json.dumps(list))

def select(request):
    a=models.Food.objects.all().values()
    list=[]
    for i in a:
        list.append(i)
    return HttpResponse(json.dumps(list))