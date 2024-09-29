import requests

def test_frontend():
    # URL of the frontend service
    url = 'http://192.168.49.2:30001'  # Update this if needed

    # Send a GET request to the frontend
    response = requests.get(url)

    # Check if the response contains the expected message
    assert '<h1>Hello from the Backend!</h1>' in response.text

    print("Frontend service is communicating with the backend successfully!")

if __name__ == "__main__":
    test_frontend()
