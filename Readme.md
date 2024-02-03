# Ecommerce API collection

This repository contains two APIs built with FastAPI and MongoDB.
	-First API returns product listings
	-Second API accecpts product orders


## Installation

1. Clone the repository:
    ```
    git clone https://github.com/shaunaksb/ecommerceapi.git
    ```

2. Navigate to the project directory:
    ```
    cd ecommerceapi
    ```

3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, use the following command:

```
uvicorn listing:app --port 8000 --reload
uvicorn orders:app --port 8001 --reload
```


# Listing API

This API returns a list of products stored in a MongoDB collection according to the constraints provided in the request.

## Endpoints

### GET /products/

Retrieves all products from the MongoDB collection.

#### Request

```bash
curl -X GET http://127.0.0.1:8000/products/
```

#### Response

Returns a list of all products and pagination information.

```json
{
  "data": [
    {
      "_id": "65be645dc9b6e43c8f7983cf",
      "name": "Samsung Galaxy S21",
      "price": 10,
      "quantity": 5
    },
    {
      "_id": "65be645dc9b6e43c8f7983d0",
      "name": "Sony PlayStation 5",
      "price": 20,
      "quantity": 10
    },
    {
      "_id": "65be645dc9b6e43c8f7983d1",
      "name": "Microsoft Xbox Series X",
      "price": 30,
      "quantity": 15
    },
    {
      "_id": "65be645dc9b6e43c8f7983d2",
      "name": "Apple MacBook Pro",
      "price": 40,
      "quantity": 20
    }
  ],
  "page": {
    "limit": 10,
    "nextOffset": null,
    "prevOffset": null,
    "total": 4
  }
}
```

### GET /products/?limit=20

Retrieves the amount of products specified in the request from the MongoDB collection.

#### Request

```bash
curl -X GET 'http://127.0.0.1:8000/products/?limit=20'
```

### GET /products/?limit=20&offset=20

Retrieves the amount of products specified in the request from the MongoDB collection, starting from the product which comes after the last product of the previous response.

#### Request

```bash
curl -X GET 'http://127.0.0.1:8000/products/?limit=20&offset=20'
```

### GET /products/?min_price=10

Retrieves all products from the MongoDB collection with a price greater than or equal to specified min_price.

#### Request

```bash
curl -X GET 'http://127.0.0.1:8000/products/?min_price=10'
```

### GET /products/?max_price=40

Retrieves all products from the MongoDB collection with a price less than or equal to specified max_price.

#### Request

```bash
curl -X GET 'http://127.0.0.1:8000/products/?max_price=40'
```

### GET /products/?min_price=10&max_price=40

Retrieves all products from the MongoDB collection with a price between specified min_price and max_price (inclusive).

#### Request

```bash
curl -X GET 'http://127.0.0.1:8000/products/?min_price=10&max_price=40'
```

## API Call Parameters

- `limit`: This parameter is used to limit the number of products returned in the response. For example, `limit=20` will return only the first 20 products.

- `offset`: This parameter is used in conjunction with `limit` to implement pagination. For example, `limit=20&offset=20` will return 20 products, starting from the 21st product.

- `min_price`: This parameter is used to filter the products by their price. `min_price=10` will return only the products with a price of 10 or more.

- `max_price`: This parameter is also used to filter the products by their price. `max_price=40` will return only the products with a price of 40 or less.

## Response Parameters

- `data`: This is an array of product objects. Each object contains the following properties:
  - `_id`: The unique identifier of the product in the MongoDB collection.
  - `name`: The name of the product.
  - `price`: The price of the product.
  - `quantity`: The quantity of the product available.

- `page`: This is an object that contains pagination information:
  - `limit`: The number of products returned in the current page.
  - `nextOffset`: The offset for the next page of products. If there are no more products, this will be `null`.
  - `prevOffset`: The offset for the previous page of products. If this is the first page, this will be `null`.
  - `total`: The total number of products in the MongoDB collection.


# Create Order API

This API places orders for an ecommerce application built with FastAPI and MongoDB.

## Installation

### Create Order

**URL:** `/orders/`

**Method:** `POST`

**Request Parameters:**

- `items`: A list of items that the user is ordering. Each item in this list is an object with the following properties:
  - `productId`: The unique identifier of the product that the user is ordering.
  - `boughtQuantity`: The quantity of the product that the user is ordering.
- `totalAmount`: The total cost of the order. It should be the sum of the cost of all items in the order.
- `userAddress`: An object containing the user's address. It has the following properties:
  - `city`: The city where the user lives.
  - `country`: The country where the user lives.
  - `zipCode`: The zip code of the user's address.

**Request Body:**

```json
{
  "items": [
    {
      "productId": "65be645dc9b6e43c8f7983d4",
      "boughtQuantity": 1
    }
  ],
  "totalAmount": 1,
  "userAddress": {
    "city": "Nagpur",
    "country": "India",
    "zipCode": "440010"
  }
}
```

**Response Parameters:**

- `_id`: The unique identifier of the order. It is automatically generated by MongoDB when the order is inserted into the database.
- `items`: The list of items that the user ordered. It is the same as the `items` field in the request.
- `totalAmount`: The total cost of the order. It is the same as the `totalAmount` field in the request.
- `userAddress`: The user's address. It is the same as the `userAddress` field in the request.
- `createdOn`: The date and time when the order was created. It is automatically set to the current date and time when the order is inserted into the database.

**Response:**

```json
{
  "_id": "65be6c4afc6ea551ac6f4892",
  "items": [
    {
      "productId": "65be645dc9b6e43c8f7983d4",
      "boughtQuantity": 1
    }
  ],
  "totalAmount": 1.0,
  "userAddress": {
    "city": "Nagpur",
    "country": "India",
    "zipCode": "440010"
  },
  "createdOn": "2024-02-03T22:09:38.168000"
}