from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "January Challenges!",
    "february": "February Challenges!",
    "march": "March Challenges!",
    "april": "April Challenges!",
    "may": "May Challenges!",
    "june": "June Challenges!",
    "july": "July Challenges!",
    "august": "August Challenges!",
    "september": "September Challenges!",
    "october": "October Challenges!",
    "november": "November Challenges!",
    "december": None
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    # return HttpResponse(months)
    return render(request, "challenges/index.html", {
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound("This month is not supported!")
