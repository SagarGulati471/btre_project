from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
# Create your views here.
from contacts.models import Contact


@login_required(redirect_field_name='login')
def contact(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']


        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'User has already made a request')
                return  redirect('/listings/'+listing_id)


        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,        user_id=user_id )
        print(contact)
        contact.save()

        send_mail('property Listing Inquiry',
        'There has been an inquiry for '+  listing+ '.' + 'Sign in for more info',
        'sagargulati84@gmail.com',
         [realtor_email,'sagargulati471@gmail.com'],
         fail_silently=False)

        print('success******************************************')
        messages.success(request,"Your request has been submitted successfully")
        return redirect('/listings/'+listing_id)
    
    else:
        return redirect(request.META['HTTP_REFERER'])