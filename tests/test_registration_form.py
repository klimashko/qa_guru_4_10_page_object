from selene import have

from qa_guru_4_10_page_object.data.users import User
from qa_guru_4_10_page_object.pages.registration_page import RegistrationPage


def test_reg_form():
    registration_page = RegistrationPage()
    student = User(first_name='John', last_name='Smith', email='name@example.com',
                   gender='Male', mobile='9079079079', year_of_birth='1986',
                   month_of_birth='June',
                   day_of_birth='15', subject='Computer Science', hobby='Reading',
                   picture='resources/foto.jpg', address='1478 Custer Street',
                   state='NCR', city='Delhi')

    registration_page.open()

    # WHEN
    registration_page.register(student)

    # THEN
    registration_page.should_have_registered.should(
        have.exact_texts(
            'John Smith',
            'name@example.com',
            'Male',
            '9079079079',
            '15 June,1986',
            'Computer Science',
            'Reading',
            'foto.jpg',
            '1478 Custer Street',
            'NCR Delhi',
        )
    )
