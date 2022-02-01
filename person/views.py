from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from person.models import Person
from person.serializers import PersonSerializer


class PersonViewSet(APIView):
    def post(self, request):
        serializer = PersonSerializer(data=request.data)

        if serializer.is_valid():
            person_database = Person.objects.filter(email=request.data['email']).exists()

            if person_database:
                return Response({'message': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetail(APIView):
    def get(self, request, pk):
        try:
            person = Person.objects.get(pk=pk)
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        except Person.DoesNotExist:
            raise Http404
