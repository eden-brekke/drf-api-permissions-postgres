from rest_framework import generics
from .models import PetPic
from .serializers import PetPicSerializer


# Create your views here.
class PetPicList(generics.ListCreateAPIView):
  queryset = PetPic.objects.all()
  serializer_class = PetPicSerializer
  
  
class PetPicDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = PetPic.objects.all()
  serializer_class = PetPicSerializer
  