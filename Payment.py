import stripe

class Payment(object):
    stripe.api_key = "YOUR SECRET KEY"

    @staticmethod
    def create_customer(user):
        customer = stripe.Customer.create(email=user.email)
        user.stripe_id = customer.id
        user.save()
        return customer

    @staticmethod
    def retrieve_customer(user):
        return stripe.Customer.retrieve(user.stripe_id)

    @staticmethod
    def get_or_create_customer(user):
        try:
            return Payment.retrieve_customer(user)
        except Exception:
            return Payment.create_customer(user)

    @staticmethod
    def add_card(token, user):
        return Payment.get_or_create_customer(user).sources.create(source=token)

    @staticmethod
    def all_cards(user):
        return Payment.get_or_create_customer(user).sources.all(
            limit=30, object='card')['data']

    @staticmethod
    def delete_card(token, user):
        Payment.get_or_create_customer(user).sources.retrieve(token).delete()

    @staticmethod
    def retrieve_card(card_id, user):
        return (Payment.get_or_create_customer(user)).sources.retrieve(card_id)

    @staticmethod
    def get_default_card_id(user):
        return Payment.get_or_create_customer(user).default_source

    @staticmethod
    def get_default_card(user):
        return Payment.retrieve_card(Payment.get_default_card_id(user), user)

    @staticmethod
    def change_default_card(token, user):
        customer = Payment.get_or_create_customer(user)
        customer.default_source = token
        customer.save()

    @staticmethod
    def create_charge(token, user, amount):
        return stripe.Charge.create(
            amount=amount,
            currency="gbp",
            source=token,
            customer=user.stripe_id,
            receipt_email=user.email
        )

    @staticmethod
    def refund_charge(charge_id):
        stripe.Refund.create(
            charge=charge_id,
            amount=int(booking.amount*100)
        )
