from django import forms


class TextForm(forms.Form):
    text = forms.CharField(label='Add Item', max_length=300)