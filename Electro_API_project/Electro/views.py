from rest_framework import generics
from .models import Electro
from .serializer import ElectroSerializer

class ElectroListView(generics.ListCreateAPIView):
    queryset = Electro.objects.all()
    serializer_class = ElectroSerializer


class ElectroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Electro.objects.all()
    serializer_class = ElectroSerializer