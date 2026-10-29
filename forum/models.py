from django.db import models

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    nome_autor = models.CharField(max_length=100, default='Anônimo')
    eixo = models.CharField(max_length=100, default='Geral')
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True) # <--- Adicionado aqui também!

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='comentarios')
    nome_autor = models.CharField(max_length=100)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.nome_autor} - {self.postagem.titulo}"