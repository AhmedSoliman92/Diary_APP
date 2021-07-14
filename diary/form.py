from .models import DiaryModel
from django import forms


class DiaryForm(forms.ModelForm):
    class Meta:
        model = DiaryModel
        fields = ('diary_msg',)
        widgets = {
            'diary_msg': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Whatz\' in your mind?'})
        }
