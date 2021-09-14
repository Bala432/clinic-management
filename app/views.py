from django.shortcuts import render
from app.models import Patient,Consult,SendEmail
from app.forms import PatientForm,ConsultForm,SendEmailForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse,reverse_lazy
from django.views.generic import (CreateView,ListView,DeleteView,UpdateView,DetailView)
from django.core.mail import send_mail
from clinic.settings import EMAIL_HOST_USER

def user_login(request):

    if request.method=="POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:

            login(request,user)
            return render(request,"login_page.html",{})

        else:

            return HttpResponse("Invalid Login Details")

    else:

        return render(request,"login.html",{})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required
def done(request):
    return render(request,'done.html',{})

@login_required
def add(request):
    return render(request,'add.html',{})


@login_required
def CreateRecordView(request):

    form = PatientForm()

    if request.method=="POST":

        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('done'))

        else:
            return HttpResponse("Invalid Form")

    else:

        return render(request,'patient_form.html',{'form':form})

'''class CreateRecordView(LoginRequiredMixin,CreateView):

    login_url = '/login_page/'
    redirect_field_name = 'app/login_page.html'

    form_class = PatientForm
    model = Patient'''

class PatientListView(LoginRequiredMixin,ListView):

    model = Patient
    context_object_name = "list"

    def get_queryset(self):
        return Patient.objects.all()

class PatientDetailView(LoginRequiredMixin,DetailView):

    model = Patient
    context_object_name = "detail"

    template_name = "patient_detail.html"

class PatientUpdateView(LoginRequiredMixin,UpdateView):

    fields = ('email','mobile','area','height','weight','bpi')
    model = Patient
    template_name_suffix = "_update_form"

@login_required
def index(request):
    return render(request,'name_list.html',{})

@login_required
def PatientNameListView(request):
    if request.method=="POST":

        new_name = request.POST.get('search')
        p=Patient.objects.filter(name__iexact=new_name)
        return render(request,"patient_name_list.html",{'p':p})

    else:
        return HttpResponse("No GET Data'")

class PatientNameDetailView(LoginRequiredMixin,DetailView):

    model = Patient
    context_object_name = "detail"
    template_name = "patient_detail.html"

@login_required
def complete(request):
    return render(request,"id_list.html",{})

@login_required
def PatientIDListView(request):
    if request.method=="POST":

        j=request.POST.get('i')
        p=Patient.objects.filter(uid__iexact=j)
        return render(request,"patient_id_list.html",{'p':p})

    else:
        return HttpResponse("NO GET Data")

class PatientIDDetailView(LoginRequiredMixin,DetailView):

    model = Patient
    context_object_name = "detail"
    template_name = "patient_detail.html"

@login_required
def home(request):
    return render(request,"problem_list.html",{})

def PatientProblemListView(request):

    if request.method=="POST":

        new_problem = request.POST.get('specify')
        p=Patient.objects.all()
        lt=[]
        for i in p:
            s=Consult.objects.filter(consult=i)
            for j in s:
                if j.problem==new_problem:
                    lt.append(i)
                    break
        return render(request,"patient_problem_list.html",{'p':lt})

    else:
        return HttpResponse("No GET Data")


class PatientProblemDetailView(LoginRequiredMixin,DetailView):

    model = Patient
    template_name = "patient_detail.html"
    context_object_name = "detail"

@login_required
def AddRecord(request,pk):

    form = ConsultForm()

    if request.method == "POST":
        form = ConsultForm(request.POST)
        new_form=form.save(commit=False)
        new_form.consult = Patient(uid=pk)
        new_form.save()
        return HttpResponseRedirect(reverse('done'))

    else:
        return render(request,"consult_form.html",{'form':form})


@login_required
def PatientEmailView(request,pk):

    form = SendEmailForm()

    if request.method == "POST":
        form = SendEmailForm(request.POST)
        sub = form['subject'].value()
        msg = form['message'].value()
        recepient = Patient.objects.get(uid=pk).email
        send_mail(str(sub),str(msg),EMAIL_HOST_USER,[recepient],fail_silently=False)

        return HttpResponseRedirect(reverse('success'))
    else:
        return render(request,"email_form.html",{'form':form})

def success(request):
    return render(request,"success.html",{})


def Add(request):
    return render(request,"add.html",{})

'''def RecordsListView(request):
        p = Consult.objects.filter(consult=request.consult)
        return render(request,'list_record.html',{'p':p})'''

class RecordsListView(LoginRequiredMixin,ListView):

    model = Consult
    context_object_name = "p"
    template_name = "list_record.html"

    def get_queryset(self,*args,**kwargs):
        h=Patient.objects.get(uid=self.kwargs['pk'])
        return Consult.objects.filter(consult=h)


class RecordsDetailView(LoginRequiredMixin,DetailView):

    model = Consult
    template_name = "detail_record.html"
    context_object_name = "h"

    def get_object(self,*args,**kwargs):
        d=Consult.objects.get(pk=self.kwargs['pks'])
        d=d.id
        return Consult.objects.get(id=d)


class PatientDeleteView(LoginRequiredMixin,DeleteView):

    model = Patient
    success_url = reverse_lazy('patient_list')

class ConsultDeleteView(LoginRequiredMixin,DeleteView):

    model = Consult
    success_url = reverse_lazy('patient_list')
    template_name = "patient_record_confirm_delete.html"