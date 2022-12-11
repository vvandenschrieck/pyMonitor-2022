from website.website import Website


def probe_mock_true(url):
    return True


def probe_mock_false(url):
    return False


class TestWebsite:
    def test_init(self):
        site = Website("Test", "www.test.com")
        assert site.status == "UNKNOWN"

    def test_probe_true(self):
        site = Website("Test", "www.test.com")
        site.add_probe(probe_mock_true)
        site.test()
        assert site.status == "OK"

    def test_probe_false(self):
        site = Website("Test", "www.test.com")
        site.add_probe(probe_mock_false)
        site.test()
        assert site.status == "KO"

    def test_multiple_probes(self):
        site = Website("Test", "www.test.com")
        site.add_probe(probe_mock_true)
        site.add_probe(probe_mock_true)
        site.test()
        assert site.status == "OK"
        site.add_probe(probe_mock_false)
        site.test()
        assert site.status == "KO"
