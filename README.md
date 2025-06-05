## 🚀 Features

- ✅ User registration & authentication
- 🔐 JWT-based secure login
- 🛍️ Product listing and detail views
- 🛒 Cart management
- 📦 Order processing and management
- 🧑‍💼 Admin panel for managing models
- 🌐 RESTful API structure for frontend integration

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (via `djangorestframework-simplejwt`)
- **Database**: SQLite (default), easily switchable to PostgreSQL
- **Others**: Django Admin, DRF serializers, class-based views

---

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/kadour22/Ecommerce.git
   cd Ecommerce
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional for admin access):

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**:

   ```bash
   python manage.py runserver
   ```

---

## 🔑 Authentication

This API uses **JWT (JSON Web Token)** for secure authentication.

- Obtain token:
  ```
  POST /api/token/
  ```

- Refresh token:
  ```
  POST /api/token/refresh/
  ```

Include the token in the `Authorization` header as:
```
Authorization: Bearer <your_token>
```

---

## 🔍 API Endpoints (Sample)

> Full list can be explored via the browsable DRF API interface or Postman.

| Method | Endpoint                | Description             |
|--------|-------------------------|-------------------------|
| POST   | `/api/token/`           | Obtain JWT tokens       |
| POST   | `/api/token/refresh/`   | Refresh JWT token       |
| GET    | `/api/products/`        | List all products       |
| GET    | `/api/products/<id>/`   | Product details         |
| POST   | `/api/cart/`            | Add item to cart        |
| GET    | `/api/orders/`          | List user orders        |

---

## 🖼️ Admin Panel

Access Django's built-in admin at:
```
http://127.0.0.1:8000/admin/
```

Use the superuser credentials created earlier.

---

## 📌 Folder Structure

```
Ecommerce/
├── core/               # Main Django app
│   ├── models.py       # Product, Cart, Order models
│   ├── serializers.py  # DRF serializers
│   ├── views.py        # API views
│   └── urls.py         # URL routing
├── Ecommerce/          # Project settings
├── manage.py
└── requirements.txt
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Kadour22**

- GitHub: [@kadour22](https://github.com/kadour22)

---

## 🌟 Show Your Support

If you found this project helpful, feel free to ⭐️ star the repo and share it!

```

---

Let me know if you want to include a section for **Docker setup**, **Postman collection**, or **deployment instructions**!
