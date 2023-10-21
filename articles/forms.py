from django import forms
from . import models
class  createArticel(forms.ModelForm):
    class Meta:
        model=models.Article
        fields=['title','body','slug','thumb']