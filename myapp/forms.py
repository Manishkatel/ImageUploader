from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image  # Reference the model, not an instance
        fields = '__all__'  # Include all fields in the form
        labels = {'photo': ''}  # Match 'photo' to the actual field name in your model
