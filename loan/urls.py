from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import LoanApiView
from django.views.generic import TemplateView

import os

router = SimpleRouter()
router.register('loan', LoanApiView, basename='Loan')

urlpatterns = []

    
urlpatterns += router.urls