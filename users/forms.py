from django import forms 
from .models import User

class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email','password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.data.get('confirm-password')

        print(password, confirm_password)
        if password != confirm_password:
            self.add_error('password','Passwords do not match')
        
        if password and len(password) < 6:
            self.add_error('password','Password must be at least 6 characters long')

        return cleaned_data