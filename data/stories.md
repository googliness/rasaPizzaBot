## story1
* greet
  - utter_greet
  - utter_service
* pizza_no_details
  - utter_size
* pizza_only_size{"size":"large"}
  - slot{"size":"large"}
  - utter_topping
* pizza_only_topping{"topping":"cheese"}
  - slot{"topping":"cheese"}
  - utter_fetch_name
* greet_name{"person":"jaya"}
  - slot{"person":"jaya"}
  - utter_fetch_address
* user_address_full{"address":"house 45/B, 16th st, koramangala, bangalore"}
  - slot{"address":"house 45/B, 16th st, koramangala, bangalore"}
  - utter_fetch_number
* user_phone{"phone":"6767898954"}
  - slot{"phone":"6767898954"}
  - action_pizza_order

## story2
* greet
  - utter_greet
  - utter_service
* pizza_only_size{"size":"medium"}
  - slot{"size":"medium"}
  - utter_topping
* pizza_only_topping{"topping":"onions"}
  - slot{"topping":"onions"}
  - utter_fetch_name
* greet_name{"person":"swastik"}
  - slot{"person":"swastik"}
  - utter_fetch_address
* user_address_full{"address":"21, richmond road, banglore"}
  - slot{"address":"21, richmond road, banglore"}
  - utter_fetch_number
* user_phone{"phone": "909897654"}
  - slot{"phone": "9076897654"}
  - action_pizza_order
  
## story3
* greet
  - utter_greet
  - utter_service
* pizza_only_topping{"topping":"pepperoni"}
  - slot{"topping":"pepperoni"}
  - utter_size
* pizza_only_size{"size":"small"}
  - slot{"size":"small"}
  - utter_fetch_name
* greet_name{"person":"rashid"}
  - slot{"person":"rashid"}
  - utter_fetch_address
* user_address_full{"address":"Q.no: 21A, 7th st., cubbon park, bangalore"}
  - slot{"address":"Q.no: 21A, 7th st., madivala, bangalore"}
  - utter_fetch_number
* user_phone{"phone": "876809054"}
  - slot{"phone": "876809054"}
  - action_pizza_order

 ## story4
* greet
  - utter_greet
  - utter_service
* pizza_all_details{"topping":"olives", "size":"large"}
  - slot{"topping":"olives", "size":"large"}
  - utter_fetch_name
* greet_name{"person":"raghu"}
  - slot{"person":"raghu"}
  - utter_fetch_address
* user_address_full{"address":"1st floor, 118, S.R flora Apartments, marathalli, banaglore"}
  - slot{"address":"1st floor, 118, S.R flora Apartments, marathalli, banaglore"}
  - utter_fetch_number
* user_phone{"phone":"7887564560"}
  - slot{"phone":"7887564560"}
  - action_pizza_order
 
 ## story5
* greet
  - utter_greet
  - utter_service
* pizza_order_status_no_details
  - utter_order_id
* pizza_order_status_with_id{"order_id":"26"}
  - slot{"order_id":"26"}
  - action_fetch_order_status
  
 ## story6
* greet
  - utter_greet
  - utter_service
* pizza_order_status_with_id{"order_id":"73"}
  - slot{"order_id":"73"}
  - action_fetch_order_status
  
 ## story7
* greet
  - utter_greet
  - utter_service
* pizza_order_status_with_id{"order_id":"18"}
  - slot{"order_id":"18"}
  - action_fetch_order_status
 
 ## story8
* greet
  - utter_greet
  - utter_service
* pizza_order_status_no_details
  - utter_order_id
* pizza_order_status_with_id{"order_id":"44"}
  - slot{"order_id":"44"}
  - action_fetch_order_status
  

## interactive_story_1
* greet
    - utter_greet
    - utter_service
* pizza_no_details
    - utter_size
* pizza_all_details{"size": "medium"}
    - slot{"size": "medium"}
    - utter_topping
* pizza_all_details{"topping": "onions"}
    - slot{"topping": "onions"}
    - utter_fetch_name
* greet_name{"person": "rahul", "PERSON": "Rahul"}
    - slot{"person": "rahul"}
    - utter_fetch_number
* user_phone{"phone": "9076897654"}
    - slot{"phone": "9076897654"}
    - utter_fetch_address
* user_address_full{"address": "4647, st 36, banglore"}
    - slot{"address": "4647, st 36, banglore"}
    - action_pizza_order


## interactive_story_2
* greet
    - utter_greet
    - utter_service
* pizza_size_details{"size": "small"}
    - slot{"size": "small"}
    - utter_topping
* pizza_only_topping{"topping": "corn"}
    - slot{"topping": "corn"}
    - utter_fetch_name
* greet_name{"person": "nikhil"}
    - slot{"person": "nikhil"}
    - utter_fetch_address
* user_address_full{"address": "334, 2nd floor, 9th street, hsr layout, bangalore"}
    - slot{"address": "334, 2nd floor, 9th street, hsr layout, bangalore"}
    - utter_fetch_number
* user_phone{"phone": "67843545347"}
    - slot{"phone": "67843545347"}
    - action_pizza_order


## interactive_story_3
* greet
    - utter_greet
    - utter_service
* pizza_all_details{"size": "medium", "topping": "pepproni"}
    - slot{"size": "medium"}
    - slot{"topping": "pepproni"}
    - utter_fetch_name
* greet_name{"person": "ravi"}
    - slot{"person": "ravi"}
    - utter_fetch_address
* user_address_full{"address": "madivala, bangalore"}
    - slot{"address": "madivala, bangalore"}
    - utter_fetch_number
* user_phone{"phone": "8989765676"}
    - slot{"phone": "8989765676"}
    - action_pizza_order

## interactive_story_4
* greet
    - utter_greet
    - utter_service
* pizza_all_details{"size": "large", "topping": "onions"}
    - slot{"size": "large"}
    - slot{"topping": "onions"}
    - utter_fetch_name
* greet{"person": "adwait"}
    - slot{"person": "adwait"}
    - utter_fetch_address
* user_address_full{"address": "room 202 hotel plaze domlur"}
    - slot{"address": "room 202 hotel plaze domlur"}
    - utter_fetch_number
* user_phone{"phone": "8735986383"}
    - slot{"phone": "8735986383"}
    - action_pizza_order

## interactive_story_5
* greet
    - utter_greet
    - utter_service
* pizza_order_status_no_details
    - utter_order_id
* pizza_order_status_with_id{"order_id": "4"}
    - slot{"order_id": "4"}
    - action_fetch_order_status

## interactive_story_6
* greet
    - utter_greet
    - utter_service
* pizza_order_status_no_details
    - utter_order_id
* pizza_order_status_with_id{"order_id": "11"}
    - slot{"order_id": "11"}
    - action_fetch_order_status

## interactive_story_7
* greet
    - utter_greet
    - utter_service
* pizza_order_status_no_details
    - utter_order_id
* pizza_order_status_with_id{"order_id": "34"}
    - slot{"order_id": "34"}
    - action_fetch_order_status


## interactive_story_8
* greet
    - utter_greet
    - utter_service
* pizza_no_details
    - utter_size
* pizza_all_details{"size": "medium"}
    - slot{"size": "medium"}
    - utter_topping
* pizza_only_topping{"topping": "corn"}
    - slot{"topping": "corn"}
    - utter_fetch_name
* greet_name{"person": "ravi kumar"}
    - slot{"person": "ravi kumar"}
    - utter_fetch_number
* user_phone{"phone": "8736356876"}
    - slot{"phone": "8736356876"}
    - utter_fetch_address
* user_address_full{"address": "35 electronic city bangalore"}
    - slot{"address": "35 electronic city bangalore"}
    - action_pizza_order

## interactive_story_1
* greet
    - utter_greet
    - utter_service
* pizza_no_details
    - utter_size
* pizza_all_details{"size": "small"}
    - slot{"size": "small"}
    - utter_topping
* pizza_only_topping{"topping": "cheese"}
    - slot{"topping": "cheese"}
    - utter_fetch_name
* greet_name{"person": "Meghna Singh"}
    - slot{"person": "Meghna Singh"}
    - utter_fetch_number
* user_phone{"phone": "6789067890"}
    - slot{"phone": "6789067890"}
    - utter_fetch_address
* user_address_full{"address": "22 street 1st floor 33 indiranagar"}
    - slot{"address": "22 street 1st floor 33 indiranagar"}
    - action_pizza_order
