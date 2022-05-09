from rest_framework import generics
from rest_framework.response import Response
from .serializer import StuSerializer
from .models import stu
class StuCreateApi(generics.CreateAPIView):
    queryset = stu.objects.all()
    serializer_class = StuSerializer
class StuApi(generics.ListAPIView):
    queryset = stu.objects.all()
    serializer_class = StuSerializer
class StuUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = stu.objects.all()
    serializer_class = StuSerializer
class StuDeleteApi(generics.DestroyAPIView):
    queryset = stu.objects.all()
    serializer_class =StuSerializer
class StuFindApi(generics.RetrieveAPIView):
    queryset = stu.objects.all()
    serializer_class =StuSerializer