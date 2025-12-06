from django.db import models
from django.urls import reverse

# Create your models here.


class Customer(models.Model):
    class Status(models.TextChoices):
        TO_DO = "to_do", "To Do"
        DOING = "doing", "Doing"
        DONE = "done", "Done"

    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField()
    birth_date = models.DateField()
    area_code = models.CharField(max_length=4)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_status = models.CharField(
        max_length=50, choices=Status.choices, default=Status.TO_DO
    )
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    project_budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.project_name}"

    def get_absolute_url(self):
        return reverse("customer:customer-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("customer:customer-delete", kwargs={"id": self.id})

    class Meta:
        db_table = "customer"
