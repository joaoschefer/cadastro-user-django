from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, "usuarios/home.html")

def usuarios(request):
    if request.method == "POST":
        # salvar os dados da tela para o banco de dados
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get("nome")
        novo_usuario.idade = request.POST.get("idade")
        novo_usuario.save()
        # redirecionar para a página de listagem de usuários
        return redirect('lista_users')
    else:
        # exibir todos os usuarios já cadastrados em uma página
        usuarios = {
            "usuarios": Usuario.objects.all()
        }
        # retornar os dados para a pagina de listagem de usuarios
        return render(request, "usuarios/usuarios.html", usuarios)
        
