from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Address(models.Model):
    '''
        Modelo para endereço do cliente
    '''
    street = models.CharField(max_length=100, verbose_name='Rua')
    city = models.CharField(max_length=100, verbose_name='Cidade')
    state = models.CharField(max_length=50, verbose_name='Estado')
    postal_code = models.CharField(max_length=20, verbose_name='CEP')

    class Meta:
        verbose_name = _('Endereço')

    def __str__(self):
        return f'{self.id}: {self.street}, {self.city}, {self.state} {self.postal_code}'


class Loan(models.Model):
    '''
        Modelo da proposta de empréstimo
    '''

    STATUS_CHOICES = (
        ('approved', 'Aprovado'),
        ('denied', 'Negado'),
        ('pending', 'Pendente'),
    )

    name = models.CharField(max_length=100, verbose_name='Nome do Cliente')
    email = models.EmailField(verbose_name='Email do Cliente')
    cpf = models.CharField(max_length=14, verbose_name='CPF do Cliente')
    value = models.FloatField(verbose_name='Valor da proposta de empréstimo')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Endereço', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Status da Proposta',default="pending", blank=True)

    class Meta:
        verbose_name = _('Proposta de Empréstimo')

    def __str__(self) -> str:
        return f'{self.id} - {self.name}, valor: {self.value}'
