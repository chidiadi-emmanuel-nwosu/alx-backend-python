#!/usr/bin/env python3
""" unittest for utils
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock

client = __import__('client')


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


if __name__ == "__main__":
    unittest.main()
