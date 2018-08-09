import http.client
 
conn = http.client.HTTPSConnection("api.ibm.com")
 
headers = {
    'x-ibm-client-secret': "P7qN7qP0mU1iG2vR0fL0hG0kP1qU6tQ1iA5cS8pP0vE3pT4vN6",
    'x-ibm-client-id': "c8840816-060a-4e38-9242-38f65bbf3eb9",
    'authorization': "Bearer A5iql6i8tI5H9lx+9f2UKGXITl7BOVhyxC+awOJV1L3+DjFQbPcw/sxDIwcOt4VVbrsUwxOl0G19RloWQGsFTz+TwsUNavqxu0WoINRB2q5Du8AWuRiaPpYr6iImPHPwDKCv5pndVeUrmQAJy/37OmiQyuvhjO7SvU+8J1g7gIyHg+N0qO62c7EaCHyzPCm1A9JD7VZsBvXkI6I+gp7khB0iQqpcxUeXpM0NPSyQ8A7h4GrbAcAPY9gE6SXSeMKOE1yZuJBSK/sjVWwnL+sjccicDMJYL97KgHK7X9GnPRVfNYcFuRsgsB5NgD8tYHnPm6Yc+0KbLm76e1Y+Be0vHfVUE8ogMpXjCXVSAUdyFlXo0jy0ix5uGWdUuHNtgJ0VXmVMtzGIW/g=;=;LS0=","token_type":"bearer","expires_in":"3600","scope":"userContext","refresh_token":"BTFatz/aLkJ2311sWd0aCPQJCM3swH8IHLt5QyJeanNEEzAgRj6wuvzeef+eQikQ1f/Wr5ZRPprJA5T+8Lxb89e3V736ulnI/UtCMZZgWH5ULLRcCAk0QeOLY/IAXxOKprHBu6pnppbZP4b4zoqbVINaKYZVATTZK1Nd8KUuWr1Ul4EpX76AuoIaP0CCjFlSwXIxMUv1CVrOtwdmFzxQcx8iVhMyspP8/seuQWstWllO4leDBCCPsoZz10q0QBk9ayOaOfg27kmCjb+Ze7IkPuZmuBHpUwzacjfDKHUt3T8aAHjX7dbzCPUtZLBYy/HwxUdpmgTU1h9ArfbKDERfKyqgTvHx2ZDuP4wX8FE0/aFPnGejWc8YHCnjIw++sUfo",
    'accept': "application/json",
    'content-type': "application/json"
    }
 
conn.request("DELETE", "/watsonanalytics/run/data/v1/datasets/b1512366-30fe-4920-a0fd-7cc709d3a350", headers=headers)
 
res = conn.getresponse()
data = res.read()
 
print(data.decode("utf-8"))