from django import forms

web_scrape_choices = (
    ("1", "GPU"),
    ("2", "CPU"),
    ("3", "Motherboard"),
    ("4", "Monitor")
)


class QuizForm(forms.Form):
    pc_parts_choice = forms.ChoiceField(choices = web_scrape_choices)