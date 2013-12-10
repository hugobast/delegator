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

    def test_can_use_its_own_callables(self):
        self.assertEqual(self.delegator.greeting(), self.delegated.greeting())

    def test_acts_as_the_real_object_with_set_attributes(self):
        self.delegator.first_name = "John"
        self.assertEqual(self.delegator.first_name, self.delegated.first_name)


class FrameworkObject(object):
    text_field_title = "Title"
    text_field_fname = "First Name"
    text_field_lname = "Last Name"


class FrameworkObjectProxy(SimpleDelegator):
    category = "Person"

    def shout(self):
        return "I am the {}!".format(self.text_field_title.upper())

    def define(self):
        return "{0}, is a {1}.".format(self.text_field_fname, self.category)


class TestsInheritedSimpleDelegator(TestCase):

    def setUp(self):
        self.model = FrameworkObject()
        self.model_proxy = FrameworkObjectProxy(self.model)

    def test_can_check_attributes_on_delegated_model(self):
        self.assertEqual(self.model_proxy.text_field_fname, "First Name")

    def test_can_exec_callables_on_delegated_model(self):
        self.assertEqual(self.model_proxy.shout(), "I am the TITLE!")

    def test_can_exec_callables_on_itself(self):
        self.assertEqual(self.model_proxy.define(), "First Name, is a Person.")
