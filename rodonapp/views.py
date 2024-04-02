from django.shortcuts import render,redirect
from .models import ContactMessage
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import auth
from django.conf import settings

def static_url(request):
    return {
        'STATIC_URL': settings.STATIC_URL,
    }


def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def adminlog(request):
    messages = ContactMessage.objects.all()

    
    return render(request,'adminlog.html', {'messages': messages}   )

def admin(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('adminlog')
           
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/')
    return render(request, 'index.html')

def contact_submit(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Send the form data to the admin
        contact_message = ContactMessage.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)
        
        # Return a JSON response indicating success
        return JsonResponse({'success': True})
    
    # If the request method is not POST, return a JSON response indicating failure
    return JsonResponse({'success': False})
def delete_message(request):
    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        message = get_object_or_404(ContactMessage, pk=message_id)
        message.delete()
        return JsonResponse({'message': 'Message deleted successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

def properties(request):
    return render(request,'properties.html')

def signin(request):
    return render(request,'signin.html')

def user_logout(request):
    auth.logout(request)
    return redirect('signin')