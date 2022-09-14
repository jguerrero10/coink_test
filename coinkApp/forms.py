from django import forms

from coinkApp.models import UserBasic


class UserBasicForm(forms.ModelForm):
    fullname = forms.CharField(max_length=180, label='Nombre Completo', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))
    city = forms.CharField(label='Ciudad', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

    class Meta:
        model = UserBasic
        fields = '__all__'
