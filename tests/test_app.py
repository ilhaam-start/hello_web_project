# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
"""
When: I make a GET request to /
Then: I should get a 200 response
"""
def test_get_wave(web_client):
    # We'll simulate sending a GET request to /wave?name=Dana
    # This returns a response object we can test against.
    response = web_client.get("/submit?name=Dana")
    # Assert that the status code was 200 (OK)
    assert response.status_code == 200
    # Assert that the data returned was the right string
    assert response.data.decode("utf-8") == "I am waving at Dana"

"""
When: I make a POST request to /submit
And: I send a name and message as body parameters
Then: I should get a 200 response with the right content
"""
def test_post_submit(web_client):
    # We'll simulate sending a POST request to /submit with a name and message
    # This returns a response object we can test against.
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello" '

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""
When: I make a POST request to /sort-names
And: I send "Ilhaam,Ahmed,Layla,Hussein" as the body paramater text
Then: I should get a 200 response with the names in alphabetical 
order- Ahmed,Hussein,Ilhaam,Layla
"""
def test_sort_names_example(web_client):
    response = web_client.post('/sort-names', data={'names': 'Ilhaam,Ahmed,Layla,Hussein'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Ahmed,Hussein,Ilhaam,Layla'

"""
When: I make a POST request to /sort-names
And: I send "Joe,Alice,Zoe,Julia,Kieran" as the body paramater text
Then: I should get a 200 response with the names in alphabetical
order- Alice,Joe,Julia,Kieran,Zoe
"""
def test_sort_names_new(web_client):
    response = web_client.post('/sort-names', data={'names': 'Alice,Joe,Julia,Kieran,Zoe'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
When: I make a POST request to /sort-names
And: I send "zzzzz,hhhhh,aaaab,fgfhfh,jk" as the body paramater text
Then: I should get a 200 response with the names in alphabetical
order- aaaab,fgfhfh,hhhhh,jk,zzzzz
"""
def test_sort_names_random(web_client):
    response = web_client.post('/sort-names', data={'names': 'zzzzz,hhhhh,aaaab,fgfhfh,jk'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'aaaab,fgfhfh,hhhhh,jk,zzzzz'

"""
When: I make a POST request to /sort-names
And: I send nothing as the body parameter text
Then: I should get a 400 Bad Request and a message that says
'Please provide some names'.
"""
def test_no_name_invalid(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Please provide some names'

"""
When: I make a GET request to /names
And: I send Eddie as the query parameter
Then: I should get a 200 OK response with the following
output - Julia, Alice, Karim, Eddie
"""
def test_get_list_with_eddie(web_client):
    response = web_client.get("/names?add_name=Eddie")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Julia, Alice, Karim, Eddie"