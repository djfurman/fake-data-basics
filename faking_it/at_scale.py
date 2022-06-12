from datetime import datetime

import pandas as pd
from faker import Faker

fake = Faker()


def parquet_write(fake_data: list) -> None:
    now = datetime.utcnow().date()

    df = pd.DataFrame(fake_data)

    df.to_parquet(
        path=f"fake-records-{now.isoformat()}.snappy.parquet",
        compression="snappy",
        engine="pyarrow",
    )


def make_fake_records(how_many: int) -> list:
    records = []

    for _ in range(how_many):
        records.append(
            {
                "name": {
                    "given": fake.first_name(),
                    "surname": fake.last_name(),
                },
                "demographics": {
                    "birth_date": fake.date_of_birth(
                        minimum_age=18, maximum_age=122
                    ).isoformat(),
                },
                "occupation": fake.job(),
                "location": {
                    "latitude": float(fake.latitude()),
                    "longitude": float(fake.longitude()),
                },
            }
        )

    return records


def main() -> None:
    # generate a list of fake records
    fake_stuff = make_fake_records(10_000)

    parquet_write(fake_stuff)

    print("complete")


if __name__ == "__main__":
    main()
