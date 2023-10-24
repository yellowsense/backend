from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import Maid, Cook, Nanny, Customer, Booking
from django.db.models import Q
import json

def home(request):
    return render(request, 'home.html')

def request_maid(request):
    return render(request,'request_maid.html')

def request_cook(request):
    return render(request,'request_cook.html')

def request_nanny(request):
    return render(request,'request_nanny.html')

def add_service_provider(request):
    return render(request, 'add_service_provider.html')

def success_page(request):
    return render(request, 'success-page.html')

def add_maid(request):
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST['name']
        gender = request.POST['gender']
        contact = request.POST['contact']
        country = request.POST['country']
        start_date = request.POST['start_date']
        preferred_time_range_start = request.POST['preferred_time_range_start']
        preferred_time_range_end = request.POST['preferred_time_range_end']
        maid_services_offered = ', '.join(request.POST.getlist('maid_services_offered'))
        cost_per_day = request.POST['cost_per_day']
        cost_per_month = request.POST['cost_per_month']
        sunday_availability = request.POST['sunday_availability'] == "Yes"
        languages = ', '.join(request.POST.getlist('languages'))
        experience = request.POST['experience']
        additional_details = request.POST['additional_details']

        # Create a new Maid object and save it to the database
        Maid.objects.create(
            name=name,
            gender=gender,
            contact=contact,
            country=country,
            start_date=start_date,
            preferred_time_range_start=preferred_time_range_start,
            preferred_time_range_end=preferred_time_range_end,
            services_offered=maid_services_offered,
            cost_per_day=cost_per_day,
            cost_per_month=cost_per_month,
            sunday_availability=sunday_availability,
            languages=languages,
            experience=experience,
            additional_details=additional_details,
        )

        return render(request, 'success-page.html')  # Redirect to a success page after form submission

    return render(request, 'add_maid.html')  # Render the form page for GET requests

def add_cook(request):
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST['name']
        gender = request.POST['gender']
        contact = request.POST['contact']
        start_date = request.POST['start_date']
        preferred_time_range_start = request.POST['preferred_time_range_start']
        preferred_time_range_end = request.POST['preferred_time_range_end']
        cost_per_day = request.POST['cost_per_day']
        cost_per_month = request.POST['cost_per_month']
        sunday_availability = request.POST['sunday_availability'] == "Yes"
        languages = ', '.join(request.POST.getlist('languages'))
        cooking_options = request.POST['cooking_options']
        experience = request.POST['experience']
        additional_details = request.POST['additional_details']

        # Create a new Cook object and save it to the database
        Cook.objects.create(
            name=name,
            gender=gender,
            contact=contact,
            start_date=start_date,
            preferred_time_range_start=preferred_time_range_start,
            preferred_time_range_end=preferred_time_range_end,
            cost_per_day=cost_per_day,
            cost_per_month=cost_per_month,
            sunday_availability=sunday_availability,
            languages=languages,
            cooking_options=cooking_options,
            experience=experience,
            additional_details=additional_details,
        )

        return render(request, 'success-page.html')  # Redirect to a success page after form submission

    return render(request, 'add_cook.html') 

def add_nanny(request):
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST['name']
        gender = request.POST['gender']
        contact = request.POST['contact']
        start_date = request.POST['start_date']
        preferred_time_range_start = request.POST['preferred_time_range_start']
        preferred_time_range_end = request.POST['preferred_time_range_end']
        cost_per_day = request.POST['cost_per_day']
        cost_per_month = request.POST['cost_per_month']
        sunday_availability = request.POST['sunday_availability'] == "Yes"
        languages = ', '.join(request.POST.getlist('languages'))
        childcare_experience = request.POST['childcare_experience']
        experience = request.POST['experience']
        additional_details = request.POST['additional_details']

        # Create a new Nanny object and save it to the database
        Nanny.objects.create(
            name=name,
            gender=gender,
            contact=contact,
            start_date=start_date,
            preferred_time_range_start=preferred_time_range_start,
            preferred_time_range_end=preferred_time_range_end,
            cost_per_day=cost_per_day,
            cost_per_month=cost_per_month,
            sunday_availability=sunday_availability,
            languages=languages,
            childcare_experience=childcare_experience,
            experience=experience,
            additional_details=additional_details,
        )

        return render(request, 'success-page.html')  # Redirect to a success page after form submission

    return render(request, 'add_nanny.html')

def add_customer(request):
    if request.method == 'POST':
        selected_service = request.POST['selected_service']
        society_name = request.POST['society_name']
        preferred_gender = request.POST['preferred_gender']
        customer_name = request.POST['customer_name']
        contact = request.POST['contact']
        country = request.POST['country']
        timings_from = request.POST['timings_from']
        timings_to = request.POST['timings_to']
        additional_requirements = request.POST['additional_requirements']

        additional_data = {}  # Initialize an empty dictionary to hold additional attributes
        services_required = ""
        if selected_service == 'cook':
            cook_attributes = ['add_ons', 'number_of_people', 'meals_per_day', 'veg_or_non_veg', 'cooking_specialty']
            additional_data.update({attr: request.POST[attr] for attr in cook_attributes})
            
        elif selected_service == 'maid':
            services_required = ', '.join(request.POST.getlist('services_required'))
            additional_data.update({'services_required' : services_required})
            maid_attributes = ['other_services', 'house_size']
            additional_data.update({attr: request.POST[attr] for attr in maid_attributes})
            
        elif selected_service == 'nanny':
            nanny_attributes = ['children_gt2', 'children_lt2']
            additional_data.update({attr: request.POST[attr] for attr in nanny_attributes})

        # Convert the additional_data dictionary to JSON
        additional_data_json = json.dumps(additional_data)

        # Create a new Customer object and save it to the database
        customer_instance = Customer.objects.create(
            selected_service=selected_service,
            society_name=society_name,
            preferred_gender=preferred_gender,
            customer_name=customer_name,
            contact=contact,
            country=country,
            timings_from=timings_from,
            timings_to=timings_to,
            additional_requirements=additional_requirements,
            additional_data=additional_data_json  # Store additional data JSON in the model
        )
        matching_providers = get_matching_providers(selected_service, preferred_gender, timings_from, timings_to, society_name, services_required)
        
        return render(request, 'provider_list.html', {'customer_instance': customer_instance, 'providers': matching_providers, 'selected_service' : selected_service})

    return render(request, 'home.html')  # Render the form page for GET requests

# Create your views here.

def get_matching_providers(selected_service, preferred_gender, timings_from, timings_to, society_name, services_required):
    if selected_service == 'cook':
        providers = Cook.objects.filter(gender=preferred_gender, society_name=society_name, preferred_time_range_start__lte=timings_from, preferred_time_range_end__gte=timings_to)
    elif selected_service == 'maid':
        print("in maid")
        providers = Maid.objects.filter(gender=preferred_gender, society_name=society_name, preferred_time_range_start__lte=timings_from, preferred_time_range_end__gte=timings_to, services_offered__icontains=services_required)
    elif selected_service == 'nanny':
        providers = Nanny.objects.filter(gender=preferred_gender, society_name=society_name, preferred_time_range_start__lte=timings_from, preferred_time_range_end__gte=timings_to)
    else:
        providers = []  # If the selected service is not recognized
    # print("providers - ", providers)
    return providers

# matching_providers = get_matching_providers('maid', 'female', '15:00:00', '17:00:00', "Society1", "Sweeping, Mopping")
# print(matching_providers)
# print("All maids")
# all_maids = Customer.objects.all()

# for maid in all_maids:
#     print(f"id: {maid.id}")
#     print(f"Name: {maid.customer_name}")
    # print(f"Gender: {maid.gender}")
    # print(f"Contact: {maid.contact}")
    # print(f"Society: {maid.society_name}")
    # print(f"Start time: {maid.preferred_time_range_start}")
    # print(f"end time: {maid.preferred_time_range_end}")
    # print(f"services offered type: {type(maid.services_offered)}")

    # print(f"services offered: {maid.services_offered}")

        # render(request, 'provider_list.html', {'customer_name': customer_name, 'providers': matching_providers})

def book_provider(request):
    if request.method == 'POST':
        selected_provider_id = request.POST.get('selected_provider')
        customer_id = request.POST.get('customer_id')
        selected_service = request.POST.get('selected_service')

        if selected_service == 'maid':
            selected_provider = get_object_or_404(Maid, id=selected_provider_id)
        elif selected_service == 'cook':
            selected_provider = get_object_or_404(Cook, id=selected_provider_id)
        elif selected_service == 'nanny':
            selected_provider = get_object_or_404(Nanny, id=selected_provider_id)

        # Create a customer instance (assuming you have a way to identify the customer)
        customer = Customer.objects.get(pk=customer_id)  # Replace with your logic to get the customer

        # Create a booking entry in the Bookings table
        Booking.objects.create(
            customer=customer,
            service_provider_type=ContentType.objects.get_for_model(selected_provider),
            service_provider_id=selected_provider.id,
            status='Booked',  # Set the initial booking status
        )

        # Update the provider's availability status
        selected_provider.available = False
        selected_provider.save()

        return render(request, 'Booking-success-page.html')

    return redirect('home')

from django.http import JsonResponse

def make_service_provider_available(request, selected_service, provider_id):
    try:
        selected_provider = None

        if selected_service == "Maid":
            selected_provider = Maid.objects.get(id=provider_id)

        elif selected_service == "Nanny":
            selected_provider = Nanny.objects.get(id=provider_id)

        elif selected_service == "Cook":
            selected_provider = Cook.objects.get(id=provider_id)
        else:
            return JsonResponse({'success': False, 'error': 'Invalid service type'})

        selected_provider.available = True
        selected_provider.save()

        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
