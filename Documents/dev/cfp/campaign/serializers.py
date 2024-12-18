from rest_framework import serializers

from . models import Campaign,Category,CampaignPage

class CategogrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['title','description','goal_amount','category_type','image','video']

class CreateCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['title','description','goal_amount','start_date','deadline'] 


class CampaignPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignPage
        fields = ['user_id','campaign','viewed_at']


