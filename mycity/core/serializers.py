from rest_framework import serializers
from .models import Proposal

class ProposalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['id', 'title', 'description']

class ProposalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['title', 'description']

class ProposalSerializerJson(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['id', 'title', 'description', 'photo']
