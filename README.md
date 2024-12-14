# Snapmart - E-commerce Online Platform

Welcome to Snapmart, an e-commerce platform designed to simplify online shopping with efficient user authentication and seamless product management. This project demonstrates a backend API built using Django and Django REST Framework (DRF), connected to a PostgreSQL database and managed via pgAdmin4. The project includes JWT-based authentication, CRUD operations for products, categories, and stock management, and can be extended with Dockerization and hosting.

## Features

### Core Features

#### User Authentication and Registration
- User login and registration APIs with JWT-based authentication.

#### Product Management
- Models for Product, Category, and Stock with full CRUD functionality.

#### PostgreSQL Integration
- Database connection using PostgreSQL and management through pgAdmin4.

### Bonus Features

- Dockerized setup for easy deployment.
- Hosting-ready architecture.
- Flexible and scalable design to integrate a frontend.

## API Documentation

### Base URL
`https://snapmart-wzw3.onrender.com/api`

### Endpoints

#### User Authentication

**Register**
- **URL**: `/auth/register/`
- **Method**: `POST`
- **Request Body**:
  ```json
    {
    "first_name":"Md Rafiul",
    "last_name":"Islam",
     "username": "rafiul_islam",
     "password": "Rafi12234",
     "confirm_password":"Rafi12234",
     "email": "rafiul@gmail.com",
     "role":"customer"
    }
  ```
- **Response**:
  ```json
    {
        "message": "User registered successfully!"
    }
  ```

**Login**
- **URL**: `/auth/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
   "username": "rafiul_islam",
   "password": "Rafi12234"
  }
  ```
- **Response**:
  ```json
    {
        "token": "41cfd325ef211d01f2589ae506d7cf59af41cdb2",
        "user": {
            "user_id": 3,
            "username": "rafiul_islam",
            "email": "rafiul@gmail.com",
            "role": "customer"
        }
    }
  ```
**Logout**
- **URL**: `/auth/logout/`
- **Method**: `GET`
- **Response**:
  ```json
    {
        "success": "User Logout Successfull"
    }
  ```
  


#### Category Management

**List All Categories**
- **URL**: `/store/categories/`
- **Method**: `GET`
- **Response**:
  ```json
    {
        "data": [
            {
                "id": 1,
                "name": "Laptop"
            },
            {
                "id": 2,
                "name": "Mobile"
            }
        ],
        "success": "Fetch all Categories"
    }
  ```

**Create a Category**
- **URL**: `/store/categories/`
- **Method**: `POST`
- **Request Body**:
  ```json
    {
        "name": "Laptop"
    }
  ```
- **Response**:
  ```json
    {
        "data": {
            "id": 1,
            "name": "Laptop"
        },
        "success": "Category create successfully"
    }
  ```

**Retrieve a Category**
- **URL**: `/store/categories/{id}/`
- **Method**: `GET`
- **Response**:
  ```json
    {
        "data": {
            "id": 1,
            "name": "Laptop"
        },
        "success": "Fetch single Category successfully"
    }
  ```

**Update a Category**
- **URL**: `/store/categories/{id}/`
- **Method**: `PUT`
- **Request Body**:
  ```json
    {
        "name": "Laptop update"
    }
  ```
- **Response**:
  ```json
    {
        "data": {
            "id": 1,
            "name": "Laptop update"
        },
        "success": "Category Update successfully"
    }
  ```

**Update specifc any field a Category**
- **URL**: `/store/categories/{id}/`
- **Method**: `PATCH`
- **Request Body**:
  ```json
    {
        "name": "Laptop update"
    }
  ```
- **Response**:
  ```json
    {
        "data": {
            "id": 2,
            "name": "Mobile 111"
        },
        "success": "Category udated successfully"
    }
  ```

**Delete a Category**
- **URL**: `/store/categories/{id}/`
- **Method**: `DELETE`
- **Response**: 
```json
    {
        "success": "Category delete successfully."
    }
```

#### Product Management

**List All Products**
- **URL**: `/store/products/`
- **Method**: `GET`
- **Response**:
  ```json
    {
        "data": [
            {
                "id": 1,
                "category": {
                    "id": 3,
                    "name": "Laptop"
                },
                "name": "Hp Pavilion Laptop",
                "description": "this is a laptop",
                "price": "200.00"
            },
            {
                "id": 2,
                "category": {
                    "id": 2,
                    "name": "Mobile"
                },
                "name": "Realme C3",
                "description": "this is a mobile phone",
                "price": "200.00"
            }
        ],
        "success": "Fetch all Products"
    }
  ```

**Create a Product**
- **URL**: `/store/products/`
- **Method**: `POST`
- **Request Body**:
  ```json
    {
        "category_id":3,
        "name": "Hp Pavilion Laptop",
        "description": "this is a laptop",
        "price": 200
    }
  ```
- **Response**:
  ```json
    {
        "data": {
            "id": 1,
            "category": {
                "id": 3,
                "name": "Laptop"
            },
            "name": "Hp Pavilion Laptop",
            "description": "this is a laptop",
            "price": "200.00"
        },
        "success": "Product create successfully"
    }
  ```
**Update a Product All Document**
- **URL**: `/store/products/{id}/`
- **Method**: `PUT`
- **Request Body**:
  ```json
   {
        "category_id":3,
        "name": "Hp Pavilion Laptop update ",
        "description": "this is a laptop",
        "price": 200
    }
  ```
- **Response**:
  ```json
    {
        "data": {
            "id": 1,
            "category": {
                "id": 3,
                "name": "Laptop"
            },
            "name": "Hp Pavilion Laptop update ",
            "description": "this is a laptop",
            "price": "200.00"
        },
        "success": "Product Update successfully"
    }
  ```
 
 **Update a Product Any Fields**
- **URL**: `/store/products/{id}/`
- **Method**: `PATCH`
- **Request Body**:
  ```json
   {
        "description": "this is a laptop update",
        "price": 2023
    }
  ```
- **Response**:
  ```json
    {
        "data": {
            "id": 1,
            "category": {
                "id": 3,
                "name": "Laptop"
            },
            "name": "Hp Pavilion Laptop update ",
            "description": "this is a laptop update",
            "price": "2023.00"
        },
        "success": "Product udated successfully"
    }
  ```

**Delete a Product**
- **URL**: `/store/products/{id}/`
- **Method**: `DELETE`
- **Response**: 
```json
    {
        "success": "Product delete successfully."
    }
```
  
#### Stock Management

**List All Stocks**
- **URL**: `/store/stocks/`
- **Method**: `GET`
- **Response**:
  ```json
    {
        "data": [
            {
                "id": 1,
                "product": {
                    "id": 1,
                    "category": {
                        "id": 3,
                        "name": "Laptop"
                    },
                    "name": "Hp Pavilion Laptop update ",
                    "description": "this is a laptop update",
                    "price": "2023.00"
                },
                "quantity": 5
            }
        ],
        "success": "Fetch all Stocks Product"
    }
  ```
  
 **Get  Single Product Stocks**
- **URL**: `/store/stocks/{id}/`
- **Method**: `GET`
- **Response**:
  ```json
    {
        "data": {
            "id": 1,
            "product": {
                "id": 1,
                "category": {
                    "id": 3,
                    "name": "Laptop"
                },
                "name": "Hp Pavilion Laptop update ",
                "description": "this is a laptop update",
                "price": "2023.00"
            },
            "quantity": 5
        },
        "success": "Fetch single Stock Product successfully"
    }
  ```
  
**Create a new Product Stocks**
- **URL**: `/store/stocks/`
- **Method**: `POST
- **Request Body**:
    ```json
        {
            "product_id": 1,
            "quantity": 5
        }
    ```
- **Response**:
  ```json
    {
        "data": {
            "id": 1,
            "product": {
                "id": 1,
                "category": {
                    "id": 3,
                    "name": "Laptop"
                },
                "name": "Hp Pavilion Laptop update ",
                "description": "this is a laptop update",
                "price": "2023.00"
            },
            "quantity": 5
        },
        "success": "Stock Product create successfully"
    }
  ```
  
**Update a single Product Stocks All Document**
- **URL**: `/store/stocks/{id}/`
- **Method**: `PUT`
- **Request Body**:
  ```json
    {
        "product_id": 1,
        "quantity": 100
    }
  ```
- **Response**:
  ```json
    {
        "data": {
            "id": 1,
            "product": {
                "id": 1,
                "category": {
                    "id": 3,
                    "name": "Laptop"
                },
                "name": "Hp Pavilion Laptop update ",
                "description": "this is a laptop update",
                "price": "2023.00"
            },
            "quantity": 100
        },
        "success": "Product Stock Update successfully"
    }
  ```


**Update a single Product Stocks All Document**
- **URL**: `/store/stocks/{id}/`
- **Method**: `PATCH`
- **Request Body**:
  ```json
    {
        "quantity": 5
    }
  ```
- **Response**:
  ```json
    {
        "data": {
            "id": 1,
            "product": {
                "id": 1,
                "category": {
                    "id": 3,
                    "name": "Laptop"
                },
                "name": "Hp Pavilion Laptop update ",
                "description": "this is a laptop update",
                "price": "2023.00"
            },
            "quantity": 5
        },
        "success": "Product Stock  udated successfully"
    }
  ```

## Installation

1. **Clone the repository:**
   ```bash
   https://github.com/Rafiul29/snapmart.git
   cd snapmart
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure PostgreSQL:**
   - Update `DATABASES` in `settings.py` with your PostgreSQL credentials.
   - Open the settings.py file of your Django project.
   - Update the DATABASES Setting:
    - Replace the default database settings with the following configuration:
    - Already setup Complete settings file
     ```json
      DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'postgres',
                'USER': 'postgres.vovjpmzgptdtgwfmiwkg',
                'PASSWORD': 'revc7REcEyRZRL8O',
                'HOST': 'aws-0-ap-southeast-1.pooler.supabase.com',
                'PORT': '6543'
            }
        }
     ```
4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the server:**
   ```bash
   python manage.py runserver
   ```

## Run with Docker

1. **Build and Start the Docker Container:**
   ```bash
   docker-compose up --build
   ```
    or detach mode
    ```bash
   docker-compose up -d
   ```
   

2. **Access the Application:**
   - Navigate to `http://localhost:8000/` to access the API.

## Bonus Features

### Dockerize the Application
- Build and run the Docker container using the provided Dockerfile.

### Host the Application
- Deploy to services  Render: Cloud Application Platform.

## Frontend Design
- Integrate with a creative frontend using modern frameworks like React + Vite.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
