from rest_framework import generics, permissions
from django.contrib.auth.models import User

from .models import Note
from .serializers import UserSerializer, NoteSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class NoteListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(
            author=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(
            author=self.request.user
        )
