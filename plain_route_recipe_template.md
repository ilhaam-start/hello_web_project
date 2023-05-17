# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Home route
POST /sort-names

# Body parameters 
names=Joe,Alice,Zoe,Julia,Kieran

# Submit message route
POST /sort-names
  name: string, seperated by commas
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# POST /sort-names
#  Parameters:
#    name: Ilhaam, Ahmed, Layla, Hussein
#  Expected response (200 OK):
"""
returns the same list, sorted in alphabetical order.
(Ahmed,Hussein,Ilhaam,Layla)
"""

# POST /sort-names
#  Parameters:
#    name: Joe,Alice,Zoe,Julia,Kieran
#  Expected response (200 OK):
"""
Alice,Joe,Julia,Kieran,Zoe
"""

# POST /sort-names
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a few names.
"""

#GET /names
# Parameters:
#   name: Eddie
# Expected response (200 OK):
"""
Julia, Alice, Karim, Eddie
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

"""
POST /sort-names
Parameters:
  names: Ilhaam, Ahmed, Layla, Hussein
Expected response (200 OK): Ahmed,Hussein,Ilhaam,Layla
"""
def test_sort_names_example(web_client):
  response = web_client.post('/sort-names', data={'names': 'Ilhaam,Ahmed,Layla,Hussein'})
  assert response.status_code == 200
  assert response.data.decode('utf-8') == 'Ahmed,Hussein,Ilhaam,Layla'

"""
POST /sort-names
Parameters:
  names: Joe,Alice,Zoe,Julia,Kieran
Expected response (200 OK): Alice,Joe,Julia,Kieran,Zoe
"""
def test_sort_names_example(web_client):
  response = web_client.post('/sort-names', data={'names': 'Alice,Joe,Julia,Kieran,Zoe'})
  assert response.status_code == 200
  assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
POST /sort-names
 Parameters: none
 Expected response (400 Bad Request): Please provide a few names.
"""
def test_no_name_invalid(web_client):



<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
