# Django User Management System

A simple Django project that handles user registration, login, logout, profile viewing, and password change.

## ✅ Features

- User Registration
- User Login & Logout
- User Profile Page
- Password Change Functionality
- Admin Panel Access
- Basic Unit Tests

## 🛠️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/User_mgt.git
   cd User_mgt
Create virtual environment & activate

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
Install dependencies

bash
Copy
Edit
pip install django
Run migrations

bash
Copy
Edit
python manage.py migrate
Start the server

bash
Copy
Edit
python manage.py runserver

![Screenshot 2025-07-07 150537](https://github.com/user-attachments/assets/59e60d8c-fa27-444a-b246-f573279c6b22)
![Screenshot 2025-07-07 161238](https://github.com/user-attachments/assets/289e43f5-98fb-4892-8f63-f63a0052f129)
![Screenshot 2025-07-07 163333](https://github.com/user-attachments/assets/43814d87-8d6e-40d7-a705-d66e688fcc10)


👩‍💻 Admin Access
To access the admin panel:

bash
Copy
Edit
python manage.py createsuperuser
Then visit http://127.0.0.1:8000/admin

🧪 Run Tests and debug any error experienced

bash
Copy
Edit
python manage.py test

![Screenshot 2025-07-07 170023](https://github.com/user-attachments/assets/90e33a6c-6b51-491f-927a-75faf79d8251)

📂 Project Structure
bash
Copy
Edit
User_mgt/
│
├── akaunti/            # User app
│   ├── views.py
│   ├── forms.py
│   ├── tests.py
│   └── urls.py
│
├── User_mgt/           # Main project settings
│   ├── settings.py
│   └── urls.py
│
├── templates/          # HTML files
├── db.sqlite3
└── manage.py
📄 License
MIT License.

🔗 Author
GitHub: rinnah-oyugi

yaml
Copy
Edit

---










