from rest_framework import serializers
from editor import models


class SimpleSerializer(serializers.ModelSerializer):
    """
    Serializes a SimpleModel to be passed as a json file.
    """

    class Meta:
        model = models.SimpleModel
        fields = '__all__'
