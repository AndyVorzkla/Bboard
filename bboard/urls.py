from django.urls import path
from .views import index, by_rubric, BbCreateView

app_name = 'bboard'

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('', index, name='index'),

]
