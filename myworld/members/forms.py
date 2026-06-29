from django import forms
from .models import ImageUpload
from .models import Student
from .models import Staff

class UploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['title', 'image']

class Studentbio(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'clas','photo','marksheet']

class Staffbio(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'designation','photo']