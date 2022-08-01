from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import oracleapp.model_df.cart as ct

def view_Cart_List(request) :
    df = ct.getCart_list()
    
    context = {"df" : df}
    return render(request,
                    "oracleapp/cart/cart_list.html",
                    context)
    
def view_Cart_List2(request) :
    df = ct.getCart_list2()
    
    context = {"df" : df}
    return render(request,
                    "oracleapp/cart/cart_list2.html",
                    context)