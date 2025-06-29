from django import forms
from django.core.validators import RegexValidator

class TempForm(forms.ModelForm):
    pass


phone_validator = RegexValidator(regex=r"^\+?1?\d{9,15}$", message="Tuura telefon nomer kirgiz")

class TempForm(forms.Form):
    email = forms.EmailField(
        label="Email talaasy",
        max_length=50,
        widget=forms.EmailInput(attrs={'placeholder': "email_name@example.com"})
    )

    text = forms.CharField( 
        label="Text talaasy", 
        max_length=20,
        widget=forms.Textarea(attrs = {'rows': 5, 'placeholder': 'Enter your feedback her'})
    )

    phone_number = forms.CharField(
        label="telefon nomer",
        validators=[phone_validator],
        required=False
        )
    # def clean_text(self):
    #     data = self.cleaned_data['text']

    #     if "temp" in data:
    #         raise forms.ValidationError("Temp degen soz koldonso bolboit")
        
    #     return data
    
    # def clean_email(self):
    #     data = self.cleaned_data['email']

    #     # .com .kg
    #     if not "gmail.com" in data:
    #         raise forms.ValidationError("Tolko gmail pochtalary kerek")

    #     return data
    
    def clean(self):

        cleaned_data = super().clean()

        data = cleaned_data['text']

        if "temp" in data:
            raise forms.ValidationError("Temp degen soz koldonso bolboit clean()")
        
        data = cleaned_data['email']

        # .com .kg
        if not "gmail.com" in data:
            raise forms.ValidationError("Tolko gmail pochtalary kerek clean()")