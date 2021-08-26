from .models import Passenger
from .serializers import PassengerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import  APIView
from django.http import Http404
from rest_framework import  generics, mixins, viewsets

'''
Function Based views
'''
# @api_view(['GET','POST'])
# def passenger_list(request):
#
#     if request.method == "GET":
#         passenger = Passenger.objects.all()
#         serializer = PassengerSerializer(passenger,many=True)
#         return Response(serializer.data)
#
#     if request.method == "POST":
#         serializer = PassengerSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','POST','PUT','DELETE'])
# def passenger_detail(request,pk):
#     try:
#         passenger = Passenger.objects.get(pk=pk)
#     except Passenger.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "GET":
#         serializer = PassengerSerializer(passenger)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         serializer = PassengerSerializer(passenger,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         passenger.delete()
#         return Response(status=status.HTTP_204_DELETED)

'''
Class Based views
'''

# class PassengerListView(APIView):
#
#     def get(self,request):
#         passenger = Passenger.objects.all()
#         serializer = PassengerSerializer(passenger,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer = PassengerSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
#
#
# class  PassengerDetailView(APIView):
#     def get_object(self,pk):
#         try:
#             return Passenger.objects.get(pk=pk)
#         except Passenger.DoesNotExist:
#             raise Http404
#
#     def get(self,request,pk):
#         passenger = self.get_object(pk)
#         serializer = PassengerSerializer(passenger)
#         return Response(serializer.data)
#
#     def put(self,request,pk):
#         passenger = self.get_object(pk)
#         serializer = PassengerSerializer(passenger,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk):
#         passenger = self.get_object(pk)
#         passenger.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

'''
mixins
'''

# class PassengerListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Passenger.objects.all()
#     serializer_class = PassengerSerializer
#
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
# class  PassengerDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Passenger.objects.all()
#     serializer_class = PassengerSerializer
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)

'''
generics
'''
# class PassengerListView(generics.ListCreateAPIView):
#     queryset = Passenger.objects.all()
#     serializer_class = PassengerSerializer
#
# class PassengerDetailView(generics.RetrieveUpdateDestroyAPIView):
#       queryset = Passenger.objects.all()
#       serializer_class = PassengerSerializer

'''
viewset
'''
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
