from django import forms
# type="range" class="form-range" min="8" max="16" step="1" id="customRange2"
class passwordForm(forms.Form):
    length = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "type":"range",
            "class":"form-range",
            "min":8,
            "max":16,
            "step":1,
            "value":8
        })
    )
    lower = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class":"form-check"
        })
    )
    upper = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class":"form-check"
        })
    )
    digits = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class":"form-check"
        })
    )
    symbols = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class":"form-check"
        })
    )