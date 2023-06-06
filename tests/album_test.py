import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
        
        def setUp(self):
            self.album = Album("Science Fiction")

        def test_album_has_name(self):
              self.assertEqual("Science Fiction", self.album.album_name)