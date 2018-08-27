from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    Veiculo,
    MovimentoRotativo,
    Mensalista,
    MovimentoMensalista,
)

from .form import (
    PessoaForm,
    VeiculoForm,
    MovimentoRotativoForm,
    MensalistaForm,
    MovimentoMensalistaForm,
)

# Create your views here.
def home(request):
    context = {'mensagem' : 'Olá Mundo!'}
    return render(request, 'core/index.html', context)

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    dados = {'pessoas' : pessoas, 'form' : form}
    return render(request, 'core/lista_pessoas.html', dados)

def nova_pessoa(request):
    form = PessoaForm(request.POST or None)
    
    if form.is_valid():
        form.save()

    return redirect('core_lista_pessoas')

def update_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    dados = {'pessoa' : pessoa, 'form' : form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', dados)

def delete_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'objeto' : pessoa})

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    dados = {'veiculos' : veiculos, 'form' : form}
    return render(request, 'core/lista_veiculos.html', dados)

def novo_veiculo(request):
    form = VeiculoForm(request.POST or None)
    
    if form.is_valid():
        form.save()

    return redirect('core_lista_veiculos')

def update_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    dados = {'veiculo' : veiculo, 'form' : form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', dados)

def delete_veiculo(request, id):
    veiculo = Veiculo.objects.get(id=id)

    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'objeto' : veiculo})

def lista_movRotativos(request):
    movRotativo = MovimentoRotativo.objects.all()
    form = MovimentoRotativoForm()
    dados = {'movRotativo' : movRotativo, 'form' : form}
    return render(request,'core/lista_movRotativos.html', dados)

def novo_movRotativo(request):
    form = MovimentoRotativoForm(request.POST or None)
    
    if form.is_valid():
        form.save()

    return redirect('core_lista_movRotativos')

def update_movRotativo(request, id):
    movRotativo = MovimentoRotativo.objects.get(id=id)
    form = MovimentoRotativoForm(request.POST or None, instance=movRotativo)
    dados = {'movRotativo' : movRotativo, 'form' : form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movRotativos')
    else:
        return render(request, 'core/update_movRotativo.html', dados)

def delete_movRotativo(request, id):
    movRotativo = MovimentoRotativo.objects.get(id=id)

    if request.method == 'POST':
        movRotativo.delete()
        return redirect('core_lista_movRotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'objeto' : movRotativo})

def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    dados = {'mensalistas' : mensalistas, 'form' : form}
    return render(request, 'core/lista_mensalistas.html', dados)

def novo_mensalista(request):
    form = MensalistaForm(request.POST or None)
    
    if form.is_valid():
        form.save()

    return redirect('core_lista_mensalistas')
    
def update_mensalista(request, id):
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    dados = {'mensalista' : mensalista, 'form' : form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', dados)

def delete_mensalista(request, id):
    mensalista = Mensalista.objects.get(id=id)

    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', {'objeto' : mensalista})

def lista_movMensalista(request):
    movMensalista = MovimentoMensalista.objects.all()
    form = MovimentoMensalistaForm()
    dados = {'movMensalista' : movMensalista, 'form' : form}
    return render(request,'core/lista_movMensalista.html', dados)

def novo_movMensalista(request):
    form = MovimentoMensalistaForm(request.POST or None)
    
    if form.is_valid():
        form.save()

    return redirect('core_lista_movMensalista')

def update_movMensalista(request, id):
    movMensalista = MovimentoMensalista.objects.get(id=id)
    form = MovimentoMensalistaForm(request.POST or None, instance=movMensalista)
    dados = {'movMensalista' : movMensalista, 'form' : form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movMensalista')
    else:
        return render(request, 'core/update_movMensalista.html', dados)

def delete_movMensalista(request, id):
    movMensalista = MovimentoMensalista.objects.get(id=id)

    if request.method == 'POST':
        movMensalista.delete()
        return redirect('core_lista_movMensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'objeto' : movMensalista})
