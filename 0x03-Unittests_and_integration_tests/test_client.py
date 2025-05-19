#!/usr/bin/env python3
""" Tests for `client` module
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Unittest class for `GithubOrgClient` class
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"abc": "abc"}),
        ])
    @patch("client.get_json")
    def test_org(self, org, expected_value, mock_get_json):
        """ Testing that `org` returns expected value
        """
        mock_get_json.return_value = expected_value

        client = GithubOrgClient(org)
        result = client.org

        self.assertEqual(result, expected_value)
        mock_get_json.assert_called_once_with(client.ORG_URL.format(org=org))

    def test_public_repos_url(self):
        """ Test `_public_repos_url`
        """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                    "repos_url": "https://api.github.com/orgs/google/repos",
                    }

            client = GithubOrgClient("google")
            result = client._public_repos_url

            self.assertEqual(result, mock_org.return_value["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """ Test `public_repos`
        """

        test_payload = [
                {"name": "repo1"},
                {"name": "repo2"},
                {"name": "repo3"},
                ]
        mock_get_json.return_value = test_payload
        test_url = "https://api.github.com/orgs/org/repos"
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_url

            self.assertEqual(
                    GithubOrgClient("org").public_repos(),
                    ["repo1", "repo2", "repo3"],
                    )

            mock_get_json.assert_called_once_with(test_url)
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected):
        """ Test `has_license`
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
        },
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test class for `public_repos`
    """
    @classmethod
    def setUpClass(cls):
        """ Set up class method for `TestIntegrationGithubOrgClient` class
        """
        route_payload = {
                "https://api.github.com/orgs/google": cls.org_payload,
                "https://api.github.com/orgs/google/repos": cls.repos_payload,
                }

        def side_effect(url):
            if url in route_payload:
                return Mock(**{"json.return_value": route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=side_effect)
        cls.get_patcher.start()

    def test_public_repos(self):
        """
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        """
        client = GithubOrgClient("google")
        self.assertEqual(
                client.public_repos(license="apache-2.0"),
                self.apache2_repos
                )

    @classmethod
    def tearDownClass(cls):
        """ Tear down class method for `TestIntegrationGithubOrgClient` class
        """
        cls.get_patcher.stop()
