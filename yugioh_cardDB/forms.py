from django import forms


class SearchForm(forms.Form):
    text = forms.CharField(max_length=255)
    name_or_all = forms.ModelChoiceField(
        queryset=None,
        label="選択",
        widget=forms.RadioSelect(),
        empty_label=None,
    )
