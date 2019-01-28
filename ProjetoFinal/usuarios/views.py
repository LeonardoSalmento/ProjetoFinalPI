from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.contrib.auth.models import User
from perfis.models import Perfil
from timeline.models import *
from usuarios.forms import *
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db import transaction




class LoginView(View):
	template_name = 'login.html'

	def get(self, request):
		return render (request, self.template_name)
	@transaction.atomic
	def post(self, request):
		form = LoginForm (request.POST)
		if form.is_valid():
			user = authenticate(username=request.POST['username'],
                           password=request.POST["password"])
		
		if user is not None:
			login(request, user)
			return redirect('index')

		return render(request, self.template_name, {'form':form})


class RegistrarUsuarioView(View):
	template_name = 'registrar.html'

	def get(self, request):
		return render (request, self.template_name)
	@transaction.atomic
	def post(self, request):
		form = RegistrarUsuarioForm (request.POST)
		if form.is_valid ():
			dados_form = form.cleaned_data
			usuario = User.objects.create_user (username = dados_form['nome'], email = dados_form['email'], password = dados_form['senha'])
			perfil = Perfil(nome=dados_form['nome'], telefone = dados_form['telefone'], nome_empresa = dados_form['nome_empresa'], usuario = usuario)
			perfil.save()
			timeline = Timeline(perfil = perfil)
			timeline.save()
			return redirect('index')

		return render(request, self.template_name, {'form':form})

class RedefinirSenhaView(View):
	template_name = 'form_redefinir_senha.html'

	def get(self, request):
		form = RedefinirSenhaForm()
		return render(request, self.template_name, {'form': form})
	@transaction.atomic
	def post(self, request):
		form = RedefinirSenhaForm(request.POST)
		usuario_logado = User.objects.get(id=request.user.id)
		if form.is_valid():
			dados_form = form.cleaned_data
			if usuario_logado.check_password(dados_form['senha_atual']):
				if dados_form['nova_senha'] == dados_form['confirmacao_nova_senha']:
					usuario_logado.set_password(dados_form['nova_senha'])
					usuario_logado.save()
					return redirect('index')
		
		return render(request, self.template_name, {'form':form})

