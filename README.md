# Science Virtual Lab (MVP)

A virtual science lab designed to simulate real-world scientific experiments interactively.  
The MVP version focuses on **basic physics simulations** such as the _simple pendulum_ and _free fall_ experiments.

---

## 🎯 MVP Goals

- Build two fundamental experiments:
  - **Simple Pendulum Simulation**
  - **Free Fall Simulation**
- Run simulations on the backend using scientific formulas.
- Display results interactively in the frontend.
- Allow users to register/login (Firebase Auth).
- Save user experiment runs and results (Firestore).

---

## 🧱 Project Architecture (MVP)

| Layer               | Technology                                      | Purpose                                |
| ------------------- | ----------------------------------------------- | -------------------------------------- |
| **Frontend**        | Next.js (App Router), TypeScript, MUI, Three.js | Interactive UI and visualization       |
| **Backend**         | FastAPI (Python), NumPy, SciPy                  | Physics simulation engine              |
| **Database / Auth** | Firebase Firestore + Authentication             | Store user data and experiment results |
| **Deployment**      | Vercel (Frontend) + Google Cloud Run (Backend)  | Scalable, serverless hosting           |

---

## 📁 Repository Structure (Monorepo)

---

## ✅ MVP Success Criteria

- User can sign up and log in.
- User can perform both simulations.
- Results are displayed and saved in Firestore.
- Frontend and backend are both deployed and working together publicly.

---

## 🛣️ Development Roadmap (Phases)

| Phase       | Description                                            |
| ----------- | ------------------------------------------------------ |
| **Phase 1** | Setup GitHub repo, add base docs (this file)           |
| **Phase 2** | Add `.svlignore` and `make_project_snapshot.py`        |
| **Phase 3** | Create backend skeleton (`/health`, `/sim/pendulum`)   |
| **Phase 4** | Create frontend skeleton (Next.js `lab/pendulum` page) |
| **Phase 5** | Connect Firebase Auth & Firestore                      |
| **Phase 6** | Deploy frontend (Vercel) & backend (Cloud Run)         |
| **Phase 7** | Add tests and basic monitoring                         |

---

## 🔒 Security & Environment

- Use `.env` files (not committed to Git).
- Store secrets in **Vercel Environment Variables** and **GCP Secret Manager**.
- Enable HTTPS and restricted CORS in production.

---

## 🧪 Testing Strategy

| Type       | Tool                         | Description                        |
| ---------- | ---------------------------- | ---------------------------------- |
| Unit Tests | **Pytest**, **Vitest/Jest**  | Logic testing for backend/frontend |
| E2E Tests  | **Playwright** (later phase) | Simulate full user flows           |

---

## 📊 Future Enhancements (After MVP)

- Real-time simulations using WebSocket.
- Interactive 3D visualizations (Three.js / Plotly).
- AI tutor assistant to explain results.
- Role-based access (Teacher / Student).
- PostgreSQL for advanced analytics.

---

## 🧩 Contribution Guidelines

This is a collaborative project between **Amin (Lead Developer)** and **Chatty (AI Assistant)**.

- Amin: coding, repo management, deployment.
- Chatty: architecture, documentation, reviews, code samples.

---

## 📄 License

The license will be added later after MVP completion.

---

## 📬 Contact

For questions or collaboration ideas:  
**Author:** Amin Nazari  
**Location:** Melbourne, Australia  
**AI Teammate:** Chatty (GPT-5)
