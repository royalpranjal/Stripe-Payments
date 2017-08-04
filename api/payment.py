import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from User.models import Person, Card

stripe.api_key = "sk_test_3AQ26cqRyBTo0ygj85Tug97p"


@csrf_exempt
def create_customer(request):
    email = request.POST.get('email', None)
    cust = stripe.Customer.create(
        email=email
    )

    if email is not None:
        Person.objects.create(email=email, customer_id=cust.id)

    return JsonResponse(cust)


@csrf_exempt
def create_card(request):
    person = Person.objects.last()
    customer = stripe.Customer.retrieve(person.customer_id)
    card = customer.sources.create(source="tok_mastercard")
    Card.objects.create(
        card_id=card.id,
        person=person
    )
    return JsonResponse(card)


@csrf_exempt
def create_charge(request):
    amount = 1000
    customer_id = Person.objects.last().customer_id
    print("started")
    t = datetime.now()
    for i in range(1, 100):
        charge = stripe.Charge.create(
            amount=amount,
            currency="usd",
            customer=customer_id
        )
        print(str(i) + " ---> " + str((datetime.now()-t).seconds))
    print("done in {}".format((datetime.now()-t).seconds))

    return JsonResponse(charge)
