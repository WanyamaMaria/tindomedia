from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse
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

# def contact_us(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contacts')  # Redirect to the same page after submission
#     else:
#         form = ContactForm()
#     return render(request, 'contacts.html', {'form': form})



# from django.http import JsonResponse
# from django.core.mail import send_mail
# from django.shortcuts import render
# import logging
# from django.contrib import messages

# # Configure logging
# logger = logging.getLogger(__name__)

# def contact_view(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         subject = request.POST.get("subject")
#         message = request.POST.get("message")

#         email_subject = f"New Contact Form Submission: {subject}"
#         email_message = f"""
#         New message received from the website:

#         Name: {name}
#         Email: {email}
#         Subject: {subject}
#         Message:
#         {message}
#         """

#         try:
#             # Log before sending email
#             logger.info(f"Attempting to send email: {email_subject}")

#             send_mail(
#                 subject=email_subject,
#                 message=email_message,
#                 from_email="bryanatuhaire3@gmail.com",
#                 recipient_list=["bryanatuhaire3@gmail.com"],
#                 fail_silently=False,
#             )

#             logger.info("Email sent successfully!")
#             # return JsonResponse({"success": True, "message": "Your message has been sent successfully!"})
#             messages.success(request, "Your message has been sent successfully!") 
#             return HttpResponseRedirect(request.path)  # Refresh the page after submission 
        
#         except Exception as e:
#             logger.error(f"Error sending email: {e}")  # Log the error
#             # return JsonResponse({"success": False, "message": f"Error sending message: {e}"})
#             messages.error(request, "Error sending message. Please try again.")
#         # return redirect("/")  # Redirect to home page 
#             return render(request, "index.html")  # No error messages returned   

#     return render(request, "index.html")  # Ensure this is the correct template



# from django.http import HttpResponseRedirect
# from django.core.mail import send_mail
# from django.shortcuts import render
# import logging

# # Configure logging
# logger = logging.getLogger(__name__)

# def contact_view(request):
#     if request.method == "POST":
#         name = request.POST.get("name", "").strip()
#         email = request.POST.get("email", "").strip()
#         subject = request.POST.get("subject", "").strip()
#         message = request.POST.get("message", "").strip()

#         email_subject = f"New Contact Form Submission: {subject}"
#         email_message = f"New message received:\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage:\n{message}"

#         try:
#             # Log before sending email
#             logger.info(f"Sending email: {email_subject}")

#             send_mail(
#                 subject=email_subject,
#                 message=email_message,
#                 from_email="bryanatuhaire3@gmail.com",
#                 recipient_list=["bryanatuhaire3@gmail.com"],
#                 fail_silently=False,
#             )

#             logger.info("Email sent successfully!")

#             # Store success message in session
#             request.session["success_message"] = "Your message has been sent successfully!"
#             return HttpResponseRedirect(request.path)  # Refresh the page after submission

#         except Exception as e:
#             logger.error(f"Error sending email: {e}")  
#             return render(request, "index.html")  # No error messages returned

#     return render(request, "index.html")


from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render
import logging

# Configure logging
logger = logging.getLogger(__name__)

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        email_subject = f"New Contact Form Submission: {subject}"
        email_message = f"""
        New message received from the website:

        Name: {name}
        Email: {email}
        Subject: {subject}
        Message:
        {message}
        """

        try:
            # Log before sending email
            logger.info(f"Attempting to send email: {email_subject}")

            send_mail(
                subject=email_subject,
                message=email_message,
                from_email="bryanatuhaire3@gmail.com",
                recipient_list=["bryanatuhaire3@gmail.com"],
                fail_silently=False,
            )

            logger.info("Email sent successfully!")
            return JsonResponse({"success": True})  # No message returned
        
        except Exception as e:
            logger.error(f"Error sending email: {e}")  # Log the error
            return JsonResponse({"success": False})  # No message returned

    return render(request, "index.html")



# import feedparser # type: ignore
# from django.shortcuts import render

# def fetch_rss_news():
#     rss_url = "https://www.businessinsider.com/sai.rss"  # Replace with your desired RSS feed URL
#     feed = feedparser.parse(rss_url)
#     news_items = []

#     for entry in feed.entries[:10]:  # Limit to 10 latest news articles
#         news_items.append({
#             "title": entry.title,
#             "link": entry.link,
#             "summary": entry.summary,
#             "published": entry.published if "published" in entry else "Unknown Date",
#         })

#     return news_items

import feedparser  # type: ignore
from django.shortcuts import render

def fetch_rss_news():
    rss_url = "https://www.businessinsider.com/sai.rss"  # Business Insider RSS feed
    feed = feedparser.parse(rss_url)
    
    news_items = []
    for entry in feed.entries[:10]:  # Limit to 10 latest news articles
        news_items.append({
            "title": entry.title if "title" in entry else "No Title",
            "link": entry.link if "link" in entry else "#",
            "summary": entry.summary if "summary" in entry else "No Summary Available",
            "published": entry.published if "published" in entry else "Unknown Date",
            "image": entry.media_content[0]["url"] if "media_content" in entry else "/static/img/news-placeholder.jpg"
        })

    return news_items

def news_feed(request):
    news_articles = fetch_rss_news()
    return render(request, "index.html", {"articles": news_articles})



# def news_feed(request):
#     news_items = fetch_rss_news()
#     return render(request, "news_feed.html", {"news_items": news_items})
