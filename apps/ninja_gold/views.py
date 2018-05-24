from django.shortcuts import render, HttpResponse, redirect
import random
from time import ctime

# Create your views here.
def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
    if "activities" not in request.session:
        request.session["activities"] = []
    return render(request, "ninja_gold/index.html")

def process_money(request, building):
    now = ctime()
    if (building == "farm"):
        gold = random.randrange(10, 21)
    elif (building == "cave"):
        gold = random.randrange(5, 11)
    elif (building == "house"):
        gold = random.randrange(2, 6)
    elif (building == "casino"):
        gold = random.randrange(-50, 51)
    else:
        gold = 0

    if gold > 0:
        activity = "Nice! You earned {} gold from the {}!  ({})".format(gold, building, now)
    elif gold < 0:
        activity = "Yikes! You lost {} gold from the {}... ({})".format(gold, building, now)
    else:
        activity = "Well... I guess 0 gold isn't bad... ({})".format(now)

    if "gold" not in request.session:
        request.session["gold"] = gold
    else:
        request.session["gold"] += gold

    if "activities" not in request.session:
        request.session["activities"] = [activity]
    else:
        request.session["activities"].insert(0, activity)

    return redirect(index)