from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions

# Create your views here.
'''ModelViewSet class crate CRUD behind the scene without defining 
create(), get(), update() and delete() methods,'''
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    '''Add SessionAuthentication to this API, so that only authenticated user
    can access this API. user try to access API with user name & password.
    In SessionAuthentication credential is user name and password'''
    authentication_classes = [SessionAuthentication] 
    # Gives all kinds of autheticated user permission to access API
    # permission_classes = [IsAuthenticated]

    '''Gives only admin user (whose staff status is True) permission 
    to access API'''
    # permission_classes = [IsAdminUser]

    # Gives all kinds of users permission to access API
    # permission_classes = [AllowAny]
    
    '''Allows autheticated users to perform any request, and allows 
    anonymous or unauthorized users to perform only read operation.'''
    # permission_classes = [IsAuthenticatedOrReadOnly]

    '''Autheticated user can read only. If a user is given specific access,
    (like post, put or delete access) it is done from admin site manually,
     then he can perform actions according to given access. '''  
    # permission_classes = [DjangoModelPermissions]

    '''Similar to DjangoModelPermissions, but also allows unautheticated
    users to have read-only access to the API.'''
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    '''Unautheticated users will not get any access to API, and autheticated user will get 
    read-only access. but superuser get all kinds of access.'''
    permission_classes = [DjangoObjectPermissions]
    
