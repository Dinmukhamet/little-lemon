from restaurant.models import Menu
import pytest

pytestmark = pytest.mark.django_db


def test_get_item():
    item = Menu.objects.create(title="IceCream", price=80, inventory=100)
    assert str(item) == "IceCream : 80"
