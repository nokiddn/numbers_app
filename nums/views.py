from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
import tensorflow as tf


from .models import model2

def index(request):
    info = model2.objects.filter(default = True)
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
    test_labels = test_labels[:1000] 
    test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0
    model1 = tf.contrib.saved_model.load_keras_model(info.values('model_path')[0]['model_path'])
    model1.compile(
            optimizer = tf.train.AdamOptimizer(),
            loss = 'sparse_categorical_crossentropy',
            metrics = ['accuracy'])   
    test_loss, test_acc = model1.evaluate(test_images, test_labels)
    name = info.values('name')[0]['name']
    return render(request, 'nums/frontpage.html', { 'name': name, "accuracy": test_acc })

def viewmodel(request, modelno):
    cur_model = get_object_or_404(model2, pk = modelno)
    return render(request, 'nums/index.html', { 'model': cur_model })

def allmodels(request):
    models = model2.objects.all()
    return render(request, 'nums/allmodels.html', { 'models': models })

def predict(request):
    cur_model = model2.objects.filter(default = True)
    return render(request, 'nums/predict.html', { 'model': cur_model })
    

# Create your views here.
