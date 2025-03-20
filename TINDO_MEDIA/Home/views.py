from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def blog(request):
    return render(request, 'blog.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

def contact_us(request):
    return render(request, 'contact_us.html')


from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us')  # Redirect to the same page after submission
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})
