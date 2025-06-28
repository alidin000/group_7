from django import forms


class TempForm(forms.ModelForm):
    pass



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

    def clean_text(self):
        data = self.cleaned_data['text']

        if "temp" in data:
            raise forms.ValidationError("Temp degen soz koldonso bolboit")
        
        return data

    