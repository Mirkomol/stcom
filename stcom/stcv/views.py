from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ProfileCV
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io



def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        work_experience= request.POST.get("work_experience","")
        skills = request.POST.get("skills","")


        profile = ProfileCV(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,work_experience=work_experience,skills=skills)
        profile.save()
        return redirect('list')
    return render(request, "stcv/accept.html")

@login_required
def cv(request, id):
    user_profile = ProfileCV.objects.get(pk=id)
    template = loader.get_template('stcv/cv.html')
    html = template.render({'user_profile': user_profile})
    options = {
        'page-size':'Letter',
        'encoding':"UTF-8",
        'enable-local-file-access': ''
    }


    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response

@login_required
def list(request):
    profile = ProfileCV.objects.all()
    return render(request,'stcv/list.html',{'profile':profile})




@login_required
def delete_cv(request,id):

    profile = ProfileCV.objects.get(id=id)


    if request.method == 'POST':
        profile.delete()
        return redirect('stcv')

    return render(request, 'stcv/cv_delete.html',{'profile':profile})

