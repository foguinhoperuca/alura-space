from django import forms

from apps.gallery.models import Photograph


class PhotographForms(forms.ModelForm):
    class Meta:
        model = Photograph
        exclude = ['published',]
        labels = {
            'name': 'Nome',
            'legend': 'Legenda',
            'description': 'Descrição',
            'photo': 'Foto',
            'category': 'Categoria',
            'photo_date': 'Data de Registro',
            'user': 'Usuário'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'legend': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date', 'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }
