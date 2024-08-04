from django import forms
from .models import ImageUpload, BackgroundImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']

class BackgroundSelectionForm(forms.Form):
    background = forms.ModelChoiceField(queryset=BackgroundImage.objects.all(), widget=forms.Select())