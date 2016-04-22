from quicksearch.search_engines import engines, get_config
from validators.url import url
from quicksearch.launch import open
import mock
import unittest


class TestSearchEngines(unittest.TestCase):
    def setUp(self):
        self.engines = {k: get_config(k) for k in engines}

    def test_proper_url(self):
        for engine, config in self.engines.items():
            for option in config:
                self.assertTrue(url(config[option]), 'proper url for engine {0} option {1}'.format(engine, option))

    def test_url_uses_parameter(self):
        for engine, config in self.engines.items():
            for option in config:
                self.assertIn('test-phrase', config[option].format('test-phrase'))


class TestLauncher(unittest.TestCase):
    def test_launch_win(self):
        with mock.patch('quicksearch.launch.os') as os_mocked:
            os_mocked.startfile = mock.MagicMock()
            with mock.patch('quicksearch.launch.sys.platform', 'win32'):
                open('http://example.com/')
                os_mocked.startfile.assert_called_once_with('http://example.com/')

    def test_launch_darwin(self):
        with mock.patch('quicksearch.launch.subprocess') as subprocess_mocked:
            subprocess_mocked.Popen = mock.MagicMock()
            with mock.patch('quicksearch.launch.sys.platform', 'darwin'):
                open('http://example.com/')
                subprocess_mocked.Popen.assert_called_once_with(['open', 'http://example.com/'])


if __name__ == '__main__':
    unittest.main()
