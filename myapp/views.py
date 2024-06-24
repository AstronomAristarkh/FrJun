from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    return HttpResponse("Hello, world!")

def coin(request):
    result = random.choice(['Орёл', 'Решка'])
    return HttpResponse(f'<h1>{result}</h1>')

def random_roll(request):
    result = random.randint(1, 6)
    return HttpResponse(f'<h1>{result}</h1>')

def random_number(request):
    result = random.randint(0, 100)
    return HttpResponse(f'<h1>{result}</h1>')

def aboutme(request):
    result = """<h1>Обо мне:</h1>  
            <p>
                <img src="https://i.pinimg.com/originals/a9/f7/55/a9f75550e3ccc34aa20bb52cb590d4ca.jpg" alt="Doctor_Who" width="200"> 
                Занимаюсь много чем. В основном, смотрю сериалы и ем. Но иногда успеваю преподавать, учиться и заниматься научной работой. 

            </p>  """
    return HttpResponse(result)

def glav(request):
    result = """ <h1>Главная:</h1>  
            <p>
                Вооооть 

            </p>  """
    return HttpResponse(result)

