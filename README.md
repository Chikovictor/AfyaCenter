# 🏥 AfyaCenter — Hospital Management System

Welcome to **AfyaCenter** — a complete hospital management system built with **Django (Python)**.  
This system helps hospitals manage patients, doctors, appointments, medical records, billing, and more.

---

## 🚀 Live Demo

👉 **Link:** https://your-deployment-url.com  
*(This link will work once you deploy your app — see Deployment section below)*

---

## 🧠 Project Overview

AfyaCenter is designed for healthcare facilities to efficiently:

✅ Manage patient records  
✅ Register and assign doctors  
✅ Book and manage appointments  
✅ Track medical history and billing  
✅ Provide secure access for staff and admins

✨ This system improves workflow and reduces manual paperwork across departments.

---

## 📁 Features

| Feature | Available |
|---------|-----------|
| Patient Registration | ✅ |
| Appointment Scheduling | ✅ |
| Doctor Management | ✅ |
| Billing & Payments | ⚠️ Coming Soon |
| Role-based Access | ⚙️ Planning |

---

## 🧰 Tech Stack

- **Framework:** Django (Python)  
- **Database:** SQLite (default, can migrate to PostgreSQL)  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** TBD (Heroku, Render, or Vercel)  
- **Version Control:** Git & GitHub

---

## 📸 Screenshots

### Dashboard View
<div style="border: 3px solid #4CAF50; padding: 10px; display: inline-block; border-radius: 6px;">
  <img src="images/dashboard.png" alt="Dashboard Screenshot" width="800">
</div>

### Patient List View
<div style="border: 3px solid #4CAF50; padding: 10px; display: inline-block; border-radius: 6px;">
  <img src="images/patient_list.png" alt="Patient List Screenshot" width="800">
</div>

---

## 📦 Installation (Local Setup)

1. Clone the repository

```bash
git clone https://github.com/Chikovictor/AfyaCenter.git
cd AfyaCenter
Create virtual environment & install dependencies

python -m venv venv
venv\Scripts\activate        # (Windows)
source venv/bin/activate     # (Mac/Linux)
pip install -r requirements.txt
Apply database migrations

python manage.py migrate
Run the development server

python manage.py runserver
Now visit: http://localhost:8000

🗂 Folder Structure
AfyaCenter/
│
├── AFYACENTER/        Python Django core project
├── patients/          Patients app (models & views)
├── static/            CSS, JS & images
├── db.sqlite3         Database
├── manage.py          Django runner
