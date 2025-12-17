from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse


def view1(request):
    return HttpResponse("hello from view1")

def view2(request):
    return JsonResponse({"name":"mpr","batch":"59r"})

def dynamicview(request):
    qp1 = request.GET.get("name")
    return HttpResponse(f"hello {qp1}")

def personalInfo(request):
    name = request.GET.get("name")
    city = request.GET.get("city")
    role = request.GET.get("role")
    type = request.GET.get("type","model")

    info = {"name":name,"city":city,"role":role,"type":type}

    return JsonResponse({"status":"success","data":info})

def temp1(request):

    return render(request,'simple.html')