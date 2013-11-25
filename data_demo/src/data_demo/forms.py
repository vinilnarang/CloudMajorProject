from django import forms

class DataUploadForm (forms.Form):
	data_file = forms.FileField ()
