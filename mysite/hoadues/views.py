from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from .models import  Address , Bill
import stripe

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


import stripe
stripe.api_key = 'sk_test_51MgxbRDasDOaJtxccHA7mDET3F449MUNLtbsIjdwOPW2KgZSvmB9CoHqkd0Ggpo6rNt9yIZtwGDXKEcGSXfnwHJP00W3DrZqt2'

YOUR_DOMAIN="http://localhost:8000"


# Create your views here.

def login_user( request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            print("MADDDDDE IT!!!!")
            return redirect('hoadues:member_page')
        else:
            # Return an 'invalid login' error message
            print("ERROROROROROROROROR!")
            return  render ( request, 'hoadues/login.html')
    else:
         return  render ( request, 'hoadues/login.html')

def logout_user(request):
    logout(request)
    return  render ( request, 'hoadues/login.html')

def index( request):
    return  render ( request, 'hoadues/login.html')


@login_required
def member_page (request ):

    bills = Bill.objects.filter(owner= request.user)
    bill = Bill.objects.filter(owner= request.user)[:1].get()
    print(bill.address)
    print(list(bills))

    sum=0
    for i in bills:
        if i.paid == False:
            sum += i.amt

    #address = Address.objects.get( owner =request.user)
    address = bill.address
    return  render ( request, 'hoadues/members.html' , {"address": address , "bills": bills , "sum": sum})

def check_out  (request):
    #get the sum of the payment
    #print("SUM " + str(sum))

    if request.method =='POST':
        sum = request.POST['SUM']
        print("hidden_sum" + str(sum))

        #multiply by *100
        sum = float(sum) * 100

        sum  = int(sum)
        print("sum_Ready" + str(sum))

        #make Intent to pay
        payment_intent = stripe.PaymentIntent.create(
        amount= sum,
        currency="usd",
        payment_method_types=["card"]

        )


        payment_method = "card"
        context={}

        if payment_method == "card":

            context['client_secret'] = payment_intent.client_secret
            #context['customer_email'] = request.user.email
            return render (request , 'hoadues/checkout.html', context)
    else:

        return member_page (request)



def postcheck_out  (request):
## POST PAID
   ## get this users bill
   print("Made it to postcheck_out!!!!!!")
   if request.method =='POST':
       print("POSTING........")
       bills = Bill.objects.filter(owner= request.user)
   ## go through all the bills
       for i in bills:
           i.paid = True
           i.save()
           print(i.paid)

       return member_page (request)
   else:

       return member_page (request)
