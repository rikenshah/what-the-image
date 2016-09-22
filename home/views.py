from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from utilities import imClassify
from utilities import duckduckGo
from django.http import HttpResponse
from forms import ImageUploadForm
from models import ExampleModel
import os

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")

@login_required(login_url="/login/")
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        imageName = str(request.FILES['image'])
        print "Hello this is :"+imageName
        # print request.POST
        if form.is_valid():
            m = ExampleModel()
            m.model_pic = form.cleaned_data['image']
            m.save()

            im = imClassify.imClassify()
            imagePath = 'utilities/images/'+imageName
            resultList = im.main(imagePath)
            print  "THi is view ;;;;;; ------ ;;;;"
            print resultList

            # Considering only the first string
            # [['giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca', 0.89233041], ['indri, indris, Indri indri, Indri brevicaudatus', 0.0085870409], ['lesser panda, red panda, panda, bear cat, cat bear, Ailurus fulgens', 0.0026423461], ['custard apple', 0.0014067066], ['earthstar', 0.0010706335]]
            nameOfTopic = resultList[0][0].split(",")[0]
            print nameOfTopic

            du = duckduckGo.duckduckGo()
            description = du.getInfo(nameOfTopic)

            print description

            # Now deleting the file
            if os.path.isfile(imagePath):
                os.remove(imagePath)

            return render(request,'result.html',{'imageName':nameOfTopic, 'description':description})
    return HttpResponseForbidden('allowed only via POST')

