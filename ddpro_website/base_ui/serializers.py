from rest_framework import serializers
from .models import Article


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'heading',
            'text_html',
        ]


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'first_name',
            'last_name',
            'image',
            'priority',
            'roles'
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'image',
            'short_description',
        ]