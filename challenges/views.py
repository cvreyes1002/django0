from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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
    "december": "December Challenges!",
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
