"""Test suite for interested companies."""


from unittest import TestCase

from your import Company


class CompanyTestCase(TestCase):

    def setUp(self):
        self.company = Company()

    def test_uses_git(self):
        self.assertTrue('git' in self.company.vcs)

    def test_loves_testing(self):
        self.assertTrue(self.company.coverage > .50)

    def test_has_ci(self):
        self.assertTrue(self.company.ci)

    def test_has_cd(self):
        self.assertTrue(self.company.cd)

    def test_has_seen_the_it_crowd(self):
        self.assertTrue('it_crowd' in self.company.engineers.favorite.tv_shows)

    def tearDown(self):
        del self.company
