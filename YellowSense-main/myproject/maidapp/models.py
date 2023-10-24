from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Profile(models.Model):
    society_name = models.CharField(max_length=20, default='Society1')
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, default='Female')
    contact = models.CharField(max_length=15)
    country = models.CharField(max_length=20, default='Country')
    available = models.BooleanField(default=True)
    start_date = models.DateField(null=True)
    preferred_time_range_start = models.TimeField(null=True)
    preferred_time_range_end = models.TimeField(null=True)
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    sunday_availability = models.BooleanField()
    languages = models.TextField()
    experience = models.TextField()
    additional_details = models.TextField()

    class Meta:
        abstract = True

class Maid(Profile):
    services_offered = models.TextField()

class Cook(Profile):
    cooking_options = models.TextField()
    specialty = models.TextField()

class Nanny(Profile):
    childcare_experience = models.TextField()

class Customer(models.Model):
    selected_service = models.CharField(max_length=10, default='Maid')
    society_name = models.CharField(max_length=100, default='Society2')
    preferred_gender = models.CharField(max_length=10, default='Any')
    customer_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    country = models.CharField(max_length=20, default='Country')
    timings_from = models.TimeField(null=True)
    timings_to = models.TimeField(null=True)
    additional_requirements = models.TextField(null=True)
    additional_data = models.JSONField(default=dict)  # To store additional attributes as JSON
    # selected_service=selected_service,
    # society_name=society_name,
    # preferred_gender=preferred_gender,
    # customer_name=customer_name,
    # contact=contact,
    # timings_from=timings_from,
    # timings_to=timings_to,
    # additional_requirements=additional_requirements,
    # additional_data=additional_data_json
    def __str__(self):
        return self.customer_name

class Booking(models.Model):
    STATUS_CHOICES = (
        ('Booked', 'Booked'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    )

    PROVIDER_CHOICES = (
        ('maid', 'Maid'),
        ('cook', 'Cook'),
        ('nanny', 'Nanny'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_provider_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    service_provider_id = models.PositiveIntegerField()
    service_provider = GenericForeignKey('service_provider_type', 'service_provider_id')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Booked')

    def __str__(self):
        return f"Booking for {self.customer.customer_name} with {self.service_provider}"

