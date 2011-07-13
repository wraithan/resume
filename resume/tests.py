"""Test suite for interested companies."""


from unittest import TestCase

from your import Company


class CompanyTestCase(TestCase):

    def setUp(self):
        self.company = Company()

    def tearDown(self):
        del self.company
