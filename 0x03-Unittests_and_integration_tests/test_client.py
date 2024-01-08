#!/usr/bin/env python3
""" unittest for utils
"""
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock

client = __import__('client')
TEST_PAYLOAD = __import__('fixtures').TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ test cases for client
    """

    @parameterized.expand([('google',), ('abc',)])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: MagicMock) -> None:
        """ test org fn
        """
        instance = client.GithubOrgClient(org_name)
        expected_url = instance.ORG_URL.format(org=instance._org_name)
        instance.org()
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self) -> None:
        """ test _public_repos_url fn
        """
        known_payload = {
                "repos_url": "https://api.github.com/repos/example"
                }
        with patch.object(client.GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = known_payload
            instance = client.GithubOrgClient('example')
            result = instance._public_repos_url

            self.assertEqual(result, known_payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """ test_public_repos
        """
        payload = {
            "repos_url": "https://api.github.com/repos/example",
            "repos": [{"name": "repo1"}, {"name": "repo2"}]
            }
        mock_get_json.return_value = payload['repos']

        with patch.object(
                client.GithubOrgClient,
                '_public_repos_url',
                return_value=payload['repos_url'],
                new_callable=PropertyMock
                ) as mock_public_repos_url:
            instance = client.GithubOrgClient('example')
            repos = instance.public_repos()

            self.assertEqual(repos, ["repo1", "repo2"])
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, result) -> None:
        """ test_has_license
        """
        _result = client.GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, _result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            client.GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            client.GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
