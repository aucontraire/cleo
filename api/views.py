from api.serializers import CompanySerializer, FamilySerializer, GuideSerializer, UserSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from service.models import Company, Family, Guide, User


class CompanyList(APIView):
    """
    List all companies, or create a new company.
    """
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    """
    Retrieve, update or delete a company instance.
    """
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FamilyList(APIView):
    """
    List all families, or create a new family.
    """
    def get(self, request, format=None):
        families = Family.objects.all()
        serializer = FamilySerializer(families, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FamilyDetail(APIView):
    """
    Retrieve, update or delete a family instance.
    """
    def get_object(self, pk):
        try:
            return Family.objects.get(pk=pk)
        except Family.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        family = self.get_object(pk)
        serializer = FamilySerializer(family)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        family = self.get_object(pk)
        serializer = FamilySerializer(family, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        family = self.get_object(pk)
        family.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GuideList(APIView):
    """
    List all guides, or create a new guide.
    """
    def get(self, request, format=None):
        guides = Guide.objects.all()
        serializer = GuideSerializer(guides, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GuideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuideDetail(APIView):
    """
    Retrieve, update or delete a guide instance.
    """
    def get_object(self, pk):
        try:
            return Guide.objects.get(pk=pk)
        except Guide.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        guide = self.get_object(pk)
        serializer = GuideSerializer(guide)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        guide = self.get_object(pk)
        serializer = GuideSerializer(guide, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        guide = self.get_object(pk)
        guide.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def activate(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404

    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        if not request.data.get('activation_code') or not request.data.get('password'):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if user.activation_code != request.data.get('activation_code'):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if len(user.password) != 0:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        user.set_password(request.data['password'])
        user.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
