

from typing import Text

from rasa_sdk import Action
import requests
import json


class ActionPlacePizzaOrder(Action):

    def name(self) -> Text:
        return "action_pizza_order"

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot('person')
        size = tracker.get_slot('size')
        topping = tracker.get_slot('toppings')
        address = tracker.get_slot('address')
        phone = tracker.get_slot('phone')
        request_body = {
          "name": name,
          "address": address,
          "phone": phone,
          "size": size,
          "toppings": topping
        }
        response = requests.post(url='https://a35i9s8cdl.execute-api.ap-south-1.amazonaws.com/test/savepizzaorder/',
                                 data=json.dumps(request_body))
        dispatcher.utter_message(text="Your order for {} {} pizza has been successfully placed :). Your order id is- {}".format(size, topping, response.text))
        return []

class ActionFetchOrderStatus(Action):

    def name(self) -> Text:
        return "action_fetch_order_status"

    def run(self, dispatcher, tracker, domain):
        order_id = tracker.get_slot('order_id')
        PARAMS = {'order_id': order_id}
        response = requests.get(url=' https://a35i9s8cdl.execute-api.ap-south-1.amazonaws.com/test/getorderstatus/',
                                 params = PARAMS)
        dispatcher.utter_message(text="{}".format(response.text))
        return []
