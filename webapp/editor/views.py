from editor.models import SimpleModel
from editor.serializers import SimpleSerializer
from rest_framework import generics


class SimpleModelListCreator(generics.ListCreateAPIView):
    queryset = SimpleModel.objects.all()
    serializer_class = SimpleSerializer
