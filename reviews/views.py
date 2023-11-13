from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def review(request):
    if request.method == 'POST':
        entered_username = request.POST['username']    # POST will hold the dictionary of the returned form data

        if entered_username == "":
            return render(request, "reviews/review.html", {
                "has_error": True
            })
        print(entered_username)
        return HttpResponseRedirect("/thank-you")
    
    return render(request, "reviews/review.html")


def thank_you(request):
    return render(request, "reviews/thank_you.html")