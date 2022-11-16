from django.shortcuts import HttpResponse, render

from youtubers.models import Youtuber
from .models import Slider, Team
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by(
        '-created_date').filter(is_featured=True)
    all_ytubers = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'all_ytubers': all_ytubers,
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')
