# 🚀 Stratos. | Team Task Management

**Stratos** is a high-performance, visually stunning task management dashboard built with Flask. It features a modern **Glassmorphism** UI, role-based access control, and real-time project tracking.



## ✨ Features

*   **Glassmorphism UI:** A sleek, futuristic interface built with Tailwind CSS and custom backdrop filters.
*   **Command Center:** A centralized dashboard displaying active tasks, completion rates, and team size.
*   **Role-Based Access (RBAC):**
    *   **Admins:** Full control to create projects, assign tasks, and manage users.
    *   **Members:** Read-only access to project boards with the ability to track their assigned work.
*   **Task Management:** Color-coded priority levels (High, Medium, Low) and deadline tracking.
*   **Secure Authentication:** User signup and login powered by `Werkzeug` security with `scrypt` password hashing.

## 🛠️ Tech Stack

*   **Backend:** Python / Flask
*   **Database:** SQLAlchemy (SQLite/PostgreSQL)
*   **Frontend:** Tailwind CSS, FontAwesome 6
*   **Deployment:** Railway / GitHub

## 🚀 Installation & Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/KrishnahithaJagannatham/team-task-management.git
    cd team-task-management
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    # Activate on Windows:
    .\venv\Scripts\activate
    # Activate on Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python run.py
    ```
    The app will be available at `[http://127.0.0.1:5000](http://127.0.0.1:5000)`.

## 🌐 Deployment

This project is configured for easy deployment on **Railway**.

1.  Push your code to GitHub.
2.  Connect your repository to Railway.
3.  Ensure your `Procfile` is present: `web: gunicorn run:app`.
4.  Generate a domain in Railway Settings.

## 📝 License

This project is open-source and available under the **MIT License**.

👨‍💻 Author
Krishnahitha
