from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import  APIView
from django.http import Http404

class OrderListView(APIView):

    def get(self,request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class  OrderDetailView(APIView):
    def get_object(self,pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        orders = self.get_object(pk)
        serializer = OrderSerializer(orders)
        return Response(serializer.data)

    def put(self,request,pk):
        orders = self.get_object(pk)
        serializer = OrderSerializer(orders,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        orders = self.get_object(pk)
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerListView(APIView):

     def get(self,request):
         customer = Customer.objects.all()
         serializer = CustomerSerializer(customer,many=True)
         return Response(serializer.data)

     def post(self,request):
         serializer = CustomerSerializer(data = request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class  CustomerDetailView(APIView):

     def get_object(self,pk):
         try:
             return Customer.objects.get(pk=pk)
         except Customer.DoesNotExist:
             raise Http404

     def get(self,request,pk):
         customer = self.get_object(pk)
         serializer = CustomerSerializer(customer)
         return Response(serializer.data)

     def put(self,request,pk):
         customer = self.get_object(pk)
         serializer = CustomerSerializer(customer,data = request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

     def delete(self,request,pk):
         customer = self.get_object(pk)
         customer.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
