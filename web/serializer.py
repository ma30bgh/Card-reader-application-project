from rest_framework import serializers
from web.models import register


class registerSerializer(serializers.ModelSerializer):

    class Meta:
        model = register
        # fields = '__all__'
        fields = ['name','family']