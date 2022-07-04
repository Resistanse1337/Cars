import requests


def create_user():
    data = {
        "email": "test@mail.ru",
        "username": "user",
        "password": "123"
    }

    r = requests.post("http://127.0.0.1:8000/auth/users/", data=data).text


def login():
    data = {
        "username": "user",
        "password": "123"
    }

    r = requests.post("http://127.0.0.1:8000/auth/token/login/", data=data).json()

    return r["auth_token"]


def send_csv(headers):
    file = open("tmp/test.csv", "rb")

    r = requests.post("http://127.0.0.1:8000/cars/", files={'upload_file': file}, headers=headers).text

    print(r)


def send_xlsx(headers):
    file = open("tmp/book1.xlsx", "rb")

    r = requests.post("http://127.0.0.1:8000/cars/", files={'upload_file': file}, headers=headers).text

    print(r)


def create_car(headers):
    data = {'id': 1, 'mark': 'gfdg', 'model': 'fdgfd', 'color': 'gdfg', 'registration_number': 'fdgd',
            'release_year': 2022, 'vin': 'dsfdsf', 'sts_number': 'dsfdsf', 'sts_date': '2022-07-15'}
    r = requests.post("http://127.0.0.1:8000/cars/", headers=headers, data=data).json()
    print(r)


def get_cars(headers):
    r = requests.get("http://127.0.0.1:8000/cars", headers=headers).json()
    print(r)


def delete_car(headers):
    r = requests.delete("http://127.0.0.1:8000/cars/1/", headers=headers)
    print(r)


if __name__ == "__main__":
    create_user()
    token = login()
    headers = {"Authorization": f"Token {token}"}
    # send_xlsx(headers)
    # send_csv(headers)
    # create_car(headers)
    # get_cars(headers)
    # delete_car(headers)


