from api.client import ProductsClient
from config import BASE_URL


def run_app():
    client = ProductsClient(BASE_URL)

    cat = client.create_category("Овощи", "Капуста, редиска и все зеленое")
    print(cat)

    # cats = client.get_categories()
    # print(cats)
    #
    # first_cat_id = cats[0]["id"]
    #
    # success = client.delete_category(first_cat_id)
    # if success:
    #     print("Successfully deleted")
    #
    # cats = client.get_categories()
    # print(cats)


if __name__ == "__main__":
    run_app()
