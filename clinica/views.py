from django.shortcuts import render,redirect, get_object_or_404
from .models import Medico,Consulta
from .forms import MedicoForm,ConsultaForm
# Create your views here.
def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta')
    else:
        form = ConsultaForm()
    return render(request, 'form_consulta.html', {'form': form})
def listar_medicos(request):
    if request.method == 'POST':
        medicos = MedicoForm(request.POST)
        return render(request, 'listar_medicos.html',{'medicos': medicos })
    medicos  = Medico.objects.all()
    return render(request, 'listar_medicos.html',{'medicos': medicos })
def detalhes_consulta(request,pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        consulta= ConsultaForm(request.POST)
        return render(request, 'buscar_consulta.html',{'consulta': consulta })
    consulta  = Consulta.objects.all()
    return render(request, 'buscar_consulta.html', {'consulta': consulta})
