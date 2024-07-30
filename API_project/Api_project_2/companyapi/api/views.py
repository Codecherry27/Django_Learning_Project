from django.shortcuts import render
from rest_framework import viewsets
from .models import company,employee
from api.serializers import companyserializer,employeeserializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class companyviewset(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = companyserializer
    

    #companies/{companyid}/employees
    
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        print("Get employees of ",pk," company")
        Company = company.objects.get(pk=pk)
        emps = employee.objects.filter(Company=Company)
        emps_serilizer = employeeserializer(emps,many=True,context={'request':request})
        
        return Response(emps_serilizer.data)


class employeeviewset(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeserializer