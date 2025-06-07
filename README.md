<h1 align="center">🛍️ Style Circuit</h1>

<p align="center">A modern and scalable full-stack <strong>eCommerce platform</strong> built with Django & PostgreSQL</p>
<p align="center"><em>“Where Style Meets Innovation”</em></p>

---

## 🚧 Project Status

> 🔧 **Status:** In development  
> 🎯 Goal: Full-featured online fashion store with custom admin panel and payment gateway

---

## ✨ Features (Planned + In Progress)

✅ **User Features**
- 🔐 Secure signup, login, logout
- 👤 Profile with avatar upload
- 🛒 Cart & Wishlist (coming soon)
- 💳 Seamless checkout with payment gateway (e.g., Stripe/Razorpay)

🔧 **Admin Panel**
- 📦 Product management (CRUD)
- 👥 User management
- 📈 Dashboard & analytics *(planned)*

💄 **Frontend**
- 🎨 Clean, responsive UI (Tailwind CSS)
- 🌓 Dark mode *(optional)*

🗃️ **Backend**
- ⚙️ Built with Django & PostgreSQL
- 🔒 Role-based access control
- ✉️ Email-based password reset *(planned)*

---

## 🧰 Tech Stack

| Layer        | Technology           |
| ------------ | -------------------- |
| Backend      | Django, Python       |
| Frontend     | HTML5, Tailwind CSS  |
| Database     | PostgreSQL           |
| Auth         | Django Auth System   |
| Deployment   | Render / Railway / Vercel (planned) |
| Payment      | Stripe / Razorpay *(planned)* |

---

## 🗂️ Directory Structure

```bash
stylecircuit/
├── usermanagement/       # Auth & user profile
├── adminpanel/           # Admin tools
├── cart/                 # Cart logic (upcoming)
├── products/             # Product catalog (upcoming)
├── payments/             # Gateway logic (upcoming)
├── templates/            # HTML templates
├── static/               # Static assets (CSS, JS, images)
├── media/                # Uploaded files (profile images, etc.)
├── stylecircuit/         # Project settings, URLs
└── manage.py
