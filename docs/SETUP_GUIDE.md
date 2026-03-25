# Setup Guide

Complete guide to setting up and running the AI Automation Workflows project.

---

## Prerequisites

- Python 3.10 or higher
- Git
- A Make.com account (free tier works)
- API keys (OpenAI, etc.)

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/fairaaz0089-ops/ai-automation-workflows.git
cd ai-automation-workflows
```

---

## Step 2: Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Step 3: Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Then edit `.env` with your actual credentials:

```env
# AI APIs
OPENAI_API_KEY=sk-your-key-here

# WordPress
WORDPRESS_URL=https://yoursite.com
WORDPRESS_USER=your_username
WORDPRESS_PASS=your_app_password

# Medium
MEDIUM_TOKEN=your_medium_token

# Pinterest
PINTEREST_ACCESS_TOKEN=your_pinterest_token

# LinkedIn
LINKEDIN_ACCESS_TOKEN=your_linkedin_token
```

> **Security Note:** Never commit your `.env` file. It is already listed in `.gitignore`.

---

## Step 4: Run Your First Script

```bash
# Generate a blog post
python scripts/content/generate_blog_post.py --topic "AI Automation Tools" --words 800

# Generate an Upwork proposal
python scripts/upwork/proposal_generator.py --job "Need Python developer for automation project"
```

---

## Step 5: Import Make.com Workflows

1. Log into your [Make.com](https://make.com) account
2. Click **Create a new scenario**
3. Click the **three dots** icon > **Import Blueprint**
4. Upload any `.json` file from the `/workflows` folder
5. Fill in your API credentials in each module
6. Test and activate the scenario

---

## Troubleshooting

### ImportError: No module named 'openai'
```bash
pip install openai
```

### .env file not loading
Make sure you have `python-dotenv` installed:
```bash
pip install python-dotenv
```

### WordPress authentication failing
- Use an **Application Password**, not your main password
- Generate one at: WordPress Dashboard > Users > Profile > Application Passwords

---

## Getting Help

- Open an [Issue](https://github.com/fairaaz0089-ops/ai-automation-workflows/issues)
- Visit [figofai.com](https://figofai.com) for more resources
