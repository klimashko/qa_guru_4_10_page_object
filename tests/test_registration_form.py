from selene.support.shared import browser
from selene import have, by, be
from selene import command
import os
import tests
from tests import resources


def test_reg_form():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__]').with_(
        timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    # WHEN
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Smith')

    browser.element('#userEmail').type('name@example.com')

    browser.all('[name=gender]').element_by(have.value('Male')).element(
        '..').click()

    browser.element('#userNumber').type('9079079079')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('June')
    browser.element('.react-datepicker__year-select').type('1986')
    browser.element(f'.react-datepicker__day--0{15}').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()

    browser.element('[for=hobbies-checkbox-2]').perform(
        command.js.scroll_into_view)
    browser.element('[for=hobbies-checkbox-2]').click()


    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/foto.jpg')
        )
    )

    browser.element('#currentAddress').type('1478 Custer Street')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('NCR')
    ).click()


    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Delhi')
    ).click()


    browser.element('#submit').perform(command.js.click)
    '''

    # THEN
    '''
    # can be considered as additional check:
    browser.element('[id=example-modal-sizes-title-lg]').should(be.visible)
    # OR (if you allow yourself to check app texts)
    browser.element('[id=example-modal-sizes-title-lg]').should(
        have.text('Thanks for submitting the form')
    )

    browser.element('.table').all('td').even.should(
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
