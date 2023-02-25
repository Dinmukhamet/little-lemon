import factory
from faker_food import FoodProvider

factory.faker.Faker.add_provider(FoodProvider)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "auth.User"

    username = factory.Faker("user_name")


class MenuFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "restaurant.Menu"

    title = factory.Faker("dish")
    price = factory.Faker("pydecimal", left_digits=5, right_digits=2)
    inventory = factory.Faker("pyint", min_value=1, max_value=100)


class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "restaurant.Booking"

    name = factory.Faker("first_name")
    guests_number = factory.Faker("pyint", min_value=2, max_value=8)
    booking_date = factory.Faker("date_this_year")
