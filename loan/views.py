from rest_framework.viewsets import ModelViewSet

from .models import Loan
from .serializers import LoanSerializer
from .tasks import add_to_queue




class LoanApiView(ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Adicionar tarefa na fila rabbitMQ 
        add_to_queue.delay(response.data['id'])       
        return response