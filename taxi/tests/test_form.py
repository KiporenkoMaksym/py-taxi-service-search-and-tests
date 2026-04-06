from django.test import TestCase

from taxi.forms import DriverCreationForm, validate_license_number, DriverLicenseUpdateForm, DriverUsernameSearch, \
    CarModelSearchForm
from taxi.models import Driver


class FormsTest(TestCase):
    def test_driver_creation_forms(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "license_number": "ABC12345",
            "first_name": "Test first",
            "last_name": "Test last",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

        self.assertEqual(form.cleaned_data["username"], form_data["username"])
        self.assertEqual(form.cleaned_data["license_number"], form_data["license_number"])
        self.assertEqual(form.cleaned_data["first_name"], form_data["first_name"])
        self.assertEqual(form.cleaned_data["last_name"], form_data["last_name"])

    def test_validate_license_number_valid(self):
        license_number = "ABC12345"
        result = validate_license_number(license_number)

        self.assertEqual(result, license_number)

    def test_license_update_valid(self):
        driver = Driver.objects.create_user(
            username="test",
            password="12345",
            license_number="ABC12345"
        )

        form = DriverLicenseUpdateForm(
            instance=driver,
            data={"license_number": "XYZ67890"}
        )

        self.assertTrue(form.is_valid())

    def test_driver_search_form(self):
        form = DriverUsernameSearch(data={"username": "test"})
        self.assertTrue(form.is_valid())

    def test_empty_search_form(self):
        form = DriverUsernameSearch(data={})
        self.assertTrue(form.is_valid())
