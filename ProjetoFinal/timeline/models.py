from django.db import models
from perfis.models import *


class Timeline(models.Model):
    
    perfil = models.OneToOneField(Perfil, related_name = "minha_timeline", on_delete = models.CASCADE)

    def get_timeline(self):
        lista_postagens = []
        postagens_ordenadas = Postagem.objects.all()[::-1]

        for i in postagens_ordenadas:
            if i.dono in self.perfil.contatos.all() or i.dono.id == self.perfil.id:
                lista_postagens.append(i)
        
        return lista_postagens


