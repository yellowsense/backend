from django.contrib import admin

# Register your models here.
from .models import Maid, Customer, Cook, Nanny, Booking

admin.site.register(Maid)
admin.site.register(Customer)
admin.site.register(Cook)
admin.site.register(Nanny)
admin.site.register(Booking)