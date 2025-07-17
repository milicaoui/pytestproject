import requests


# def test_always_passes():
#     assert True


def test_hello_endpoint():
    response = requests.get("http://upmtest:8081/api/hello")
    print(response)
    assert response.status_code == 200
    assert response.text == "Hello from Spring Boot!"
