from django.test import TestCase
from django.urls import reverse

from taxi.models import Manufacturer, Driver, Car


class ManufacturerTest(TestCase):
    def test_model_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="test")
        self.assertEqual(
            str(manufacturer),
            f"{manufacturer.name} {manufacturer.country}"
        )


class DriverTest(TestCase):
    def test_model_driver_str(self):
        driver = Driver.objects.create(username="test")
        self.assertEqual(
            str(driver),
            f"{driver.username} ({driver.first_name} {driver.last_name})"
        )

    def test_driver_get_absolute_url(self):
        driver = Driver.objects.create(username="test")
        self.assertEqual(
            driver.get_absolute_url(),
            reverse("taxi:driver-detail", kwargs={"pk": driver.pk})
        )


class CarTest(TestCase):
    def test_model_car_str(self):
        manufacturer = Manufacturer.objects.create(name="VW", country="Germany")
        car = Car.objects.create(model="test", manufacturer=manufacturer)
        self.assertEqual(
            str(car),
            f"{car.model}"
        )
