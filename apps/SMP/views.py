from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # var1=Mymodel.objects.all()
    var1 = [1, 2, 3, 4]
    # templates\pages\social_media\index.html
    template_name='../../assets/templates/pages/social_media/index.html'
    context={'var1':var1}
    return render(request, template_name, context)