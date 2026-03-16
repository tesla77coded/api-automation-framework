from faker import Faker

fake = Faker()


def create_random_user():
    return {"email": fake.email(), "password": fake.password(length=10)}
