# Portfolio Website

A personal portfolio built with Flask.

## Features
- Home, About, Projects, Certifications, and Contact pages
- Responsive design with Bootstrap
- Contact form with email sending via SendGrid
- Modern folder structure for easy deployment

## Folder Structure

```
your-portfolio/
│
├── app.py
├── requirements.txt
├── .env.example
├── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       └── (your images)
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   ├── contact.html
│   └── certifications.html
│
└── venv/  (should be in .gitignore, not uploaded)
```

## Setup

1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and fill in your keys
5. Run the app:
   ```
   python app.py
   ```

## Environment Variables
- `SENDGRID_API_KEY`: Your SendGrid API key for sending emails
- `SECRET_KEY`: Flask secret key for sessions

## How to Deploy
- Make sure to set your environment variables on your deployment platform
- Do not upload your real `.env` file to GitHub

---

**Ready for GitHub and deployment!** 