from django import forms


class LoginForms(forms.Form):
    username = forms.CharField(label='Login Name', required=True, max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg.: Jonh Doe'}))
    password = forms.CharField(label='Password', required=True, max_length=64, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Type your password'}))


class RegisterForms(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg.: jonh_doe'}))
    email = forms.EmailField(label='Email', required=True, max_length=128, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Eg.: jonhdoe@space.alura.com.br'}))
    password = forms.CharField(label='Password', required=True, max_length=64, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Type your password'}))
    confirm_password = forms.CharField(label='Confirm Password', required=True, max_length=64, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Type your password again'}))

    def clean_username(self):
        name = self.cleaned_data.get('username')
        if name:
            name = name.strip()
            if ' ' in name:
                raise forms.ValidationError("Space between chars isn't allowed in this field!!")
            else:
                return name

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm_password')

        if password and confirm:
            if password != confirm:
                raise forms.ValidationError('Password and confirmation should match!')
            else:
                return confirm
