from rest_framework import serializers
from django.core.exceptions import ValidationError


from .models import Loan, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Loan
        fields = ['id', 'address', 'name', 'cpf', 'value', 'email']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address_serializer = self.fields['address']
        address = address_serializer.create(address_data)

        loan = Loan.objects.create(address=address, **validated_data)
        return loan
        

    def validate_email(self, value):
        if not value:
            raise ValidationError("O campo de email não pode estar vazio.")
        return value

    def validate_cpf(self, value):
        if  len(value) != 14:
            raise ValidationError("CPF inválido.")
        return value

    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return value

    def validate_value(self, value):
        if value <= 0:
            raise ValidationError("O valor deve ser maior que zero.")
        return value

    
