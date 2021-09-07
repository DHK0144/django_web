from .models import *
from rest_framework import serializers


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        music = Music.objects.all()
        model = Music
        fields = '__all__'  # __all__ 을 줄 경우, 모든 필드가 사용됨.
        # fields = ('id', 'created_at', 'title', 'category', 'star_rating',)  # req, res 시 사용되길 원하는 필드(컬럼)만 적어줘도 됨.
