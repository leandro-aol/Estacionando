from django.forms import ModelForm
from .models import (
    Pessoa,
    Veiculo,
    MovimentoRotativo,
    Mensalista,
    MovimentoMensalista,
)


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

class MovimentoRotativoForm(ModelForm):
    class Meta:
        model = MovimentoRotativo
        fields = '__all__'

class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'

class MovimentoMensalistaForm(ModelForm):
    class Meta:
        model = MovimentoMensalista
        fields = '__all__'
