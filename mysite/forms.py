from django import forms

#Assigns a numerical value to each choice from the dropdown menu
web_scrape_choices = (
    ("1", "GPU"),
    ("2", "CPU"),
    ("3", "Motherboard"),
    ("4", "Monitor")
)


#Assigns the choices on the django form to the object web_scrape_choices
class QuizForm(forms.Form):
    pc_parts_choice = forms.ChoiceField(choices = web_scrape_choices)