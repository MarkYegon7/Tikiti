# import requests

# def get_seatgeek_event_info(api_key, event_id):
#     url = f"https://seatgeek-seatgeekcom.p.rapidapi.com/events/{event_id}"

#     headers = {
#         "X-RapidAPI-Key": api_key,
#         "X-RapidAPI-Host": "seatgeek-seatgeekcom.p.rapidapi.com"
#     }

#     try:
#         response = requests.get(url, headers=headers)

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             event_data = response.json()
#             return event_data
#         else:
#             return None
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None

        
# api_key = "c1e0ade765msh7437e8ee4750468p1612dbjsncd4f68c1085a"
# event_id = 928038

# get_seatgeek_event_info(api_key,event_id)

import requests

def get_seatgeek_event_info():
    url = "https://seatgeek-seatgeekcom.p.rapidapi.com/events/928038"
    headers = {
        "X-RapidAPI-Key": "c1e0ade765msh7437e8ee4750468p1612dbjsncd4f68c1085a",
        "X-RapidAPI-Host": "seatgeek-seatgeekcom.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    event_info = response.json()
    return event_info
