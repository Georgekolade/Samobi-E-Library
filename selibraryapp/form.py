from django import forms
from .models import Message, Upload

class MessageForms(forms.ModelForm):
	class Meta:
		model = Message
		fields = "__all__"

class UploadForms(forms.ModelForm):
	class Meta:
		model = Upload
		fields = "__all__"