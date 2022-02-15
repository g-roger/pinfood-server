import datetime

from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        #TODO: some implementations like the hour of establishment works will be implemented on the future
        products = Product.objects.filter(establishment__is_open=True,
                                          date_available__gte=datetime.datetime.now()).all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Person.DoesNotExist:
            raise Http404
