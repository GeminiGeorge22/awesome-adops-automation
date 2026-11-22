[![CONTRIBUTING](https://github.com/OstinUA/Promt-AI-Helper/blob/main/Additional%20files/Image/CONTRIBUTING.svg)](https://github.com/adops-tool)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-3e80ed?style=for-the-badge&logo=github&logoColor=white)](https://github.com/adops-tool/awesome-adops-automation/pulls)
[![Open Source](https://img.shields.io/badge/Open_Source-Yes-brightgreen?style=for-the-badge&logo=open-source&logoColor=white)](https://github.com/adops-tool/awesome-adops-automation/pulls)

# Contributing to Awesome AdOps Automation

First off, thank you for considering contributing to Awesome AdOps Automation. We appreciate your time and effort in helping us build the ultimate curated list of tools that replace manual trafficking, QA, and reporting work with scripts.

The goal of this project is to curate a high-quality list of AI-powered and scriptable resources for ad server API SDKs, campaign and trafficking automation, ad tag QA and testing, ad data pipelines, reporting, and workflow orchestration. To maintain the quality of this list, please review the guidelines below before submitting a pull request.

By participating in this project you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Submission Guidelines

Please ensure your submission adheres to the following core criteria:

- **Relevance:** The tool must have a clear AI, SDK or scripting component that is an essential part of the modern AdOps stack.
- **Active Maintenance:** We only accept active projects. Abandoned, archived or unmaintained tools will not be merged.
- **Direct Links Only:** Absolutely no affiliate, tracking, or referral links are allowed.

## Description Standards

Descriptions must be concise, objective, and purely informational.

- **Do:** Focus on the exact utility and core features of the tool.
  > *Example: "Scripts bulk trafficking and QA of Campaign Manager 360 entities from Google Sheets."*
- **Don't:** Use marketing fluff, superlatives, or subjective claims.
  > *Example: "The world's best AdOps platform that revolutionizes your trafficking process."*

## Step-by-Step Submission Process

To add a new tool to the list, please follow these steps:

1. **Star the repository:** Show your support and help the community grow.
2. **Locate the file:** Navigate to the `README.md` file in the main branch of this repository.
3. **Edit the document:** Click the "Edit" (pencil) icon to begin making your changes.
4. **Format your entry:** Add your link to the appropriate category using the exact Markdown syntax below. Use the `github` icon when the primary link is a GitHub repository and the `web` icon otherwise. Always link directly to the tool's site or repository — never through search engines or redirect services:

   ```
   ![github](image/alg_R.png) [Tool Name](https://github.com/org/repo) - Short, objective description of what it does.

   ![web](image/alg_I.png) [Tool Name](https://example.com) - Short, objective description of what it does.
   ```

   Do not include pricing or promotional claims in descriptions.
5. **Run the checks locally:** This repository does not yet run server-side CI checks, so validate the format yourself:
   ```bash
   python3 scripts/check_readme.py
   ```
   The checker verifies every entry line follows the format above, that referenced images exist, and that the Table of Contents anchors resolve.
6. **Create a Pull Request:** Submit your PR with a clear and descriptive title using the following format: `Add [Tool Name]`

## What gets rejected

- Stale or archived projects (last push more than ~12 months ago).
- Lists of links without a clear, verified utility.
- Affiliate, tracking, or referral URLs.
- Duplicates of resources already in the README.
- Marketing copy instead of a factual, one-sentence description.
