from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from diary_app.serializers import (
    AuthenticationSerializer,
    NoteSerializer,
    NoteRequestSerializer,
    ToDoRequestSerializer,
    EventSerializer
)
from diary_app.services import (
    register_diary,
    login_diary,
    init_note,
    view_note,
    init_todo,
    update_todo,
    init_event,
    view_event,
    update_event
)


class RegisterDiary(APIView):
    serializer_class = AuthenticationSerializer

    def post(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            res_data = register_diary(serializer.validated_data)
            http_status = status.HTTP_201_CREATED if res_data.get('status') == 'success' else status.HTTP_400_BAD_REQUEST
            return Response(res_data, status=http_status)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginDiary(APIView):
    serializer_class = AuthenticationSerializer

    def post(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            res_data = login_diary(serializer.validated_data)
            http_status = status.HTTP_200_OK if res_data.get('status') == 'success' else status.HTTP_400_BAD_REQUEST
            return Response(res_data, status=http_status)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Notes(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get(self, request):
        res_data = view_note(data=request.query_params)
        return Response(res_data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        serializer = NoteRequestSerializer(data=request.data)
        if serializer.is_valid():
            res_data = init_note(serializer.validated_data, user)
            http_status = status.HTTP_201_CREATED if res_data.get('status') == 'success' else status.HTTP_400_BAD_REQUEST
            return Response(res_data, status=http_status)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDo(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ToDoRequestSerializer(data=request.data)
        if serializer.is_valid():
            res_data = init_todo(serializer.validated_data)
            http_status = status.HTTP_201_CREATED if res_data.get('status') == 'success' else status.HTTP_400_BAD_REQUEST
            return Response(res_data, status=http_status)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateToDo(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        res_data = update_todo(data=request.data)
        http_status = status.HTTP_200_OK if res_data.get('status') == 'success' else status.HTTP_400_BAD_REQUEST
        return Response(res_data, status=http_status)


class Events(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        res_data = view_event(data=request.query_params)
        return Response(res_data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            res_data = init_event(serializer.validated_data, user)
            http_status = status.HTTP_201_CREATED if res_data.get('status') == 'success' else status.HTTP_400_BAD_REQUEST
            return Response(res_data, status=http_status)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateEvents(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        res_data = update_event(data=request.data)
        http_status = status.HTTP_200_OK if res_data.get('status') == 'success' else status.HTTP_400_BAD_REQUEST
        return Response(res_data, status=http_status)
