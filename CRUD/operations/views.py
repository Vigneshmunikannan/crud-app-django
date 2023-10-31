from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer  # Assuming your serializer is named StudentSerializer



class StudentDetails(APIView):
    # Read Data of student 
    # if id is provided show single data else it will show all data
    def get(self,request,pk=None):
        if pk is None:
            students=Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
        else:
            try:
                student=Student.objects.get(pk=pk)
                serializer=StudentSerializer(student)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({"msg":"Student id not found"},status=status.HTTP_404_NOT_FOUND)


    # Creating new student 
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete product with pk id
    def delete(self, request, pk):
        try:
            student= Student.objects.get(pk=pk)
            student.delete()
            return Response({"msg":"deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"msg":"Student id not found"},status=status.HTTP_404_NOT_FOUND)
         
    # Update data using pk
    def put(self, request, pk):
        try:
            product = Student.objects.get(pk=pk)
            serializer = StudentSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"updated successfully","data":serializer.data},status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({"msg":"Student id not found"},status=status.HTTP_404_NOT_FOUND)

