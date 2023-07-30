from rest_framework import generics, permissions
from .serializers import ProductSerializer
from .models import Product


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.order_by("-created_at")
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated, )
