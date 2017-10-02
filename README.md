# Stripe Payments abstraction layer

The **Payment.py**   contains some abstraction routines which can be used to interact with the **Stripe Payments API**. 

####List of implemented methods :
1. ```create_customer``` - Pass in the user instance whom you want to register to stripe. The response contains the customer who is registered with stripe.

2. ```retrieve_customer``` - Pass in the user instance whose customer instance you want to retrieve from stripe. The response contains the customer who is registered with stripe.

3. ```get_or_create_customer``` - This method does what 1 & 2 do combined so you need not worry about checking if the customer exists before retrieval. This routine creates a customer if it's not already registered.

4. ```add_card``` - Pass in the user instance & the token (which you get after tokenising the card) to save a card against a user.

5. ```all_cards``` - Pass in the user instance to retrieve all cards saved against a customer. The limit set is of 30 cards in response.

6. ```delete_card``` - Pass in the user instance & the card id to delete a saved card for a user.

7. ```retrieve_card``` - Pass in the user instance & the card id to retrieve a saved card for a user. The response will have only the last 4 digits of the card number instead of the complete details (regulations).

8. ```get_default_card_id``` - Pass in the user instance to retrieve the default card id for the user.

9. ```get_default_card``` - Pass in the user instance to retrieve the default card for the user. By default, the first added card is treated as the default card.

10. ```change_default_card``` - Pass in the user instance & the card id to change the default card for the user. 

11. ```create_charge``` - Pass in the user instance, the amount to be charged & the card id for which the card has to be charged. The currency here is pounds. 
`Note` - If you want to create a charge for 30 pounds then specify the amount as 3000 as the charge is always created in the smallest denomination.

12. ```refund_charge``` Pass in the charge id & the amount to be refunded. A charge can be refunded multiple times until the whole amount is refunded. 

#### Pre-requisites
1. `TLS` should be upgraded to 1.2. For more information, [visit this](https://stripe.com/blog/upgrading-tls)

2. The `user` model should contain the following fields
	a)`stripe_id `
   b)`email` (not necessary for stripe but makes it to easier to manage the stripe dashboard)

3. `stripe api_key` should be specified in *Payment.api* 


#### Usage
```
from your_payment_path import Payment
from your_user_path import User 

class YourView():
	user = User.objects.get(email="123@abc.com")
	Payment.create_customer(user)
```

#### References
[**Stripe API Reference**](https://stripe.com/docs/api)
[**Upgrading TLS**](https://stripe.com/blog/upgrading-tls)
