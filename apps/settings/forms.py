from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='Предмет',widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='Текст',widget=forms.Textarea(attrs={'class':'form-control',"rows":5}))