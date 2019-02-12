from django import forms
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):
	nome = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	senha = forms.CharField(required=True)
	telefone = forms.CharField(required=True)
	nome_empresa = forms.CharField(required=True)

	def is_valid(self):
		valid = True

		if not super(RegistrarUsuarioForm, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		user_exists = User.objects.filter(username=self.cleaned_data['nome']).exists()
		if user_exists:
			self.adiciona_erro('Nome de usuário já cadastrado')
			valid = False

		user_exists = User.objects.filter(username=self.cleaned_data['email']).exists()
		if user_exists:
			self.adiciona_erro('Email já cadastrado')
			valid = False


		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)

class RedefinirSenhaForm(forms.Form):
	senha_atual = forms.CharField(required=True)
	nova_senha = forms.CharField(required=True)
	confirmacao_nova_senha = forms.CharField(required=True)

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)

	
class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	senha = forms.CharField(required=True)


	def is_valid(self):
		valid = True


		if not super(LoginForm, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		lista_usuarios = User.objects.filter(username=self.cleaned_data['username'])
		usuario = lista_usuarios[0]
		if not usuario.is_active:
			self.adiciona_erro('Conta desativada, justificativa: " ' + usuario.perfil.justificativa + '"')
			valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)