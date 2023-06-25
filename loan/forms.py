from django import forms
from loan.models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        if len(cpf)<14:
            raise forms.ValidationError("O campo1 não pode ser maior que o campo2.")

        return cpf
       
