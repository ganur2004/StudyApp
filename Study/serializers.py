from rest_framework import serializers
from .models import Product, Lesson

class ProductSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_num_lessons(self, obj):
        return obj.lesson_set.count()

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

