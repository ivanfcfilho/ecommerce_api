from rest_framework import generics, permissions


from inventory.models import Store, Department, Category
from inventory.serializers import (
    StoreSerializer,
    DepartmentSerializer,
    CategorySerializer,
)


class StoreCreateAndListView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    permission_classes = permission_classes = [permissions.IsAuthenticated]
    serializer_class = StoreSerializer


class StoreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    permission_classes = permission_classes = [permissions.IsAuthenticated]
    serializer_class = StoreSerializer


class DepartmentCreateAndListView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    permission_classes = permission_classes = [permissions.IsAuthenticated]
    serializer_class = DepartmentSerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer


class CategoryCreateAndListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer


class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    permission_classes = permission_classes = [permissions.IsAuthenticated]
    serializer_class = DepartmentSerializer
