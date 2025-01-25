from faker import Faker
import random

fake = Faker()

def fake_product():
    return {
        "name": fake.word(),
        "category": random.choice(["Electronics", "Clothing", "Books"]),
        "price": round(random.uniform(10.0, 100.0), 2),
        "availability": random.choice([True, False])
    }