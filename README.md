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
![image](https://github.com/user-attachments/assets/66bfc62b-b175-4ebc-8662-c926e2dc8261)
![image](https://github.com/user-attachments/assets/ffd11ab7-e007-4b92-aac4-a039b3af6010)
![image](https://github.com/user-attachments/assets/191c0537-058e-432d-a211-6c8e1678cae5)
![image](https://github.com/user-attachments/assets/1eef5142-a5f6-442f-9e35-8eb1c009d082)
![image](https://github.com/user-attachments/assets/9e37e150-5653-410c-899e-54fa7c54013d)





## 📌 To-Do List
- [ ] Implement Email Verification
- [ ] Add Image Uploads for Blog Posts
- [ ] Improve UI with Custom CSS

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📌Points to remember 
- [ ] The first login id registered should be of admin here the database already contains : email: admin@gmail.com password:admin@!
- [ ] The user id can be stored after the registeration of user the database already contains a test user : email: user@gmail.com password:user123
- [ ] you can delete the existing database and just run the main.py and store the details again and a new database will be created.


