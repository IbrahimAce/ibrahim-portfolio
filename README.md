# 🌐 Ibrahim Karanja — Personal Portfolio

A professional portfolio website built with **Django** and **Bootstrap 5**,
showcasing my projects, skills, experience, and education.

🔗 **Live Site:** https://ibrahim-portfolio-ysam.onrender.com

> ⏱️ **Note:** The site is hosted on Render's free tier which spins down
> after inactivity. First load may take **30–60 seconds** to wake up —
> subsequent loads are instant!

---

## ✨ Features

- 🎨 Dark blue responsive design
- 💼 Projects pulled from GitHub
- 📊 Animated skill progress bars
- 🕐 Experience & Education timeline
- 📬 Contact form that saves to database
- ⚙️ Django Admin dashboard to manage all content
- 🗄️ Permanent PostgreSQL database via Supabase
- 🚀 Deployed on Render free tier

---

## 🛠️ Built With

- **Backend:** Python 3.10, Django 5.2
- **Frontend:** Bootstrap 5, Font Awesome, Vanilla JS
- **Database:** Supabase PostgreSQL (production) / SQLite (local)
- **Hosting:** Render.com
- **Static Files:** WhiteNoise

---

## 🚀 Run Locally
```bash
git clone https://github.com/IbrahimAce/ibrahim-portfolio.git
cd ibrahim-portfolio
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Visit http://127.0.0.1:8000

---

## 👤 Author

**Ibrahim Karanja Wambui**
- 📧 karanjaibrahim141@gmail.com
- 🐙 GitHub: [@IbrahimAce](https://github.com/IbrahimAce)
- 🌍 Nairobi, Kenya
