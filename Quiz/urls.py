from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'Quiz'


urlpatterns = [
    path('certificate/<int:verification>',views.certificate,name="certificate"),
    path('Slide/<int:that_slide_no>', views.slide, name="slide"),
    path('Submission/<int:that_quiz_id>', views.Submission, name="Submission"),
    path('question/<int:that_quiz_id>', views.question, name="question"),
    path('Mquiz/', views.Mquiz, name="Mquiz"),
    path('Score/<int:verification>', views.Score, name="Score"),

]
