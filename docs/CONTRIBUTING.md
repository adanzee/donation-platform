# 🤝 Contributing

## 🛠️ Tech Stack Focus

* **Frontend:** [11ty](https://www.11ty.dev/), [Pico.css (styling)](https://www.picocss.com) & [HTMX](https://www.htmx.org)
* **Backend:** Node.js & Express.js
* **Database:** MongoDB Atlas (Mongoose)
* **Package Manager:** pnpm

---

## 🚀 Getting Started Locally

### 1. Fork & Clone

* Click the **'Fork'** button on the main repository.
* Clone **your fork** to your local machine:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/CareBridge.git](https://github.com/YOUR_USERNAME/CareBridge.git)
    
    cd CareBridge
    
    git remote add upstream [https://github.com/omar-hossam/CareBridge.git](https://github.com/omar-hossam/CareBridge.git)
    ```

### 2. Install Dependencies

Make sure you have [pnpm](https://pnpm.io/installation) installed:
```bash
pnpm install
```

### 3. Environment Setup

### 4. Run Development Server

```bash
pnpm dev
```

## 🏗️ Development Workflow

### The Feature Workflow (Do this for every task!)

Always work on a branch. Never code directly on `main`.

1. **Sync with the team:**
    ```bash
    git checkout main
    git pull upstream main
    ```

2. **Create your task branch:** 
   
   ```bash
    git checkout -b feature/your-task-name
    ```

3. **Code & Test:** Ensure the app runs without errors and your changes work as expected using `pnpm dev`.

4. **Push to your fork:**
    Use **Conventional Commits** (keep it simple):
    ```bash
    git add .
    git commit -m "feat: implement user donation history"
    git push origin feature/your-task-name
    ```

5. **Submit Your Work:**
    - Go to the original [omar-hossam/CareBridge](https://github.com/omar-hossam/CareBridge) repository on GitHub.
    - Click **"Compare & Pull Request"**.
    - Briefly describe your changes and tag a teammate for a quick review.

## 📐Project Architecture

### 1. Backend & Database

### 2. Frontend (11ty + Picocss + HTMX)

* **Components:** Reusable UI elements go in `_components/`.
* **Pages:** Main views/screens go in `content/`.
* **Layout:** Main layout is located in `_includes/`.
* **Styling:** We use **Pico.css** for a lightweight, semantic CSS approach. Utilize Pico's built-in variables for consistency.

## 📜 Coding Standards

* **JS Styling:** Use standard JavaScript naming conventions (camelCase).
* **Async Logic:** Use `async/await` for all asynchronous operations (API calls, DB queries).
* **Privacy:** Always ensure sensitive data is handled securely and never hardcode credentials.
* **Security:** Always anonymize patient/donor data in the UI.

## 💬 Communication

If you're stuck or want to discuss a new feature, reach out to us on our Discord Group or open an Issue in the repository. Happy coding! 🚀
