from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializer import EmployeeSerial
from .models import Employee

class EmployeeViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = EmployeeSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        employees = Employee.objects.all()
        serialzer = EmployeeSerial(employees, many=True)
        return Response(data=serialzer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerial(employee)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerial(data=request.data, instance=employee)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerial(data=request.data, instance=employee, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)
