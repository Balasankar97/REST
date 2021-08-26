from .models import Courses
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import  APIView
from django.http import Http404
from rest_framework import  generics, mixins, viewsets

'''
Class Based views
'''
# class CoursesListView(APIView):
#
#     def get(self,request):
#         courses = Courses.objects.all()
#         serializer = CourseSerializer(courses,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer = CourseSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
#
#
# class  CoursesDetailView(APIView):
#     def get_object(self,pk):
#         try:
#             return Courses.objects.get(pk=pk)
#         except Courses.DoesNotExist:
#             raise Http404
#
#     def get(self,request,pk):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)
#
#     def put(self,request,pk):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk):
#         course = self.get_object(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

'''
mixins
'''
# class CoursesListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CourseSerializer
#
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
# class  CoursesDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CourseSerializer
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
# class CoursesListView(generics.ListCreateAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CourseSerializer
#
# class CoursesDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CourseSerializer

'''
viewsets
'''
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
