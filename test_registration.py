import time

import pytest
import logging

from data.configuration import Configuration
from pageobjects.registration_page_actions import RegistrationPageActions
from utilities.email_utils import EmailUtils

log = logging.getLogger(__name__)


class TestRegistration:

    @pytest.mark.run(order=1)
    @pytest.mark.registration
    def test_01_successful_registration(self, fill_registration_details):
        try:
            self.driver = fill_registration_details
            reg = RegistrationPageActions(driver=self.driver)

            log.info("Registration page opens")
            print("Registration opens")
            reg.do_signup()

            # check there are any errors present or not
            has_errors, error_message = reg.check_registration_errors()
            if not has_errors:
                log.info("Registration successful!!")
                print("Registration successful!!")

                print("Opens Login Page")

            else:
                print(f"Registration failed due to errors :- {error_message}")
                raise AssertionError(f"Please provide all correct details to run testcase :- Successful Registration")


        except Exception as err:
            raise AssertionError(f"Error occurred: {err}")
        finally:
            self.driver.quit()

    @pytest.mark.run(order=2)
    @pytest.mark.registration
    def test_02_register_using_existing_email(self, fill_registration_details):
        try:
            self.driver = fill_registration_details
            reg = RegistrationPageActions(self.driver)

            existing_email = EmailUtils.get_next_email()
            reg.fill_email(existing_email)
            reg.do_signup()

            has_errors, error_message = reg.check_registration_errors()
            if has_errors and error_message.lower() == "A customer with this email address already exists.".lower():
                log.error(f"Oops!! registration unsuccessful :- {error_message}")
                print(f"Oops!! Registration Unsuccessful :- 'Email already in use'")
            else:
                raise AssertionError("Please provide a existing email to run testcase :- Existing Email-id Detection")

        except Exception as err:
            raise AssertionError(f"Error occurred: {err}")
        finally:
            self.driver.quit()

    @pytest.mark.run(order=3)
    @pytest.mark.registration
    def test_03_weak_password_detection(self, fill_registration_details):
        try:
            self.driver = fill_registration_details
            reg = RegistrationPageActions(self.driver)

            reg.fill_password(Configuration.weak_password)
            reg.do_signup()

            has_weak_password = reg.detect_weak_password()

            if has_weak_password:
                log.error("Password must contain at least 8 characters, including letters and numbers.")
                print("Password must contain at least 8 characters, including letters and numbers.")
            else:
                raise AssertionError("Please provide a weak password to run testcase :- Detect Weak Password")

        except Exception as err:
            raise AssertionError(f"Error occurred: {err}")
        finally:
            self.driver.quit()

    @pytest.mark.run(order=4)
    @pytest.mark.registration
    def test_04_missing_required_fields(self, skip_registration_details):
        try:
            self.driver = skip_registration_details
            reg = RegistrationPageActions(self.driver)

            reg.do_signup()

            has_blank_fields = reg.detection_skip_fields()

            if has_blank_fields:
                log.error("Firstname, Lastname, Email-id, Password all of this fields are required")
                print("Firstname, Lastname, Email-id, Password all of this fields are required")
            else:
                raise AssertionError("Please skip username, email and password to run testcase :- Detect Required Fields")
        except Exception as err:
            raise AssertionError(f"Error occurred: {err}")
        finally:
            self.driver.quit()

    @pytest.mark.run(order=5)
    @pytest.mark.registration
    def test_05_invalid_imail_format(self, check_for_invalid_email ):
        try:
            self.driver = check_for_invalid_email
            reg = RegistrationPageActions(self.driver)

            reg.do_signup()

            has_invalid_email = reg.check_email_validity(Configuration.invalid_email)

            if not has_invalid_email:
                log.error("Please enter a valid email address.")
                print("Please enter a valid email address.")
            else:
                raise AssertionError("Please enter a invalid email to run testcase :- Invalid Email Format")

        except Exception as err:
            raise AssertionError(f"Error occurred: {err}")
        finally:
            self.driver.quit()

