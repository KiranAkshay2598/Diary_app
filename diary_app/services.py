from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework.authtoken.models import Token

from diary_app.models import Diary, Notes, ToDo, Events
from diary_app.serializers import (
    NoteSerializer,
    ToDoSerializer,
    EventSerializer
)


def build_response(status_val, data):
    response = {
        'status': status_val,
        'data': data
    }
    return response


def register_diary(value):
    try:
        username = value.get('username')
        password = value.get('password')
        name = value.get('name') or username

        if User.objects.filter(username=username).exists():
            return build_response('failure', {'error': 'A user with this username already exists. Please log in.'})

        with transaction.atomic():
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
            Diary.objects.create(name=name, user=user)
            return_data = {'token': token.key}
            return build_response('success', return_data)
    except Exception as e:
        return build_response('failure', {'error': str(e)})


def login_diary(data):
    try:
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            status_val = 'success'
            return_data = {'token': token.key}
        else:
            status_val = 'failure'
            return_data = {
                'error': "Invalid credentials or user does not exist. Please register first."
            }
        return build_response(status_val, return_data)
    except Exception as exc:
        return build_response('failure', {'error': str(exc)})


def init_note(data, user):
    try:
        note_date = data.get('note_date')
        image = data.get('image')
        diary_note = data.get('note')
        
        diary, _ = Diary.objects.get_or_create(user=user, defaults={'name': user.username})
        notes = Notes.objects.create(note_date=note_date, image=image, note=diary_note, diary=diary)
        notedata_serializer = NoteSerializer(notes)
        return build_response('success', notedata_serializer.data)

    except Exception as e:
        return build_response('failure', {'error': str(e)})


def view_note(data):
    try:
        if data:
            note_date = data.get('note_date')
            diary_note = data.get('note')
            if note_date:
                notes = Notes.objects.filter(note_date=note_date)
                notedata_serializer = NoteSerializer(notes, many=True)
                return build_response('success', notedata_serializer.data)
            elif diary_note:
                notes = Notes.objects.filter(note__icontains=diary_note)
                notedata_serializer = NoteSerializer(notes, many=True)
                return build_response('success', notedata_serializer.data)
        
        notes = Notes.objects.all()
        notedata_serializer = NoteSerializer(notes, many=True)
        return build_response('success', notedata_serializer.data)

    except Exception as e:
        return build_response('failure', {'error': str(e)})


def init_todo(data):
    try:
        todo = ToDo.objects.create(title=data.get('title'), note=data.get('note'))
        todo_serializer = ToDoSerializer(todo)
        return build_response('success', todo_serializer.data)

    except Exception as e:
        return build_response('failure', {'error': str(e)})


def update_todo(data):
    try:
        note_id = data.get('note_id')
        todolist = ToDo.objects.filter(note_id=note_id)
        if todolist.exists():
            updated = False
            for todo in todolist:
                if not todo.done:
                    todo.done = True
                    todo.save()
                    updated = True
            
            if updated:
                todo_serializer = ToDoSerializer(todolist, many=True)
                return build_response('success', todo_serializer.data)
            else:
                return build_response('failure', {'error': "All todo items for this note are already completed."})
        else:
            return build_response('failure', {'error': "No todo items found for this note ID."})
    except Exception as e:
        return build_response('failure', {'error': str(e)})


def init_event(data, user):
    try:
        event_time = data.get('event_time')
        event_name = data.get('event_name')
        diary, _ = Diary.objects.get_or_create(user=user, defaults={'name': user.username})
        
        if not Events.objects.filter(event_time=event_time, diary=diary).exists():
            events = Events.objects.create(event_time=event_time, event_name=event_name, diary=diary)
            eventdata_serializer = EventSerializer(events)
            return build_response('success', eventdata_serializer.data)
        else:
            return build_response('failure', {'error': "This date and time is already booked for another event."})

    except Exception as e:
        return build_response('failure', {'error': str(e)})


def view_event(data):
    try:
        if data:
            event_time = data.get('event_time')
            event_name = data.get('event_name')
            if event_time:
                events = Events.objects.filter(event_time=event_time)
                eventdata_serializer = EventSerializer(events, many=True)
                return build_response('success', eventdata_serializer.data)
            elif event_name:
                events = Events.objects.filter(event_name__icontains=event_name)
                eventdata_serializer = EventSerializer(events, many=True)
                return build_response('success', eventdata_serializer.data)
        
        events = Events.objects.all()
        eventdata_serializer = EventSerializer(events, many=True)
        return build_response('success', eventdata_serializer.data)

    except Exception as e:
        return build_response('failure', {'error': str(e)})


def update_event(data):
    try:
        event_id = data.get('event_id')
        event = Events.objects.filter(id=event_id).first()
        if not event:
            return build_response('failure', {'error': "Event not found for the given event_id."})
        
        if not event.remind:
            event.remind = True
            event.save()
            event_serializer = EventSerializer(event)
            return build_response('success', event_serializer.data)
        else:
            return build_response('failure', {'error': "This event reminder is already set to active."})
    except Exception as e:
        return build_response('failure', {'error': str(e)})
