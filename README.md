# PLP React Dashboard

A **Personalized Learning Platform (PLP)** dashboard built with **React (frontend)** and **Django REST Framework (backend)**. This app allows instructors to track students’ performance, generate AI-driven recommendations, and see remedial needs in a visually appealing dashboard.

---

## Features

- **Dashboard for instructors** with circular progress bars showing student completion percentage.  
- **AI-driven recommendations** for learning resources.  
- **Remedial tracking** for students needing extra help.  
- **Detailed student view** with completed courses, pending courses, and subject scores.  
- **Minimalist dark-grey UI** with hover effects and Montserrat font.  
- **Frosted glass cards** for better readability.  
- **About page** and navigation bar.  
- **Footer** linking to GitHub profile.

---

## Technologies Used

- **Frontend:** React, TypeScript, Tailwind CSS, React Router, React Context API  
- **Backend:** Django, Django REST Framework  
- **Database:** SQLite (default)  
- **Others:** React Circular Progressbar, JSONField for course tracking

---

## Project Structure

```
plp_frontend/ # React frontend
├─ src/
│  ├─ components/
│  ├─ context/
│  ├─ pages/
│  ├─ App.tsx
│  └─ index.css
plp_backend/ # Django backend
├─ learning/
│  ├─ models.py
│  ├─ views.py
│  ├─ serializers.py
│  ├─ urls.py
│  └─ management/commands/seed.py
├─ plp_backend/
└─ manage.py
```

---

## Setup Instructions

## Clone and Run

**Clone the repository**
```bash
git clone https://github.com/AmanTShekar/PLP_React_App_1.git
cd PLP_React_App_1
```

### **Backend (Django)**

1. **Create a virtual environment**
```bash
python -m venv venv
```

2. **Activate the virtual environment**  
**Windows:**
```bash
venv\Scripts\activate
```
**macOS/Linux:**
```bash
source venv/bin/activate
```

3. **Install requirements**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Seed initial data**
```bash
python manage.py seed
```

6. **Run the server**
```bash
python manage.py runserver
```

---

### **Frontend (React)**

1. **Install dependencies**
```bash
cd plp_frontend
npm install
```

2. **Run the development server**
```bash
npm run dev
```

3. **Open in browser**  
Visit: [http://localhost:5173](http://localhost:5173) (default Vite dev server port)

---

## Usage

- **Home page:** Introduction to PLP dashboard.  
- **Dashboard:** View all students, completion percentage, and remedial needs.  
- **Student Recommendations:** Click on a student card to see personalized recommendations.  
- **About:** Information about the app and developer.

---

## Screenshots

### Dashboard
![Dashboard](plp_frontend/assets/dashboard.png)

### Student Card
![Student Card](plp_frontend/assets/student_card.png)

---

## Author

**Aman T Shekar**  
GitHub: [https://github.com/AmanTShekar](https://github.com/AmanTShekar)  

Made with ❤️ using React & Django
