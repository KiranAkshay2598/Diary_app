from rest_framework import serializers
from diary_app.models import Diary, Notes, ToDo, Events


class AuthenticationSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    username = serializers.CharField()
    password = serializers.CharField()


class ToDoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('note', 'title')


class ToDoSerializer(serializers.ModelSerializer):
    title = serializers.CharField()

    class Meta:
        model = ToDo
        fields = ('id', 'title', 'done', 'note_id', 'cdate', 'udate')


class NoteRequestSerializer(serializers.ModelSerializer):
    note_date = serializers.DateTimeField(input_formats=['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S', 'iso-8601'])
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Notes
        fields = ('note_date', 'note', 'image')


class NoteSerializer(serializers.ModelSerializer):
    note_date = serializers.CharField()
    todo_list = serializers.SerializerMethodField()

    def get_todo_list(self, instance):
        to_dos = instance.todo_set.all()
        todo_ser = ToDoSerializer(to_dos, many=True)
        return todo_ser.data

    class Meta:
        model = Notes
        fields = ('id', 'note_date', 'note', 'image', 'cdate', 'udate', 'todo_list')


class EventSerializer(serializers.ModelSerializer):
    event_time = serializers.CharField()
    event_name = serializers.CharField()

    class Meta:
        model = Events
        fields = ('id', 'event_time', 'event_name', 'remind', 'cdate', 'udate')
