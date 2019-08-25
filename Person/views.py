from django.shortcuts import render,HttpResponse

from django.core.mail import send_mail
from django.conf import settings


def email(request):
    # import pdb;pdb.set_trace()
    subject = 'Thank you for registering to our Site'
    message = 'Hurrah!!!!!  You Added to Technology World \n Now You Can Explore Your Better Ways '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mukesh.yadav@d3analytics.com']
    send_mail( subject, message, email_from, recipient_list ,"html")
    return HttpResponse("Email Successfully Sent")
