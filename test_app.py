from app import app

def test_echo():
    with app.test_client() as client:
        response = client.get('/echo/world')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'world'
