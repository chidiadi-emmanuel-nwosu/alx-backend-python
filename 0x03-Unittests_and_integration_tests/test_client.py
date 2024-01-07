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
        with patch.object(client.GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = known_payload
            instance = client.GithubOrgClient('example')
            result = instance._public_repos_url

            self.assertEqual(result, known_payload['repos_url'])



if __name__ == "__main__":
    unittest.main()
