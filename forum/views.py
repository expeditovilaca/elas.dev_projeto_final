from django.shortcuts import render, get_object_or_404, redirect
from .models import Postagem, Comentario

def forum_lista(request):
    postagens = Postagem.objects.all().order_by('-id')  
    return render(request, 'forum/forum_lista.html', {'postagens': postagens})

def criar_postagem(request):
    """Nova view para processar a criacao de uma postagem enviada pelo usuario"""
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        nome_autor = request.POST.get('nome_autor')
        eixo = request.POST.get('eixo')
        conteudo = request.POST.get('conteudo')
        
        if titulo and conteudo:
            Postagem.objects.create(
                titulo=titulo,
                nome_autor=nome_autor or 'Anônimo',
                eixo=eixo or 'Geral',
                conteudo=conteudo
            )
            return redirect('forum_lista')

    return render(request, 'forum/criar_postagem.html')

def forum_detalhe(request, pk):
    postagem = get_object_or_404(Postagem, pk=pk)
    
    if request.method == 'POST':
        nome = request.POST.get('nome_autor')
        texto = request.POST.get('texto')
        if nome and texto:
            Comentario.objects.create(postagem=postagem, nome_autor=nome, texto=texto)
            return redirect('forum_detalhe', pk=postagem.pk)

    return render(request, 'forum/forum_detalhe.html', {'postagem': postagem})