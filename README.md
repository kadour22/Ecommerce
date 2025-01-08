E-commerce API Project
This E-commerce API project is a robust and scalable backend solution for managing an online store. Built with Django and Django REST Framework, this project provides a comprehensive set of features to handle various aspects of an e-commerce platform, including product management, customer management, cart functionality, and order processing.

Key Features:
🟢Modular Architecture: The project is organized into separate modules for products, customers, cart items, and orders, ensuring maintainability and scalability.
🟢Secure Authentication: Utilizes Django's built-in authentication system to manage user accounts and secure endpoints.
🟢Product Management: Allows administrators to create, update, and delete products, with support for categories and product images.
🟢Customer Management: Handles customer information, including full name, phone number, address, and email, with unique constraints to ensure data integrity.
🟢Cart Functionality: Supports adding, updating, and removing items from the cart, with separate handling for guest users and authenticated customers.
🟢Order Processing: Facilitates order creation and management, including calculating the total price of orders and associating cart items with orders.
🟢Database Optimization: Uses select_related and prefetch_related to optimize database queries and improve performance.
Environment Configuration: Utilizes a .env file to securely manage environment variables, including database credentials and the Django secret key.
Caching: Implements caching for product listings to enhance performance and reduce database load.
🟢RESTful API: Provides a clean and well-documented RESTful API for interacting with the e-commerce platform, making it easy to integrate with frontend applications.
This project serves as a solid foundation for building a full-featured e-commerce platform, with a focus on security, performance, and maintainability.
