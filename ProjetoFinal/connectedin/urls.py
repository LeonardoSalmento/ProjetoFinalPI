"""connectedin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from perfis import views 
from usuarios.views import *
from django.contrib.auth import views as v
from rest_framework.authtoken.views import obtain_auth_token

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('perfil/<int:perfil_id>', views.exibir_perfil, name='exibir'),
    path('perfil/', views.PerfilView.as_view(), name='meu_perfil'),
    path('perfil/<int:perfil_id>/convidar', views.convidar, name='convidar'),
    path('perfil/<int:perfil_id>/desfazer', views.desfazer, name='desfazer'),
    path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar'),
    path('convite/<int:convite_id>/recusar', views.recusar, name='recusar'),
    path('perfil/redefinir_senha',RedefinirSenhaView.as_view(), name='form_redefinir_senha'),
    path('perfil/desativar_conta',views.desativar_conta, name='desativar_conta'),
    path('perfil/ativar_conta',views.ativar_conta, name='ativar_conta'),
    path('perfil/desativar', views.DesativarContaView.as_view(), name='desativar'),
    path('perfil/ativar', views.AtivarContaView.as_view(), name='ativar'),
    path('registrar/', RegistrarUsuarioView.as_view(), name="registrar"),
    path('perfil/alterar_foto', views.alterar_foto_perfil, name='alterar_foto_perfil'),
    path('postagem/<int:post_id>/curtir', views.curtir, name='curtir'),
    path('postagem/<int:post_id>/descurtir', views.descurtir, name='descurtir'),
    path('comentar_postagem/<int:post_id>', views.comentar_postagem, name='comentar_postagem'),
    path('comentar/<int:post_id>', views.ComentarioView.as_view(), name='comentar'),
    path('login/', v.LoginView.as_view(), name="login"),
    path('logout/', v.LogoutView.as_view(template_name = 'login.html'), name="logout"),
    path('perfil/<int:perfil_id>/super', views.setarSuperUsuario, name='super'),
    path('perfil/<int:perfil_id>/bloquear', views.bloquear, name='bloquear'),
    path('perfil/<int:bloqueio_id>/desbloquear', views.desbloquear, name='desbloquear'),
    path('perfil/postar', views.PostarView.as_view(), name='postar'),
    path('postagem/<int:postagem_id>/excluir', views.deletar_postagem, name='excluir_postagem'),
    path('perfil/pesquisar', views.PesquisarPerfilView.as_view(), name='pesquisar'),
    path('password_reset/', v.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', v.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', v.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', v.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('api-token-auth/', obtain_auth_token),
    path('api-token-auth2/', views.CustomAuthToken.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

