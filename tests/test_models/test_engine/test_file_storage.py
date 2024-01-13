"""
doc
"""
import unittest
from models import storage
import json
from models.user import User
import os
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    storage = FileStorage()

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_save(self):
        """
        doc
        """
        inst = User()
        inst.first_name = "jordan"
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """
        doc
        """
        if os.path.exists("file.json"):
            os.remove("file.json")
            self.storage._FileStorage__objects.clear()
        inst = User()
        inst.last_name = "Nguepi"
        self.storage.save()
        with open("file.json") as f:
            data = json.load(f)
        self.assertTrue(len(data) == len(self.storage.all()))

    def test___file_path(self):
        """
        doc
        """
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))

    def test_new(self):
        """test when new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
