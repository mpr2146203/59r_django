from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
# movie ticket task
# def ticket(request):

#     movie_name = "3BHK"
#     show_time = "11:00 AM"
#     ticket_cost = "150"
#     ticket_count = "200"
#     total_price = str(int(ticket_cost) * int(ticket_count))


#     info = {"movie":movie_name,
#             "show time":show_time,
#             "ticket_cost":ticket_cost,
#             "total_no_of_tickets":ticket_count,
#             "total_price":total_price
#             }
    
#     return JsonResponse({"status":"success","data":info})

# quesry aprms ?

def ticket(request):

    movie_name = request.GET.get("movie_name","ADBHUTAM")
    show_time = request.GET.get("show_time","11:00 AM")
    ticket_cost = request.GET.get("ticket_cost","150")
    ticket_count = request.GET.get("ticket_count","150")
    total_price = str(int(ticket_cost) * int(ticket_count))


    info = {"movie":movie_name,
            "show time":show_time,
            "ticket_cost":ticket_cost,
            "total_no_of_tickets":ticket_count,
            "total_price":total_price
            }
    
    return JsonResponse({"status":"success","data":info})