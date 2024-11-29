
from django.http import HttpResponse
from . import models

from . import serializers
from rest_framework import generics

# Create your views here.

class getProductsList(generics.ListCreateAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer

class getProduct(generics.RetrieveAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    lookup_field = 'productcode' # this is the field that will be used to filter the data



# def get_all_products(request):
#     products = models.Products.objects.all() # this is a selection query
#     return HttpResponse(products)



# def get_product_by_productCode(request, productCode):
#     product = models.Products.objects.get(productcode = productCode) # this is a selection query
#     # product = get_object_or_404(models.Products, productCode='S10_1678') # the same as above
#     return HttpResponse(product.productdescription)


# def add_new_product(request, productCode, productName,  buyPrice):
#     product = models.Products(productcode = productCode, 
#                               productname= productName, 
#                               productline='Not defiled', 
#                               productscale='000', 
#                               productvendor='Not defined', 
#                               productdescription='Not defined', 
#                               quantityinstock=0, 
#                               buyprice = buyPrice, 
#                               msrp = 0)
#     product.save() # this is an insertion query
#     return HttpResponse("Product added successfully")