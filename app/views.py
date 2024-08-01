from typing import Any
from django.views.generic import TemplateView
from .models import Servico, Disruptivo

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['disruptivos'] = Disruptivo.objects.order_by('?').all()
        return context
        

