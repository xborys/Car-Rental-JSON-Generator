from django import forms

class ImportForm(forms.Form):
    json_file = forms.FileField(label='Select JSON file')