import logging

from pageobjects.base_page import BasePage
from locators.login_page import LoginPage
from utilities.wait_utils import WaitUtils

log = logging.getLogger(__name__)

class LoginPageActions(BasePage):
    def fill_email(self, email):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.email_locator)
        element.clear()
        element.send_keys(email)

    def fill_password(self, password):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.password_locator)
        element.clear()
        element.send_keys(password)

    def view_password(self):
        element = WaitUtils.wait_for_clickable(self.driver, LoginPage.eye_button_locator)
        element.click()

    def do_signin(self):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.login_button_locator)
        element.click()

    def redirect_to_registration_page(self):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.registration_page_locator)
        element.click()

    def redirect_to_forget_password_page(self):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.forget_password_page_locator)
        element.click()

    def skip_email(self):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.email_locator)
        element.clear()

    def skip_password(self):
        element = WaitUtils.wait_for_element(self.driver, LoginPage.password_locator)
        element.clear()

    def check_login_errors(self):
        try:
            error_block = WaitUtils.wait_for_element(self.driver, LoginPage.login_error_locator,timeout=5)
            if error_block and error_block.text == "Invalid email or password":
                error_message = error_block.text
                log.error(f"Login Error: {error_message}")
                print(f"Login Error: {error_message}")
                return True, error_message
            else:
                return False, None
        except Exception as e:
            # Log the exception but do not raise it to allow the test to continue
            log.warning(f"No Login errors found or element not located: {e}")
            return False, None


    def detection_skip_fields(self):
        try:
            email_element = WaitUtils.wait_for_element(self.driver, LoginPage.email_blank_locator)
            password_element = WaitUtils.wait_for_element(self.driver, LoginPage.password_blank_locator)

            if all([email_element, password_element]):
                return True
            else:
                return False

        except Exception as e:
            return False