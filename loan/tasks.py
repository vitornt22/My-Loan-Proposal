from loan.models import Loan
import logging
from celery import shared_task

logger = logging.getLogger(__name__)



@shared_task
def add_to_queue(loan_pk):
    logger.info(f"Iniciando tarefa compartilhada... {loan_pk}")

    try:
        loan= Loan.objects.get(id=loan_pk)
        status= 'approved' if loan_pk%2==0 else 'denied'
        loan.status= status
        loan.save()
    except:
        return f'Não foi possivel adicionar {loan_pk}'        

    return 'Objeto JSON adicionado à fila RabbitMQ com sucesso!'

