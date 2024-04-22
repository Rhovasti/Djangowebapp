from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ExampleModel  # Replace ExampleModel with your actual model name

def home(request):
    return render(request, 'home.html')

class ExampleModelListView(ListView):
    model = ExampleModel
    template_name = 'examplemodel_list.html'

class ExampleModelDetailView(DetailView):
    model = ExampleModel
    template_name = 'examplemodel_detail.html'

