# 📖 Flask Blog - A Feature-Rich Blogging Platform

Welcome to **Flask Blog**, a simple yet powerful blog platform built with Flask, SQLAlchemy, and Bootstrap. This project allows users to create, edit, and delete blog posts, register and log in, and interact through comments.

## 🚀 Features

- 📝 **Create, Edit, and Delete Blog Posts**
- 🔑 **User Authentication & Authorization** (Flask-Login)
- 🔒 **Password Hashing** (Werkzeug Security)
- 💬 **Comment System**
- 🎨 **Rich Text Editing** (CKEditor 5 Integration)
- 📷 **User Profile Pictures** (Flask-Gravatar)
- 🏗 **Bootstrap 5 for Responsive UI**

## 🛠️ Technologies Used

- **Flask** - Web Framework
- **Flask-SQLAlchemy** - ORM for Database Management
- **Flask-Login** - User Authentication
- **Flask-CKEditor** - Rich Text Editor
- **Bootstrap 5** - Frontend Styling
- **SQLite** - Lightweight Database

## 📂 Project Structure

```
📦 flask-blog
 ┣ 📂 static
 ┃ ┣ 📂 assets
 ┃ ┗ 📂 css
 ┣ 📂 templates
 ┃ ┣ 📜 base.html
 ┃ ┣ 📜 index.html
 ┃ ┣ 📜 post.html
 ┃ ┗ 📜 login.html
 ┣ 📜 app.py
 ┣ 📜 forms.py
 ┣ 📜 models.py
 ┗ 📜 requirements.txt
```

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/flask-blog.git
cd flask-blog
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate    # For Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up the Database
```sh
flask db upgrade
```

### 5️⃣ Run the Application
```sh
flask run
```

Access the app in your browser at `http://127.0.0.1:5000/`

## 🎨 Screenshots

![image](https://github.com/user-attachments/assets/f9d5214d-dac4-4f9f-bdf3-0d6a2d70a041)
![image](https://github.com/user-attachments/assets/41c20dd4-be3d-421e-a2c7-177473eb3b84)
![image](https://github.com/user-attachments/assets/bf5a62ee-f73c-4691-80cd-8bba4b59402c)
![image](https://github.com/user-attachments/assets/d0ec262f-1bbe-4617-9dea-b0325b71a2f3)
![image](https://github.com/user-attachments/assets/af3593cf-c321-4254-81fd-f27dd1384fa3)




## 📌 To-Do List
- [ ] Implement Email Verification
- [ ] Add Image Uploads for Blog Posts
- [ ] Improve UI with Custom CSS

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📌Points to remember 
- [ ] The first login id registered should be of admin here the database already contains : email: admin@gmail.com password:admin@!
- [ ] The user id can be stored after the registeration of user the database already contains a test user : email: user@gmail.com password:user21
- [ ] you can delete the existing database and just run the main.py and store the details again and a new database will be created.


