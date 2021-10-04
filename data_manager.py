import requests

SHEETY_PRICE_ENDPOINTS = "https://api.sheety.co/9f3961adadaea306d26be4b144289070/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/9f3961adadaea306d26be4b144289070/flightDeals/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICE_ENDPOINTS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:

            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            # pprint(new_data)

            response = requests.put(
                url=f"{SHEETY_PRICE_ENDPOINTS}/{city['id']}",
                json=new_data
            )

            # print(response.headers)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
