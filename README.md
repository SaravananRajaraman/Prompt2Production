# Prompt2Production

> **"Low Code or No Code" · "Prompt to Production"**

Welcome to the **Prompt2Production** repository! This project contains comprehensive guides, hands-on tutorials, and reference materials for **mastering GitHub Copilot** - from your first prompt to building production workflows with multi-agent orchestration.

---

## 🎯 Where Do I Start?

**Pick your path:**

| I'm... | Start here |
|--------|-----------|
| **Completely new to Copilot** | → [Getting Started Primer](./docs/Getting_Started_Primer.md) (5 min) |
| **Already using Ask mode** | → [Learning Paths](./docs/Learning_Paths.md#path-2-level-up-ask-to-agent) |
| **Want quick answers to specific questions** | → [FAQ for Beginners](./docs/FAQ_For_Beginners.md) |
| **Ready for hands-on tutorials** | → [Hands-On Tutorials](./docs/Tutorials_Hands_On.md) |
| **Want advanced workflows & customization** | → [Learning Paths](./docs/Learning_Paths.md#path-3-advanced-workflows) → [Session 2](./docs/Session2_Advanced_Agent_Capabilities.md) |

---

## 📚 All Materials

### 🟢 Beginner-Friendly Entry Points

These are designed for people who are new to Copilot. Start here.

- **[Getting Started Primer](./docs/Getting_Started_Primer.md)** - The three modes in 5 minutes. Visual, quick, actionable.
- **[FAQ for Beginners](./docs/FAQ_For_Beginners.md)** - Quick answers to the 20 most common questions.
- **[Learning Paths](./docs/Learning_Paths.md)** - Choose your adventure. Three paths from beginner to advanced.
- **[Hands-On Tutorials](./docs/Tutorials_Hands_On.md)** - Learn by doing. Three guided walkthroughs (Ask, Plan, Agent modes).

### 🔵 Foundation & Conceptual Understanding

For people ready to understand *how* Copilot works and *why*.

- **[Session 1: Building the Foundation](./docs/Session1_Building_The_Foundation.md)** `[FOUNDATIONAL]`  
  The complete foundation layer: three interaction modes (Ask, Plan, Agent), context engineering, POWER prompting framework, and the three customization primitives (Custom Instructions, Prompt Files, Custom Agents).
  
  **Key sections:**
  - Part 1: The Three Interaction Modes
  - Part 2: Chat Context and POWER Framework
  - Part 3: Context Engineering (What You See Is What You Get)
  - Part 4: Building Your System Prompt

### 🔴 Advanced & Production Workflows

For people ready to orchestrate teams of AI agents and build production systems.

- **[Session 2: Advanced Agent Capabilities](./docs/Session2_Advanced_Agent_Capabilities.md)** `[ADVANCED]`  
  Build at scale: sub-agents, agent orchestration patterns, handoffs, Agent HQ, custom agent frontmatter, agent skills, and lifecycle governance with hooks.
  
  **Key sections:**
  - Part 1: Sub-Agents & Orchestration
  - Part 2: Custom Agent Frontmatter (Full Reference)
  - Part 3: Handoffs & Workflows
  - Part 4: Multi-Agent Patterns (Coordinator + Workers, Parallel Analysis)

### 🔗 Reference

- **[All Links & References](./docs/All_Links.md)** - Curated links to official GitHub Copilot docs, context engineering deep reads, community resources, and learning hubs.

---

## 🚀 Recommended Learning Paths

Choose based on your goal:

### Path 1: I'm Brand New
```
5 min:  Getting Started Primer
10 min: Try Tutorial 1 (Ask mode)
15 min: FAQ for Beginners (skim for your questions)
30 min: [OPTIONAL] More tutorials or Session 1 Part 1-2
```
**Result:** You can ask Copilot questions, understand the three modes, and feel confident using Ask mode daily.

### Path 2: I Know Ask Mode; I Want to Level Up
```
30 min: Session 1 - Part 2 (Chat Context & POWER Framework)
30 min: Tutorial 2 (Plan mode)
30 min: Tutorial 3 (Agent mode)
20 min: Session 1 - Part 3 (Context Engineering)
```
**Result:** You understand all three modes, can design features with Plan mode, run complex tasks with Agent mode, and know why context matters.

### Path 3: I Want Advanced Workflows
```
1 hour: Session 1 (full read)
1 hour: Session 2 - Part 1 (Sub-Agents & Orchestration)
30 min: Session 2 - Part 2 (Custom Agent Frontmatter)
30 min: Create your first custom agents (`.agent.md` files)
```
**Result:** You can orchestrate teams of specialized AI agents, build production workflows with quality gates, and customize Copilot for your team.

### Path 4: I Just Want Answers
```
Open: FAQ for Beginners
Ctrl+F: Your question
30 sec: Read the answer
```
**Result:** Quick answer to your specific question.

---

## ✨ What's Unique About This Repository

| Aspect | What's Here |
|--------|-----------|
| **Beginner-focused** | Primer, FAQ, tutorials - designed for first-time users, not just power users |
| **Progressive complexity** | Start with 5-min overview, build to multi-agent orchestration |
| **Hands-on** | Tutorials include step-by-step walkthroughs you can run today |
| **Comprehensive** | Everything from "What is Copilot?" to enterprise orchestration patterns |
| **Well-organized links** | 50+ curated reference links, sorted by topic |

---

## 💡 Key Concepts Covered

- **The three interaction modes:** Ask (chat), Plan (design first), Agent (autonomous execution)
- **Context engineering:** Designing what the AI sees to get better results
- **POWER framework:** Purpose, Operating Context, What Constraints, Expected Format, Role
- **Custom Instructions** (``.instructions.md``) - persistent background knowledge
- **Prompt Files** (`.prompt.md`) - reusable workflow templates
- **Custom Agents** (`.agent.md`) - specialized AI personas with their own tools and instructions
- **Sub-agents & orchestration** - coordinating teams of AI specialists
- **Handoffs** - sequential, approved workflows with clickable transitions
- **Agent HQ & background sessions** - managing multiple agent runs
- **Quality gates & hooks** - governing agent execution for security and compliance

---

## 📖 Best Practices

1. **Start with the Primer if you're new** - Don't jump to Session 1 if you're unfamiliar with Copilot
2. **Follow learning paths in order** - They're designed to build on each other
3. **Do the tutorials, don't just read them** - Open VS Code and try it
4. **Use the FAQ to answer specific questions** - Faster than reading full sessions
5. **Come back to this README as a map** - It's your north star for navigation

---

## 🎓 Time Investment

| Goal | Time | Starting Point |
|------|------|---|
| Understand what Copilot is | 5 min | Primer |
| Use Ask mode effectively | 15 min | Primer + Tutorial 1 |
| Use all three modes | 1 hour | Tutorials 1-3 + FAQ |
| Deep technical understanding | 2 hours | Session 1 (full) |
| Advanced workflows & orchestration | 3-4 hours | Session 1 + Session 2 |
| Answer a specific question | 2 min | FAQ |

---

## 🔗 Navigation

Inside each file, you'll find links to related sections. For example:
- Session 1 links to Session 2 for advanced topics
- FAQ links to tutorials for hands-on practice
- Learning Paths links to all the materials you need

**Jump around as needed.** You don't have to read linearly.

---

## 🔄 Branch Sync: Main to Website

This repository uses two branches:

- **`main`** - Source of truth for all documentation (`docs/` + `README.md`)
- **`website`** - GitHub Pages publishing branch with Jekyll configuration and custom theme

### Automatic Sync

The `website` branch automatically syncs documentation updates from `main` via a GitHub Actions workflow:

- **Trigger:** Every push to `main` that modifies `docs/` or `README.md`
- **What syncs:** 
  - All markdown files from `docs/` (renamed to root level for GitHub Pages)
  - `README.md` from root
  - `examples/` directory structure
- **What's preserved:** 
  - `_config.yml` (Jekyll configuration)
  - `_includes/` (custom HTML templates)
  - `assets/` (custom CSS/JS and theme files)
  - All other website customizations

### Manual Sync (For Testing or Offline Use)

If you need to sync manually, two scripts are provided:

#### Option 1: Python Script (Cross-Platform)
```bash
# Install none required - uses Python standard library
python sync-branches.py
```

This script:
- Automatically switches to the website branch
- Syncs all docs/ files from main
- Updates README.md
- Commits and pushes changes
- Returns to your original branch

#### Option 2: Bash Script (Linux/macOS/Git Bash)
```bash
bash sync-branches.sh
```

Same functionality as the Python script, written in bash for environments without Python.

### How the Sync Works

1. **File Migration**: Files in `main`'s `docs/` directory are copied to `website`'s root level
   - `main/docs/Getting_Started_Primer.md` → `website/Getting_Started_Primer.md`
   - This respects the website branch's deliberate reorganization for GitHub Pages
   
2. **Structure Preservation**: The website branch keeps its Jekyll configuration intact
   - `website/_config.yml` - never overwritten
   - `website/assets/`, `website/_includes/` - never touched
   - `website/docs/examples/` - synced but kept separate

3. **Conflict Prevention**: Only content files sync; website configuration is always preserved

### What to Do After Making Changes

#### On the `main` branch:
- Edit markdown files in `docs/`
- Update `README.md` at root level
- Commit and push to `main`
- GitHub Actions automatically syncs to `website` ✨

#### On the `website` branch:
- Edit Jekyll configuration (`_config.yml`)
- Customize theme files (`assets/`, `_includes/`)
- Customize `README.md` if webpage-specific changes are needed
- **Note:** Content changes on website branch will be overwritten next time main syncs - keep content edits on `main` only

---

## 🤝 Contributing

Found an error? Room for improvement? Feel free to suggest enhancements.

---

## 📝 Last Updated

April 2026 - Updated with beginner-friendly content, learning paths, and hands-on tutorials.

---

## 🚀 Ready?

Pick a starting point from the table above and dive in. You'll be surprised how quickly you go from "What is Copilot?" to building real features with AI assistance. Happy learning!
