from django import forms

FILTERS = [
    ('-publish_date',"--select--"),
    ('publish_date', "Filter By Date Increasing"),
    ('-publish_date', "Filter By Date Increasing"),
    ('title', "Filter By Title Increasing"),
    ('-title', "Filter By Title Decreasing"),
]


class FilterForm(forms.Form):
    selected_filter = forms.CharField(label='Filter Results', widget=forms.Select(choices=FILTERS))
