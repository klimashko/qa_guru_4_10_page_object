import dataclasses


@dataclasses.dataclass
class User:
    first_name: str

    last_name: str

    email: str

    gender: str

    mobile: str

    year_of_birth: str

    month_of_birth: str

    day_of_birth: str

    # ('1986', 'June', '15')
    subject: str

    hobby: str

    picture: str

    address: str

    state: str

    city: str

