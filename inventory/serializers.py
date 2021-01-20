from rest_framework import serializers

from inventory.models import Store, Department


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            "id",
            "name",
            "street",
            "number",
            "neighborhood",
            "country",
            "state",
            "zipcode",
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(
        source="department", queryset=Department.objects.all()
    )

    class Meta:
        model = Department
        fields = ["id", "description", "department_id"]
