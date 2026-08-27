from django.urls import path
from diary_app import views

urlpatterns = [
    path('api/diary/register', views.RegisterDiary.as_view(), name='RegisterDiary'),
    path('api/diary/login', views.LoginDiary.as_view(), name='LoginDiary'),
    path('api/diary/notes', views.Notes.as_view(), name='Notes'),
    path('api/diary/viewnotes', views.Notes.as_view(), name='ViewNotes'),
    path('api/diary/todo', views.ToDo.as_view(), name='ToDo'),
    path('api/diary/updatetodo', views.UpdateToDo.as_view(), name='UpdateToDo'),
    path('api/diary/events', views.Events.as_view(), name='Events'),
    path('api/diary/viewevents', views.Events.as_view(), name='ViewEvents'),
    path('api/diary/updateevents', views.UpdateEvents.as_view(), name='UpdateEvents'),
]
