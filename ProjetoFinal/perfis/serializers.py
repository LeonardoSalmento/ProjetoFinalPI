from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.db import transaction

class PostagemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Postagem
        fields = ('dono','texto','imagem_postagem','data_publicacao')