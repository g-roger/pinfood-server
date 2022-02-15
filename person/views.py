from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from person.models import Person
from person.serializers import PersonSerializer


class PersonViewSet(APIView):
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        password = request.data.pop('password')

        if serializer.is_valid():
            person_database = Person.objects.filter(email=request.data['email']).exists()

            if person_database:
                return Response({'message': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

            # Create User when generate person
            user = User.objects.create_user(username=request.data['email'],
                                            email=request.data['email'],
                                            password=password,
                                            first_name=request.data['first_name'],
                                            last_name=request.data['last_name'])
            serializer.save()

            # returns token when login
            token = str(RefreshToken.for_user(user).access_token)
            refresh_token = str(RefreshToken.for_user(user))
            return Response(data={'user': serializer.data,
                                  'token': token,
                                  'refresh_token': refresh_token}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        if request.user.pk != pk:
            return Response({'message': 'You cannot access an user different of yours'},
                            status=status.HTTP_401_UNAUTHORIZED)
        try:
            person = Person.objects.get(pk=pk)
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        except Person.DoesNotExist:
            raise Http404
