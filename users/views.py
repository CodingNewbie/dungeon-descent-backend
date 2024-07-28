from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView

class StatesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data=self.request.user.states, status=status.HTTP_200_OK)

    def post(self, request):
        self.request.user.states=request.data
        self.request.user.save()
        return Response(status=status.HTTP_200_OK)
