# 🧑‍💻 Django User Management System - Full Guide

A complete step-by-step guide to creating, developing, and deploying a Django User Management system with email verification, profile management, and deployment using Render.

---

## 🧰 Required Software

| Tool     | Description                                  | Link                                                                   |
| -------- | -------------------------------------------- | ---------------------------------------------------------------------- |
| Python   | Programming language                         | [https://www.python.org/downloads/](https://www.python.org/downloads/) |
| pip      | Python package manager                       | Comes with Python                                                      |
| Git      | Version control                              | [https://git-scm.com/downloads](https://git-scm.com/downloads)         |
| GitHub   | Code hosting                                 | [https://github.com/](https://github.com/)                             |
| VS Code  | Code editor                                  | [https://code.visualstudio.com/](https://code.visualstudio.com/)       |
| Render   | Hosting platform                             | [https://render.com/](https://render.com/)                             |
| Gunicorn | WSGI HTTP Server for Django (for deployment) | installed via pip                                                      |
| Docker   | (Optional) Containerization                  | [https://www.docker.com/](https://www.docker.com/)                     |

---

## ✅ Step-by-Step Project Workflow (11 Steps)

### 1. **Project Setup**

* Install Python and pip
* Create a virtual environment:

  ```bash
  python -m venv venv
  source venv/Scripts/activate  # On Windows
  ```
* Install Django:

  ```bash
  pip install django
  ```
* Create a new project:

  ```bash
  django-admin startproject User_mgt
  cd User_mgt
  ```
* Create a new app:

  ```bash
  python manage.py startapp akaunti
  ```
* Add the app to `INSTALLED_APPS` in `settings.py`

---

### 2. **GitHub Setup**

* Initialize Git:

  ```bash
  git init
  git add .
  git commit -m "Initial commit"
  ```
* Create a GitHub repo and push:

  ```bash
  git remote add origin https://github.com/your-username/repo.git
  git branch -M main
  git push -u origin main
  ```

---

### 3. **User Registration**

* Create a custom user registration form using `forms.py`
* Use Django's built-in `UserCreationForm` or extend it
* Create a `register` view and template

---

### 4. **Email Verification**

* After saving a new user, set `user.is_active = False`
* Generate email verification link using Django’s `default_token_generator`
* Send email using `send_mail()`
* Create a `verify_email` view to handle activation link

---

### 5. **Login / Logout**

* Use Django’s built-in `LoginView` and `LogoutView`
* Only allow login for active users
* Customize templates for login and logout

---

### 6. **Profile Page**

* Create a view to display logged-in user info
* Use `@login_required` to protect the profile route
* Display user details: username, email, etc.

---

### 7. **User Dashboard**

* Create a separate view and template after login
* Display welcome message and navigation buttons
* Add optional stats or links to recent activity

---

### 8. **Admin Panel**

* Create a superuser:

  ```bash
  python manage.py createsuperuser
  ```
* Use Django admin at `/admin/` to manage users

---

### 9. **Testing**

* Write at least 1 unit test using Django’s `TestCase`
* Example: test if registration form is valid or user gets created

---

### 10. **Deployment Preparation**

* Install Gunicorn:

  ```bash
  pip install gunicorn
  ```
* Create `requirements.txt`:

  ```bash
  pip freeze > requirements.txt
  ```
* Create `render.yaml`:

  ```yaml
  services:
    - type: web
      name: user-management-app
      env: python
      buildCommand: pip install -r requirements.txt
      startCommand: gunicorn User_mgt.wsgi:application
      envVars:
        - key: SECRET_KEY
          value: your-secret-key
        - key: DEBUG
          value: false
        - key: DJANGO_SETTINGS_MODULE
          value: User_mgt.settings
  ```
* Update `settings.py`:

  ```python
  STATIC_URL = '/static/'
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  ```
* Collect static files:

  ```bash
  python manage.py collectstatic
  ```

---

### 11. **Deployment to Render**

* Push code to GitHub
* Go to [https://render.com](https://render.com)
* Click **New Web Service**
* Select your GitHub repo
* Render will auto-detect `render.yaml`
* Add env variables:

  * `SECRET_KEY`
  * `DEBUG` = false
  * `ALLOWED_HOSTS` = yourdomain.onrender.com
* Deploy!

---

## 📸 Screenshots 
![Screenshot 2025-07-07 150537](https://github.com/user-attachments/assets/59e60d8c-fa27-444a-b246-f573279c6b22)
![Screenshot 2025-07-07 161238](https://github.com/user-attachments/assets/289e43f5-98fb-4892-8f63-f63a0052f129)
![Screenshot 2025-07-07 163333](https://github.com/user-attachments/assets/43814d87-8d6e-40d7-a705-d66e688fcc10)


---

## ✍️ Author

* Name: *rinnah-oyugi*
* GitHub: [@rinnah-oyugi](https://github.com/rinnah-oyugi)

---

