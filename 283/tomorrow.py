from datetime import date, timedelta


def tomorrow(date_today=None):
    # Your code goes here
    return (date_today if date_today else date.today()) + timedelta(days=1)


if __name__ == "__main__":
    print(tomorrow())
