from selene import have

from qa_guru_4_10_page_object.data.users import User
from qa_guru_4_10_page_object.pages.registration_page import RegistrationPage


def test_reg_form():
    registration_page = RegistrationPage()
    student = User(first_name='John', last_name='Smith', email='name@example.com',
    gender='Male', mobile='9079079079', year_of_birth='1986', month_of_birth='June',
    day_of_birth='15', subject='Computer Science', hobby='Reading',
    picture='resources/foto.jpg', address='1478 Custer Street', state='NCR', city='Delhi')

    registration_page.open()

    # WHEN

    registration_page.fill_first_name(student.first_name)

    registration_page.fill_last_name(student.last_name)

    registration_page.fill_email(student.email)

    registration_page.fill_gender(student.gender)

    registration_page.fill_mobile(student.mobile)

    registration_page.fill_date_of_birth(student.year_of_birth, student.month_of_birth, student.day_of_birth)

    registration_page.fill_subject(student.subject)

    registration_page.fill_hobby(student.hobby)

    registration_page.fill_picture(student.picture)

    registration_page.fill_address(student.address)

    registration_page.fill_state(student.state)

    registration_page.fill_city(student.city)

    registration_page.submit_data

    # THEN

    registration_page.assert_table_display

    registration_page.registered_user_data.should(
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

