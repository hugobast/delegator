from unittest import TestCase
from .delegate import SimpleDelegator


class Parent(object):
    def __init__(self, first_name, last_name, title):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title

    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Delegated(Parent):

    def greeting(self):
        return "Hello, I am {0} {1}".format(self.title, self.full_name())


class TestsSimpleDelegator(TestCase):

    def setUp(self):
        self.delegated = Delegated("Hugo", "Bastien", "Mr.")
        self.delegator = SimpleDelegator(self.delegated)

    def test_acts_as_the_real_object_with_attributes(self):
        self.assertEqual(self.delegator.first_name, self.delegated.first_name)

    def test_acts_as_the_real_object_with_callables(self):
        self.assertEqual(self.delegator.full_name(), self.delegated.full_name())

    def test_acts_as_the_real_object_with_callables_on_concreate(self):
        self.assertEqual(self.delegator.greeting(), self.delegated.greeting())
