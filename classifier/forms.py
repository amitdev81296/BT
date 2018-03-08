from django.forms import ModelForm
from classifier.models import UploadFile


class UploadFileForm(ModelForm):
    class Meta:
        model = UploadFile
        fields = ['file']
