from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
from decimal import Decimal
from django.utils.html import strip_tags
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_protect
import json
from django.contrib.auth.hashers import make_password,check_password
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
import os
from django.conf import settings
import shutil
from requests.exceptions import ConnectionError
import requests 
from django.contrib.auth.decorators import login_required
# from accounts.models import Transaction,Card
from django.db.models import Sum




# @login_required(login_url='login')
# def home_view(request):
#     account = request.user  # Assuming the logged-in user is an Account instance

#     other_transactions = Transaction.objects.filter(user=account).order_by('-transaction_date')
#     transfer_transactions = other_transactions.filter(transaction_type="transfer")
#     cards = Card.objects.filter(user=account)

#     # Calculate total credits: sum amounts for transactions marked as "completed"
#     credit_agg = Transaction.objects.filter(
#         user=account,
#         transaction_type="deposit"
#     ).aggregate(total=Sum('amount'))
#     total_credits = credit_agg['total'] or 0.00

#     # Calculate total debits: sum amounts for transactions marked as "transfer"
#     debit_agg = Transaction.objects.filter(
#         user=account,
#         transaction_type="transfer"
#     ).aggregate(total=Sum('amount'))
#     total_debits = debit_agg['total'] or 0.00

#     context = {
#         "transfer_transactions": transfer_transactions,
#         "other_transactions": other_transactions,
#         "cards": cards,
#         "total_credits": total_credits,
#         "total_debits": total_debits,
#     }
#     return render(request, 'index.html', context)



@login_required(login_url='login')
def profile_view(request):
    return render(request, 'profile.html')


def home_page(request):
    return render(request, 'home_page/index.html')

def contact_us(request):
    return render(request, 'home_page/Contact-Us.html')

def about_page(request):
    return render(request, 'home_page/about/index.html')

def services_page(request):
    return render(request, 'home_page/services/index.html')

def home_insurance_page(request):
    return render(request, 'home_page/home_insurance/index.html')

def business_insurance_page(request):
    return render(request, 'home_page/business_insurance/index.html')

def health_insurance_page(request):
    return render(request, 'home_page/health_insurance/index.html')

def news_page(request):
    return render(request, 'home_page/news/index.html')

def contact_page(request):
    return render(request, 'home_page/contact/index.html')
