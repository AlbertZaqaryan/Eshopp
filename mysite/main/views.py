from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeSlider, HomeSliderActive
# Create your views here.


class HomeListView(ListView):
    template_name='main/index.html'

    def get(self, request):
        home_slider_active = HomeSliderActive.objects.all()[0]
        home_slider = HomeSlider.objects.all()
        return render(request, self.template_name, {
            'home_slider_active':home_slider_active,
            'home_slider':home_slider
        })
    

class ContactListView(ListView):
    template_name='main/contact-us.html'

    def get(self, request):
        return render(request, self.template_name)