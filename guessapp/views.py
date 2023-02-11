from django.shortcuts import render

from .models import History

import random

# Create your views here.

def index(request):
    if request.method == "POST" :
        number = int(request.POST.get('number'))
        attempts = int(request.POST.get("attempts"))
        guess = request.POST.get("guess")

        if guess != '':
            guess = int(guess)
            attempts += 1

            if guess == number:
                message = f'Bingo! {number}'
                hist = History(number=number, attempts=attempts)
                hist.save()
            elif guess > number:
                message = f'Your guess ({guess}) is high'
            else:
                message = f'Your guess ({guess}) is low'
        else:
            message = 'Try again'

    else:
        attempts = 0  
        number = random.randint(1, 100+1)
        message = "Guess number (between 1 and 100)"

    return render(request, "guessapp/index.html", 
                  {'attempts': attempts, 'number': number, 'message': message})


def history(request):
    histories = History.objects.order_by('-finished_at')
    return render(request, "guessapp/history.html", {'histories': histories})