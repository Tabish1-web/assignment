import unittest
import requests

class Test(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000"
    
    OBJ = {
        "username" : "musa100",
        "first_name" : "musa",
        "last_name" : "ali",
        "phone_no" : "03092910630"
    }
    
    SEARCH_OBJ = {
        "emails" : [],
        "first_name" : "musa",
        "last_name" : "ali",
        "phone_no" : "03092910630",
        "username" : "musa100"
    }

    def test_get_all_contact(self):
        r = requests.get(Test.API_URL)
        self.assertEqual(r.status_code,200)
        self.assertEqual(len(r.json()["contacts"]),11)

    def test_new_contact_add(self):
        r = requests.post(Test.API_URL,json=Test.OBJ)
        self.assertEqual(r.status_code,200)

    def test_search_by_username(self):
        username = "musa100"
        r = requests.get(f"{Test.API_URL}/search",params={"username":username})
        self.assertEqual(r.status_code,200)
        self.assertDictEqual(r.json(),Test.SEARCH_OBJ)

    def test_delete_contact(self):
        username = "musa100"
        r = requests.delete(f"{Test.API_URL}/{username}")
        self.assertEqual(r.status_code,200)

    def test_update_contact(self):
        username = "musa100"
        r = requests.put(f"{Test.API_URL}/{username}",json={"username":"musa302"})
        self.assertEqual(r.status_code,200)

if __name__ == "__main__":
    unittest.main()