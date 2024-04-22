from django.urls import path
from .views import home, ExampleModelListView, ExampleModelDetailView

urlpatterns = [
    path('', home, name='home'),
    path('list/', ExampleModelListView.as_view(), name='list'),
    path('detail/<int:pk>/', ExampleModelDetailView.as_view(), name='detail'),
]

