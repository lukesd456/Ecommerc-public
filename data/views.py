from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)

product_list_create = ProductListCreateView.as_view()

class ProductDetailView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='uniqueID'

product_detail_view=ProductDetailView.as_view()