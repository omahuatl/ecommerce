#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request

import stripe
# This is your real test secret API key.
stripe.api_key = 'sk_test_51JhJOOLP1J0UnBMLhNrfefdmXfjlKApUfPCileBdMFhtcYkaCsQohLyJSalk9ytolULP29FGCnMpzEpMrRWwFGoN00ZZRSCTpy'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:4242'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1JhPGfLP1J0UnBML5Gy5682Q',
                    'quantity': 1,
                },
            ],
            payment_method_types=[
              'card',
              'oxxo',
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    app.run(port=4242)
