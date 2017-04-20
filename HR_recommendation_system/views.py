from django.shortcuts import render
from django.http import HttpResponse
from .models import postgres
from .recommendation import buildModel
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

def index(request):
	return render(request, "index.html")

def home(request):
	return render(request, "home.html")

def recs(request):
	return render(request, "recs.html")


@ensure_csrf_cookie
@api_view(['POST'])
def login(request):
	if request.method == 'POST':
		database = postgres()
		user = database.login(request.data)
		return Response(user)

	else:
		return Response(status.HTTP_400_BAD_REQUEST)

@ensure_csrf_cookie
@api_view(['POST'])
def register(request):
	if request.method == 'POST':
		database = postgres()
		user = database.register(request.data)
		return Response(user)

	else:
		return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getChallenges(request):
	if request.method == 'GET':
		database = postgres()
		posts = database.getChallenges()
		return Response(posts)

	else:
		return Response(status.HTTP_400_BAD_REQUEST)

	
@ensure_csrf_cookie
@api_view(['POST'])
def getAllRecs(request):
	if request.method == 'POST':
		database = postgres()
		user = database.getAllRecs(request.data)
		return Response(user)

	else:
		return Response(status.HTTP_400_BAD_REQUEST)

@ensure_csrf_cookie
@api_view(['POST'])
def processSubmisson(request):
	if request.method == 'POST':
		model = buildModel()
		user = model.naiveBayes(request.data)
		return Response(user)

	else:
		return Response(status.HTTP_400_BAD_REQUEST)
		