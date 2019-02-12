from django.forms import ModelForm
from perfis.models import *
from django.db import models
from django import forms

class PostForm(forms.Form):
	texto = forms.CharField(required=True)
	imagem_postagem = forms.FileField(required=False)


class ComentarioForm(forms.Form):
	texto = forms.CharField(required=True)


class UploadFotoPerfilForm(forms.Form):
	foto_perfil = forms.FileField(required=False)


class PesquisaUsuarioForm(forms.Form):
	nome = forms.CharField(required=True)
		

class DesativarContaForm(forms.Form):
	justificativa = forms.CharField(required=True)


class AtivarContaForm(forms.Form):
	nome = forms.CharField(required=True)
	password = forms.CharField(required=True)


	def is_valid(self):
		valid = True
		if not super(AtivarContaForm, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		user_exists = User.objects.filter(username=self.cleaned_data['nome']).exists()
		if not user_exists:
			self.adiciona_erro('Nome de usuário não existe')
			valid = False
		
		else:
			usuario = User.objects.get(username=self.cleaned_data['nome'])
			if not usuario.check_password(self.cleaned_data['password']):
				self.adiciona_erro('Usuario ou senha incorreto')
				valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)