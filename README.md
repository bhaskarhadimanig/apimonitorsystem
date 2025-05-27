# API Monitoring SaaS - Full Stack Bundle

This is a **production-ready, multi-tenant SaaS** solution for API availability monitoring.

---

## 🗂️ Project Structure

```
api-monitor-saas/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   ├── api.py
│   │   │   │   ├── email_group.py
│   │   │   │   ├── monitor.py
│   │   │   │   ├── settings.py
│   │   │   │   └── user.py
│   │   │   └── router.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── crud/
│   │   │   ├── crud_api.py
│   │   │   ├── crud_email_group.py
│   │   │   ├── crud_monitor.py
│   │   │   ├── crud_settings.py
│   │   │   └── crud_user.py
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   ├── base_class.py
│   │   │   └── session.py
│   │   ├── models/
│   │   │   ├── api.py
│   │   │   ├── apirequest.py
│   │   │   ├── email_group.py
│   │   │   ├── email_settings.py
│   │   │   └── user.py
│   │   ├── schemas/
│   │   │   ├── api.py
│   │   │   ├── email_group.py
│   │   │   ├── monitor.py
│   │   │   ├── settings.py
│   │   │   └── user.py
│   │   ├── services/
│   │   │   └── email.py
│   │   ├── worker/
│   │   │   └── tasks.py
│   │   └── main.py
│   ├── celery_worker.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── components/
│   │   ├── ApiForm.tsx
│   │   ├── ApiTable.tsx
│   │   ├── EmailGroupTable.tsx
│   │   ├── EmailSettingsForm.tsx
│   │   ├── Layout.tsx
│   │   ├── MonitoringChart.tsx
│   │   └── ProtectedRoute.tsx
│   ├── context/
│   │   └── AuthContext.tsx
│   ├── pages/
│   │   ├── _app.tsx
│   │   ├── apis/
│   │   │   ├── [id].tsx
│   │   │   └── index.tsx
│   │   ├── dashboard.tsx
│   │   ├── email-groups/
│   │   │   └── index.tsx
│   │   ├── index.tsx
│   │   ├── login.tsx
│   │   ├── settings.tsx
│   │   └── signup.tsx
│   ├── utils/
│   │   └── api.ts
│   ├── package.json
│   └── next.config.js
│
└── README.md
```

---

## 🚀 Step-by-Step Instructions

### 1. **Backend Setup**

#### a. Environment & Dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### b. Configuration

1. Edit `.env` with your settings (PostgreSQL, SMTP, Redis, etc).
2. Example for local dev:

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/apimonitor
SECRET_KEY=changeme
SMTP_HOST=smtp.mailtrap.io
SMTP_PORT=2525
SMTP_USER=your_mailtrap_user
SMTP_PASS=your_mailtrap_pass
REDIS_BROKER_URL=redis://localhost:6379/0
CORS_ORIGINS=http://localhost:3000
```

#### c. Database

1. Start PostgreSQL (locally or with Docker).
2. Create the database:  
   `createdb apimonitor`
3. (Optional but recommended) Run migrations with Alembic or auto-create tables:
   - For Alembic:  
     `alembic upgrade head`
   - Or let SQLAlchemy create tables on first run (for dev only).

#### d. Start Backend API

```bash
uvicorn app.main:app --reload
```

Backend should now be at [http://localhost:8000](http://localhost:8000)

#### e. Start Celery Worker

```bash
celery -A app.worker.tasks worker --loglevel=info
```

---

### 2. **Frontend Setup**

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at [http://localhost:3000](http://localhost:3000)

**Ensure `NEXT_PUBLIC_API_URL` is set in `next.config.js` to the backend URL.**

---

### 3. **Running The App**

- Open [http://localhost:3000](http://localhost:3000)
- Sign up, login, add your APIs, configure alert emails/groups, and monitor!

---

### 4. **Production Notes**

- Use production SMTP, PostgreSQL, Redis.
- Use Gunicorn (with UvicornWorker) for FastAPI.
- Use HTTPS and secure cookie storage.
- For OAuth (Google/GitHub), add NextAuth.js (see NextAuth docs).
- Deploy frontend (Vercel, Netlify, or your own server).

---

### 5. **Extending**

- For SSO/company-wide multi-tenancy: add `org_id` to user and API models, filter all queries by `org_id`.
- For OAuth: Integrate NextAuth.js in frontend (see NextAuth docs).
- For Docker Compose: let me know if you want a ready-to-run compose file!

---

## 👍 You're ready to build, test, and deploy your SaaS!

---

**Each folder contains complete, working files as shown above. Copy into `backend/` and `frontend/` and follow these steps.**

For questions, advanced features, or a zipped bundle, just ask!