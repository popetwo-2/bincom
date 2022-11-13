from django import forms
from .models import AnnouncedPuResults, Lga


class UploadResultForm(forms.ModelForm):
    class Meta:
        model = AnnouncedPuResults
        fields = ('date_entered', 'party_abbreviation', 'party_score', 'entered_by_user', 'polling_unit_uniqueid')


class LgaForm(forms.ModelForm):
    class Meta:
        model = Lga
        fields = ('lga_name',)
