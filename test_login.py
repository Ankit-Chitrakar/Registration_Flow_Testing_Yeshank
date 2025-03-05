import time

import pytest

from conftest import fill_login_details
from data.configuration import Configuration
from pageobjects.login_page_actions import LoginPageActions
from pageobjects.registration_page_actions import RegistrationPageActions
import logging

log = logging.getLogger(__name__)

class TestLogin:

    @pytest.mark.run(order=1)
    @pytest.mark.login
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
    @pytest.mark.login
    def test_02_successful_login(self, fill_login_details):
        try:
            self.driver = fill_login_details
            signin = LoginPageActions(driver=self.driver)
            signin.do_signin()

            # check there are any errors present or not
            has_errors, error_message = signin.check_login_errors()
            if not has_errors:
                log.info("Login successful!!")
                print("Login successful!!")
            else:
                print(f"Login failed due to errors :- {error_message}")
                raise AssertionError(f"Please provide all correct details to run testcase :- Successful Login")

        except Exception as err:
            raise AssertionError(f"Error occurred: {err}")
        finally:
            self.driver.quit()

    @pytest.mark.run(order=3)
    @pytest.mark.login
    def test_03_login_with_wrong_credential(self, login_invalid_credentials):
        try:
            self.driver = login_invalid_credentials
            signin = LoginPageActions(self.driver)
            signin.do_signin()

            # check there are any errors present or not
            has_errors, error_message = signin.check_login_errors()
            if has_errors:
                log.info("Invalid email or password")
                print("Invalid email or password")
            else:
                print(f"Login successful")
                raise AssertionError(f"Please provide all correct details to run testcase :- Login With Wrong Credentials")

        except Exception as e:
            raise AssertionError(f"Error occurred: {e}")
        finally:
            self.driver.quit()


    @pytest.mark.run(order=4)
    @pytest.mark.login
    def test_04_missing_required_fields(self, skip_login_details):
        try:
            self.driver = skip_login_details
            signin = LoginPageActions(self.driver)
            signin.do_signin()

            has_blank_fields = signin.detection_skip_fields()

            if has_blank_fields:
                log.error("Email-id, Password fields are required")
                print("Email-id, Password fields are required")
            else:
                raise AssertionError(
                    "Please skip email and password to run testcase :- Detect Required Fields")

        except Exception as e:
            raise AssertionError(f"Error occurred: {e}")
        finally:
            self.driver.quit()

    @pytest.mark.run(order=5)
    @pytest.mark.login
    def test_05_redirect_to_registration_page(self, chrome_driver):
        try:
            self.driver = chrome_driver(Configuration.web_url + Configuration.login_endpoint)
            signin = LoginPageActions(self.driver)

            signin.redirect_to_registration_page()

            time.sleep(2)

            if self.driver.current_url == Configuration.web_url+Configuration.registration_endpoint:
                log.error("Successfully Redirected to Registration Page")
                print("Successfully Redirected to Registration Page")
            else:
                raise AssertionError(
                    "Please check configuration to run testcase :- Redirect to Registration Page")

        except Exception as e:
            raise AssertionError(f"Error occurred: {e}")
        finally:
            self.driver.quit()

    @pytest.mark.run(order=5)
    @pytest.mark.login
    def test_06_redirect_to_forget_password_page(self, chrome_driver):
        try:
            self.driver = chrome_driver(Configuration.web_url + Configuration.login_endpoint)
            signin = LoginPageActions(self.driver)

            signin.redirect_to_forget_password_page()

            time.sleep(2)

            if self.driver.current_url == Configuration.web_url + Configuration.forget_password_endpoint:
                log.error("Successfully Redirected to Forget Password Page")
                print("Successfully Redirected to Forget Password  Page")
            else:
                raise AssertionError(
                    "Please check configuration to run testcase :- Redirect to Forget Password Page")

        except Exception as e:
            raise AssertionError(f"Error occurred: {e}")
        finally:
            self.driver.quit()

