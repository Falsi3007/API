import requests
import pandas as pd

# *****Products********
#get all products
# url = "https://fakestoreapi.com/products"
# response = requests.get(url)
# print(response.json())


#get a single product
# url = "https://fakestoreapi.com/products/1"
# response = requests.get(url)
# print(response.json())


#limit result
# url = "https://fakestoreapi.com/products?limit=5"
# response = requests.get(url)
# print(response.json())


#sort result 
# url = "https://fakestoreapi.com/products?sort=desc"
# response = requests.get(url)
# print(response.json())


#get all categories
# url = "https://fakestoreapi.com/products/categories"
# response = requests.get(url)
# print(response.json())


#get a specific category
# url = "https://fakestoreapi.com/products/category/jewelery"
# response = requests.get(url)
# print(response.json())


# add a new product 
# url = "https://fakestoreapi.com/products"
# payload = {
#             "title": 'test product',
#             "price": 13.5,
#             "description": 'lorem ipsum set',
#             "image": 'https://i.pravatar.cc',
#             "category": 'electronic'
#         }
# response = requests.post(url, json=payload)
# print(response.json())


#update a product
# url = "https://fakestoreapi.com/products/7"
# payload = {
#             "title": 'test product',
#             "price": 13.5,
#             "description": 'lorem ipsum set',
#             "image": 'https://i.pravatar.cc',
#             "category": 'electronic'
#         }
# response = requests.put(url, json=payload)
# print(response.json())


#delete a product 
# url = "https://fakestoreapi.com/products/6"
# response = requests.delete(url)
# print(response.json())



# *******cart*******
#get all carts
# url = "https://fakestoreapi.com/carts"
# response = requests.get(url)
# print(response.json())


#get a single cart
# url = "https://fakestoreapi.com/carts/5"
# response = requests.get(url)
# df = pd.DataFrame(response.json())
# print(df)

#get a new product 
# url = "https://fakestoreapi.com/carts"
# payload = {
#     "userId":5,
#     "date":"2020-02-03",
#     "products":[{"productId":5,"quantity":1},{"productId":1,"quantity":5}]
# }
# response = requests.post(url, json=payload)
# print(response.json())



#user login 
# url = "https://fakestoreapi.com/auth/login"
# payload = {
#     "username": "mor_2314",
#     "password": "83r5^_"
# }
# response = requests.post(url, json=payload)     
# print(response.json())

 

base_url = "https://jsonplaceholder.typicode.com/todos"
def fetch_todo(todo_id):
    url = f"{base_url}/{todo_id}"  # Dynamically inserting the ID
    response = requests.get(url)
    print(response.json())
    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     return f"Error: {response.status_code}"
# Example usage
todo_id = 2  # Change this to any ID
data = fetch_todo(todo_id)
# print(data)
