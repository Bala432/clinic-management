from app.models import Patient,Consult,SendEmail
from django import forms

class PatientForm(forms.ModelForm):

    class Meta:

        model = Patient
        fields = "__all__"

class ConsultForm(forms.ModelForm):

    class Meta:

        model = Consult
        fields = ['problem','treatment']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['treatment'].label = 'Diagnosis'

class SendEmailForm(forms.ModelForm):

    class Meta:

        model = SendEmail
        fields = ['subject','message']

