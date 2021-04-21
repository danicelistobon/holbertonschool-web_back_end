#!/usr/bin/env python3
""" Unittests and Integration Tests
"""
import unittest
import requests
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """ Class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """ Test that GithubOrgClient.org returns the correct value
        """
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get.return_value)
        mock_get.assert_called_once

    def test_public_repos_url(self):
        """ Method to unit-test GithubOrgClient._public_repos_url
        """
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "twitter"}) as mock_get:
            test_json = {"repos_url": "twitter"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(test_return,
                             mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "twitter"}])
    def test_public_repos(self, mock_get):
        """ Method to unit-test GithubOrgClient.public_repos
        """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("twitter")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["twitter"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_return):
        """ Method to unit-test GithubOrgClient.has_license
        """
        test_client = GithubOrgClient("twitter")
        test_return = test_client.has_license(repo, license_key)
        self.assertEqual(expected_return, test_return)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class that inherits from unittest.TestCase
    """
    @classmethod
    def setUpClass(cls):
        """ Implement the setUpClass
        """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ Implement the tearDownClass
        """
        cls.get_patcher.stop()
