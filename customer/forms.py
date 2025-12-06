from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import widgets

from .models import Customer


class DateInput(forms.DateInput):
    input_type = "date"


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Apelido")
    email = forms.EmailField(label="E-mail")
    area_code = forms.CharField(max_length=4, label="Código de Área")
    phone_number = forms.CharField(max_length=12, label="Telemóvel")
    birth_date = forms.DateField(label="Data de Nascimento", widget=DateInput())
    country = forms.CharField(label="País")
    state = forms.CharField(label="Estado")
    city = forms.CharField(label="Cidade")
    project_name = forms.CharField(label="Nome do Projeto")
    project_description = forms.CharField(
        label="Descrição do Projeto", widget=forms.Textarea()
    )
    project_status = forms.ChoiceField(
        choices=Customer.Status.choices, initial=Customer.Status.TO_DO
    )
    project_start_date = forms.DateField(label="Ínicio do Projeto", widget=DateInput())
    project_end_date = forms.DateField(label="Previsão de término", widget=DateInput())
    project_budget = forms.DecimalField(
        label="Orçamento", max_digits=10, decimal_places=2
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(
            Submit("submit", "Salvar", css_class="btn btn-primary mt-3")
        )

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "area_code",
            "phone_number",
            "birth_date",
            "country",
            "state",
            "city",
            "project_name",
            "project_description",
            "project_status",
            "project_start_date",
            "project_end_date",
            "project_budget",
        )
