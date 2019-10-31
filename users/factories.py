import factory

from . import models

DEFAULT_PASSWORD = 'default-password'

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    username = factory.Sequence(lambda i: "username{}".format(i))
