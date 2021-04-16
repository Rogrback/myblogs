from applications.home.models import Home

# Proccess for recover phone and email from home register

def home_contact(request):
    home = Home.objects.latest('created')

    return {
        'phone': home.phone,
        'email': home.contact_email,
    }