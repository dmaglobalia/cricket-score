from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.scorecard,name="scorecard"),
    path('manage_score',views.manage_score,name="manage_score"),
    path('<int:id>/',views.score_update,name='updatedata'),

]