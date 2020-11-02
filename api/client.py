import json
import requests


class ProductsClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_categories(self) -> list:
        response = requests.get(self.base_url + "/api/cats/")

        if response.status_code == 200:
            categories = json.loads(response.text)
            return categories
        else:
            print(response.text)
            return []

    def get_category(self, category_id):
        response = requests.get(self.base_url + f"/api/cats/{category_id}/")

        if response.status_code == 200:
            category = json.loads(response.text)
            return category
        else:
            print(response.text)
            return None

    def delete_category(self, category_id) -> bool:
        response = requests.delete(self.base_url + f"/api/cats/{category_id}/")
        if response.status_code == 204:
            return True
        else:
            print(response.text)
            return False

    def create_category(self, name, description):
        body = {
            "name": name,
            "description": description
        }
        response = requests.post(self.base_url + "/api/cats/", json=body)

        if response.status_code == 201:
            category = json.loads(response.text)
            return category
        else:
            return None


        # task 3:
        # 1. Создать ViewSet для продуктов
        # 2. Создать метод get_products в классе ProductsClient
