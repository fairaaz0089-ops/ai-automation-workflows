#!/usr/bin/env python3
"""
Upwork Proposal Generator
Generates personalized proposals for Upwork job postings using AI.

Usage:
    python proposal_generator.py --job-url <URL> --skills "Python, AI, Automation"
"""

import os
import argparse
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


PROFILE = {
    "name": "Your Name",
    "skills": ["Python", "AI Automation", "Make.com", "Content Creation", "WordPress"],
    "experience_years": 5,
    "specialization": "AI automation workflows and digital content systems",
    "portfolio_url": "https://figofai.com"
}


def generate_proposal(job_description: str, skills: list = None) -> str:
    """
    Generate a personalized Upwork proposal.

    Args:
        job_description: The job posting text
        skills: List of relevant skills to highlight

    Returns:
        str: Generated proposal text
    """
    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)

        skills_str = ", ".join(skills or PROFILE["skills"])

        prompt = f"""Write a compelling Upwork proposal for this job:

{job_description}

Freelancer profile:
- Skills: {skills_str}
- Experience: {PROFILE['experience_years']} years
- Specialization: {PROFILE['specialization']}
- Portfolio: {PROFILE['portfolio_url']}

Requirements:
- Start with a hook that shows you understand their problem
- Keep it under 200 words
- Include 1 relevant result/achievement
- End with a clear call-to-action
- Professional but conversational tone"""

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Error generating proposal: {e}")
        return ""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Upwork proposals")
    parser.add_argument("--job", required=True, help="Job description text or file path")
    parser.add_argument("--skills", help="Comma-separated skills to highlight")
    args = parser.parse_args()

    job_desc = args.job
    if os.path.isfile(job_desc):
        with open(job_desc, "r") as f:
            job_desc = f.read()

    skills = args.skills.split(",") if args.skills else None

    print("Generating proposal...\n")
    proposal = generate_proposal(job_desc, skills)
    print(proposal)
