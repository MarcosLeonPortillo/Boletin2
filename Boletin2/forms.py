from django import forms
from django.core.exceptions import ValidationError
import re

class formulario(forms.Form):
    username = forms.CharField(
        label='username',
        required=True,
    )

    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(),
        required=True,
    )
    
    fechaHora = forms.DateTimeField(
        widget=forms.HiddenInput(),
        input_formats=['%Y-%m-%d'],
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        fechaHora = cleaned_data.get("fechaHora")

        if username == password:
            raise forms.ValidationError('El nombre de usuario y la contraseña no pueden ser iguales.')

        
        if username.lower() in password.lower():
            raise forms.ValidationError('La contraseña no puede contener el nombre de usuario.')

        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')

        # Verificar al menos una mayúscula
        if not any(char.isupper() for char in password):
            raise forms.ValidationError('La contraseña debe contener al menos una letra mayúscula.')

        # Verificar al menos una minúscula
        if not any(char.islower() for char in password):
            raise forms.ValidationError('La contraseña debe contener al menos una letra minúscula.')

        # Verificar al menos un carácter especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError('La contraseña debe contener al menos un carácter especial.')

        # Verificar al menos un número
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('La contraseña debe contener al menos un número.')


        return cleaned_data

    