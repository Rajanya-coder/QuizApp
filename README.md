# QuizApp 🎓

A simple full-stack quiz application built with **React (TypeScript)** for the frontend and **Flask** for the backend.  
Users can take quizzes by topic, see their scores, and check the leaderboard.

---

## 📂 **Project Structure**

```plaintext
QuizApp/
├── backend/
│   ├── app.py
│   ├── questions.json
│   ├── leaderboard.json
├── frontend/
│   ├── components/
│   │   ├── Quiz.tsx
│   │   ├── Leaderboard.tsx
│   │   ├── Navbar.tsx
│   ├── pages/
│   │   ├── Home.tsx
│   ├── App.tsx
│   ├── main.tsx
│   ├── index.css
│   ├── ...
🚀 How to Run
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/QuizApp.git
cd QuizApp
2️⃣ Setup & Run Backend
bash
Copy
Edit
# Go to backend folder
cd backend

# (Optional but recommended) Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install flask flask-cors

# Run Flask server
# Windows:
set FLASK_APP=app.py
# Mac/Linux:
export FLASK_APP=app.py
flask run
By default, the backend runs on http://localhost:5000.

3️⃣ Setup & Run Frontend
bash
Copy
Edit
# Open a new terminal
cd frontend

# Install dependencies
npm install

# Start frontend (Vite or CRA)
npm run dev   # if Vite
npm start     # if CRA
By default, the frontend runs on http://localhost:3000 or http://localhost:5173.

🧩 API Endpoints
GET /questions/<topic> → Get 10 questions for selected topic.

GET /leaderboard → Get leaderboard data.

POST /leaderboard → Submit new score to leaderboard.

🔭 Planned Improvements
✅ Migrate question & leaderboard storage from JSON files to MySQL database

✅ Add user authentication (login/register)

✅ Add admin panel to manage questions

✅ Improve UI/UX with more styling

✅ Deploy backend & frontend for live demo

📝 How to Contribute
Feel free to fork this repo and submit pull requests.
Suggestions & bug reports are welcome!

📧 Contact
Author: Rajanya
GitHub: Rajanya-coder

Thanks for checking this out! 🎉
