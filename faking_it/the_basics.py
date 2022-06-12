# what is faker
# see https://faker.readthedocs.io/en/stable/index.html
from faker import Faker

# Faker.seed(0)  # get to deterministic builds

fake = Faker()

# the basics - faking variables
# print(fake.boolean(chance_of_getting_true=20))

# print(fake.pyint())

# beyond the basics - providers
# print(f"{fake.building_number()} {fake.street_name()}")

# Realistic but fake data
# for _ in range(5):
#     print(fake.country_code(representation="alpha-3"))

# for _ in range(5):
#     print(fake.random.choice(["USA", "CAN", "MEX"]))

# Fake Data
# for _ in range(5):
#     print(fake.pystr(min_chars=3, max_chars=3))

# putting this together - multiple providers
# patients = []

# for _ in range(10):
#     patients.append({
#         "name": {
#             "given": fake.first_name(),
#             "surname": fake.last_name(),
#         },
#         "demographics": {
#             "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=122).isoformat(),
#         },
#         "occupation": fake.job(),
#         "location": {
#             "latitude": float(fake.latitude()),
#             "longitude": float(fake.longitude()),
#         }
#     })

# speed of operation
# from datetime import date, datetime

# start = datetime.utcnow()

# for _ in range(10_000):
#     patients.append(
#         {
#             "name": {
#                 "given": fake.first_name(),
#                 "surname": fake.last_name(),
#             },
#             "demographics": {
#                 "birth_date": fake.date_of_birth(
#                     minimum_age=18, maximum_age=122
#                 ).isoformat(),
#             },
#             "occupation": fake.job(),
#             "location": {
#                 "latitude": float(fake.latitude()),
#                 "longitude": float(fake.longitude()),
#             },
#         }
#     )

# end = datetime.utcnow()

# print(f"Created {len(patients)} patients in {str(end - start)}")

# realistic but fake data

# print(fake.credit_card_number(card_type="amex"))

# for _ in range(10):
#     is_mastercard_or_visa = fake.boolean(chance_of_getting_true=80)

#     if is_mastercard_or_visa:
#         card_type = fake.random.choice(["mastercard", "visa"])
#     else:
#         card_type = "amex"

#     print(f"{card_type} is {fake.credit_card_number(card_type=card_type)}")

# print(fake.profile())

file_data = fake.image(size=(256, 256), image_format="png", hue=None, luminosity=None)

with open("./picture.png", "w") as f:
    f.write(str(file_data))
