from django.db import models
import datetime
from django.utils import timezone
now = timezone.now()
from django.core.validators import MinValueValidator,MinLengthValidator
import re
ESPECIALIDADES = [
    ("CA","CARDIOLOGIA"),
    ("UR","UROLOGIA"),
    ("NEU","NEUROLOGIA"),
]
STATUS = {
    ("AG", "agendado"),
    ("RE", "realizado"),
    ("CA", "cancelado") 
}
 
# Create your models here.
class Medico(models.Model):
    nome = models.CharField(max_length=50, validators=[MinLengthValidator(5,'o campo deve ter no minimo 5 caracteres')])
    especialidade = models.CharField(max_length=15,choices=ESPECIALIDADES)
    crm = models.CharField(unique=True,max_length=7)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome
class Consulta(models.Model):
    paciente = models.CharField(max_length=15)
    data = models.DateTimeField(validators=[MinValueValidator(now)])
    medico = models.ForeignKey(Medico,on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS, blank=False,null=False)
