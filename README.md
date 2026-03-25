# AI Automation Workflows

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Status-Active-brightgreen) ![Make.com](https://img.shields.io/badge/Make.com-Integrations-purple)

A comprehensive collection of **AI automation workflows**, Python scripts, and tools for content creation, affiliate marketing, Make.com integrations, and digital entrepreneurship.

> Built and maintained by [fairaaz0089-ops](https://github.com/fairaaz0089-ops) | Website: [figofai.com](https://figofai.com)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Workflows](#workflows)
- [Tools & Technologies](#tools--technologies)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This repository serves as a central hub for AI-powered automation tools designed to streamline:

- **Content Creation** - Auto-generate blog posts, Medium articles, Pinterest pins, and LinkedIn content
- **Affiliate Marketing** - Scripts to manage, track, and optimize affiliate links
- **Make.com Workflows** - JSON scenario blueprints ready to import into Make.com
- **Freelance Automation** - Upwork proposal generators, job search bots, and client management tools
- **Social Media Scheduling** - Multi-platform content scheduling and publishing automation
- **Amazon KDP** - Book generation and publishing pipeline helpers

---

## Features

- Python scripts for AI content generation using OpenAI, Genspark, and other LLMs
- Ready-to-import Make.com (formerly Integromat) JSON blueprints
- Affiliate link manager and tracker
- Upwork auto-proposal generator
- Medium & LinkedIn content scheduler
- Pinterest pin automation
- Amazon KDP book outline generator
- WordPress auto-publishing scripts
- SEO keyword research automation
- Email marketing automation templates

---

## Folder Structure

```
ai-automation-workflows/
|-- workflows/          # Make.com JSON blueprints
|-- scripts/            # Python automation scripts
|   |-- content/        # Content creation scripts
|   |-- affiliate/      # Affiliate marketing tools
|   |-- social-media/   # Social media automation
|   |-- upwork/         # Upwork proposal tools
|   |-- kdp/            # Amazon KDP helpers
|-- tools/              # Utility scripts and helpers
|-- templates/          # Prompt templates and email templates
|-- docs/               # Documentation and guides
|-- .gitignore
|-- LICENSE
|-- README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- A Make.com account (for workflow blueprints)
- API keys for OpenAI / other LLMs as needed

### Installation

```bash
# Clone the repository
git clone https://github.com/fairaaz0089-ops/ai-automation-workflows.git

# Navigate into the project directory
cd ai-automation-workflows

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
WORDPRESS_URL=your_wordpress_site_url
WORDPRESS_USER=your_username
WORDPRESS_PASS=your_app_password
MEDIUM_TOKEN=your_medium_integration_token
```

---

## Usage

### Run a Content Generation Script

```bash
python scripts/content/generate_blog_post.py --topic "AI Automation" --words 1000
```

### Import a Make.com Workflow

1. Open [Make.com](https://make.com)
2. Go to **Scenarios** > **Create a new scenario**
3. Click the **three dots** > **Import Blueprint**
4. Upload any `.json` file from the `/workflows` folder

---

## Workflows

| Workflow | Description | Platform |
|---|---|---|
| `content-pipeline.json` | Auto-generates and publishes blog posts | Make.com + WordPress |
| `social-scheduler.json` | Schedules posts to LinkedIn, Medium, Pinterest | Make.com |
| `affiliate-tracker.json` | Tracks clicks and conversions on affiliate links | Make.com |
| `upwork-proposals.json` | Monitors job listings and sends proposals | Make.com |
| `kdp-pipeline.json` | Amazon KDP book creation and upload pipeline | Make.com |

---

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core scripting language |
| Make.com | No-code workflow automation |
| OpenAI API | AI content generation |
| WordPress REST API | Auto-publishing content |
| Medium API | Article publishing |
| Pinterest API | Pin scheduling |
| LinkedIn API | Post scheduling |
| Amazon KDP | Book publishing pipeline |

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

*Made with purpose by [fairaaz0089-ops](https://github.com/fairaaz0089-ops) | [figofai.com](https://figofai.com)*
