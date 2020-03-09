from rest_framework import serializers
from .models import About, TeamMember, Product


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = [
            'id',
            'heading',
            'text_html',
        ]


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
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
        model = Product
        fields = [
            'id',
            'title',
            'image',
            'short_description',
        ]