# django
from django.contrib import admin

# current app
from .forms import LoanForm
from .models import Loan
from .tasks import add_to_queue


# Register your models here.
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'get_status_display')
    form= LoanForm

    def get_status_display(self, obj):
        return obj.get_status_display()


    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        add_to_queue.delay(obj.id)