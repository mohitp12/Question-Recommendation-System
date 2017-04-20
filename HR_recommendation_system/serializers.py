from rest_framework import serializers
from HR_recommendation_system.models import postgres



class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = postgres
      #  model = postgres.my_custom_sql()
     #   fields = ('', 'author', 'text', 'created', 'updated')

