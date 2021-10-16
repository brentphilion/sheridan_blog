"""
makes a get request to /
passes if it returns a 200
dont foget to runserver before trying it
"""
def test_index_ok(client):
    response = client.get('/')
    assert response.status_code == 200

