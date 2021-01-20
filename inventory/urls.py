from django.urls import path


from inventory.views import (
    StoreCreateAndListView,
    StoreRetrieveUpdateDestroyView,
    DepartmentCreateAndListView,
    DepartmentRetrieveUpdateDestroyView,
    CategoryCreateAndListView,
    CategoryRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("stores/", StoreCreateAndListView.as_view()),
    path("store/<int:pk>/", StoreRetrieveUpdateDestroyView.as_view()),
    path("departments/", DepartmentCreateAndListView.as_view()),
    path("department/<int:pk>/", DepartmentRetrieveUpdateDestroyView.as_view()),
    path("categories/", CategoryCreateAndListView.as_view()),
    path("category/<int:pk>/", CategoryRetrieveUpdateDestroyView.as_view()),
]
