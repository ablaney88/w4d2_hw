import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
        def setUp(self):
            self.artist = Artist("Brand New")

        def test_artist_has_name(self):
              self.assertEqual("Brand New", self.artist.artist_name)