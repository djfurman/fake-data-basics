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


def main() -> None:
    # generate a list of fake records
    records = [{"some": "data"}]

    parquet_write(records)

    print("complete")


if __name__ == "__main__":
    main()
