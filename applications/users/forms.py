from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'gender',
            'date_birth',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres',
                }
            ),
            'ocupation': forms.TextInput(
                attrs={
                    'placeholder': 'Ocupación',
                }
            ),
            'date_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                },
            ),
        }

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales') 

class LoginForm(forms.Form):
    
    email = forms.CharField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Correo Electrónico',
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')

        return  self.cleaned_data

class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña actual'
            }
        )
    )

    password2 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña nueva'
            }
        )
    )

class VerificationForm(forms.Form):
    codregister = forms.CharField(required=True)
    
    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)
    
    def clean_codregister(self):
        code = self.cleaned_data['codregister']

        #Validate if the code and id are valids
        if len(code) == 6:
            active = User.objects.cod_validation(
                self.id_user,
                code
            )
            if not active:
                raise forms.ValidationError('El código es incorrecto')
        else:
            raise forms.ValidationError('El código es incorrecto')
    
