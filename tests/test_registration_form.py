from selene import have
from qa_guru_4_10_page_object.pages.registration_page import RegistrationPage


def test_reg_form():
    registration_page = RegistrationPage()

    registration_page.open()

    # WHEN

    registration_page.fill_first_name('John')

    registration_page.fill_last_name('Smith')

    registration_page.fill_email('name@example.com')

    registration_page.fill_gender('Male')

    registration_page.fill_mobile('9079079079')

    registration_page.fill_date_of_birth('1986', 'June', 15)

    registration_page.fill_subject('Computer Science')

    registration_page.fill_hobby('Reading')

    registration_page.fill_picture('resources/foto.jpg')

    registration_page.fill_address('1478 Custer Street')

    registration_page.fill_state('NCR')

    registration_page.fill_city('Delhi')

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

