from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')  # Redirect to the same page after submission
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send email (configure your email settings in settings.py)
        send_mail(
            subject,
            message,
            email,
            ['your-email@example.com'],  # Replace with your email
        )

        return JsonResponse({'message': 'Your message has been sent. Thank you!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)
