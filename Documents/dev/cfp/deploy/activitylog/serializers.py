from rest_framework import serializers
from. models import Logbook

class LogbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logbook
        fields = ['id','user','action','description','timestamp']