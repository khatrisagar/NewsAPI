from rest_framework import serializers
from .models import NewsImage

class NewsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = (
            'image',
        )
        