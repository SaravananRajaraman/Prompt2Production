---
layout: default
title: Automation & Deployment
nav_order: 10
---

# Documentation Automation & Deployment

> **How does the website stay up-to-date?** This page explains the automated workflow that keeps the Prompt2Production documentation published and synchronized.

---

## 🔄 Overview

The repository uses **GitHub Actions** to automatically build and deploy documentation whenever changes are pushed to the `main` branch. This ensures the latest content is always live for GitHub Copilot users without manual intervention.

**The workflow:**

1. You edit markdown files in `docs/` on the `main` branch
2. You commit and push your changes
3. GitHub Actions automatically triggers a build workflow
4. The workflow builds the site with MkDocs and deploys to GitHub Pages
5. The site updates in seconds - no manual steps needed

---

## ⚙️ Workflow Details

### Trigger

The deployment workflow (`.github/workflows/deploy-website.yml`) runs automatically:

- **On every push to `main`** (whether from commits or pull requests)
- **On manual trigger** via `workflow_dispatch` (if you need to rebuild manually)

### Build Process

The workflow performs these steps:

1. **Checkout**: Clone the repository with full git history
2. **Python Setup**: Install Python 3.x for running MkDocs
3. **Dependencies**: Install `mkdocs-material` and `pymdown-extensions` (required for the theme and markdown features)
4. **Git Config**: Set up git identity for automated commits on behalf of GitHub Actions
5. **Build & Deploy**: Run `mkdocs gh-deploy --force --remote-branch website`
   - Builds the static HTML site from markdown in `docs/`
   - Deploys built files to the `website` branch (GitHub Pages publishing branch)
   - `--force` overwrites the entire `website` branch with the new build (clean slate each time)

### Deployment Target

The built site is deployed to the **`website` branch**, which is configured as the GitHub Pages source. This means:

- When you view https://SaravananRajaraman.github.io/Prompt2Production/, you're viewing the contents of the `website` branch
- The `website` branch is **fully managed by the automated build** - don't edit files there directly

---

## 📄 What Gets Synced

When the workflow builds and deploys:

| What | Where | How |
|------|-------|-----|
| **Markdown documentation** | `docs/*.md` | Converted to HTML, deployed to root of `website` branch |
| **Examples & samples** | `docs/examples/` | Synced alongside documentation |
| **Site configuration** | `mkdocs.yml` | Controls theme, fonts, nav menu for the deployed site |
| **Theme files** | `docs/css/`, Material theme config | Rendered as part of the site build |

**Nothing else is touched or overwritten.** Only the markdown content and theme-related files are processed.

---

## 🚀 For Contributors

### Making Edits

1. Create or edit markdown files in the `docs/` directory on the `main` branch
2. Commit your changes: `git commit -m "Update documentation about X"`
3. Push to `main`: `git push origin main`
4. **Automation takes over** - GitHub Actions builds and deploys within 1-2 minutes

### What You DON'T Need to Do

- ❌ Don't manually push to the `website` branch
- ❌ Don't run `mkdocs` commands locally (though you can for local testing)
- ❌ Don't edit mkdocs config on the `website` branch

### Testing Locally (Optional)

If you want to preview your changes before pushing:

```bash
# Install MkDocs locally (one time)
pip install mkdocs-material pymdown-extensions

# Build and serve the site locally
mkdocs serve

# Open http://localhost:8000 in your browser
```

Then commit and push - the automated workflow will handle deployment.

---

## 📋 Workflow File Reference

The automation is defined in:

**`.github/workflows/deploy-website.yml`**

Key points:

- **Language**: YAML (GitHub Actions syntax)
- **Trigger**: Runs on `push` to `main` and `workflow_dispatch`
- **Runner**: Ubuntu latest
- **Permissions**: Requires write access to repository contents (for git commits)
- **Deployment method**: `mkdocs gh-deploy --force --remote-branch website`

---

## 🔒 Why `--force`?

The workflow uses the `--force` flag when deploying. This means:

- **Fresh build every time**: The entire `website` branch is overwritten with the newly built site
- **No leftover files**: Old pages that have been deleted from `docs/` are automatically removed from the published site
- **Clean slate**: Prevents stale content or orphaned files from persisting

This is safe and intentional - the `website` branch is *meant* to be fully managed by the build process.

---

## ✅ Verification

After pushing changes to `main`, you can verify the deployment:

1. **Check the Actions tab** on GitHub to see the build/deploy job status
2. **Wait 1-2 minutes** for the build to complete
3. **Visit the live site** at https://SaravananRajaraman.github.io/Prompt2Production/ to confirm changes are live

If the Actions job fails, check the job logs for error messages (usually related to markdown syntax or missing dependencies).

---

## 🤔 FAQs

### Q: Can I revert a published change?
**A:** Yes. Revert the commit on `main`, push, and the automation will redeploy the reverted state. The `website` branch will update accordingly.

### Q: What if I want to make a quick fix without committing?
**A:** You can use the `workflow_dispatch` trigger to manually run the deploy job without code changes (though this isn't usually necessary).

### Q: Can I edit files directly on the `website` branch?
**A:** Technically yes, but don't - they'll be overwritten on the next deploy. Always edit on `main` instead.

### Q: How do I add new pages to the navigation?
**A:** Edit the `nav:` section in `mkdocs.yml` on the `main` branch. The automation will rebuild the navigation menu on the next deploy.

### Q: Is there a delay before changes go live?
**A:** Typically 1-2 minutes for GitHub Actions to run the build and deploy workflow. Once deployed, changes are live instantly.

---

## 🔗 Related Resources

- **[mkdocs.yml](../mkdocs.yml)** - Site configuration (theme, navigation, fonts)
- **[.github/workflows/deploy-website.yml](../.github/workflows/deploy-website.yml)** - The automation workflow
- **[GitHub Pages Documentation](https://docs.github.com/en/pages)** - How GitHub Pages works
- **[MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)** - Documentation about the theme used for this site

---

*Last updated: April 2026 - Automation ensures this documentation hub stays current as you and the community contribute.*
