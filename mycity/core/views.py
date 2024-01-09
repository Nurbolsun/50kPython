from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProposalListSerializer, ProposalCreateSerializer, ProposalSerializerJson
from .models import Proposal
from rest_framework.generics import RetrieveAPIView
# Create your views here.
class ProposalListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        proposals = Proposal.objects.all()
        proposal_json = ProposalListSerializer(proposals, many=True)
        return Response(data=proposal_json.data)
    
class ProposalCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = ProposalCreateSerializer(data=data)
        if serializer.is_valid():
            proposal = serializer.save()
            json_data = ProposalSerializerJson(instance=proposal)
            return Response(json_data.data, 201)
        return Response(data={'message': 'Data not valide', 'error': serializer.errors}, status=400)
    
class ProposalRetriAPIView(RetrieveAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializerJson