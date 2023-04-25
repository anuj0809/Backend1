from .models import Music
from django import forms


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ["title", "upload_mode", "file", "shared_with"]

    