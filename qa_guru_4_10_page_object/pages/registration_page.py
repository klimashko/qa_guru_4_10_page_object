import os

from selene import have, command, be
from selene.support.shared import browser

import tests


class RegistrationPage:


    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(
            timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(
            command.js.remove)



    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        
    def fill_email(self, value):
        browser.element('#userEmail').type(value)


    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element(
        '..').click()

    def fill_mobile(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobby(self, value):
        browser.all('[for^=hobbies]').element_by(have.exact_text(value)).perform(
            command.js.scroll_into_view)
        browser.all('[for^=hobbies]').element_by(have.exact_text(value)).click()

    def fill_picture(self, value):
        browser.element('#uploadPicture').set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), value)
            )
        )

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)



    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    @property
    def submit_data(self):
        browser.element('#submit').perform(command.js.click)

    @property
    def assert_table_display(self):
        browser.element('[id=example-modal-sizes-title-lg]').should(be.visible)

    @property
    def registered_user_data(self):
        return browser.element('.table').all('td').even















    



