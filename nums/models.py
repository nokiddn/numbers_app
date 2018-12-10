from django.db import models
from django.contrib.postgres.fields import JSONField

def default_activations():
    return ['softmax']

def default_units():
    return ['10']

# Create your models here.
class model1(models.Model):
    #time_estimated = models.DateTimeField(auto_now_add=True)
    accuracy = models.FloatField(default=0)
    name = models.CharField(max_length=200, default = 'test')
    def __str__(self):
        return self.name

class model2(models.Model):
    time_estimated = models.DateTimeField(auto_now_add = True)
    accuracy = models.FloatField(default = 0)
    name = models.TextField(default = '')
    default = models.BooleanField(default = True)
    number_of_layers = models.IntegerField(default = 1)
    unit_numbers_in_layers = JSONField(default = default_units)
    activations = JSONField(default = default_activations)
    dropout_prob = models.FloatField(default = 0)
    model_path = models.TextField(default = '/var/www/models/')
    def __str__(self):
        return self.name
