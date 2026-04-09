---
layout: default
title: Getting Started Primer
nav_order: 1
---

# GitHub Copilot in 5 Minutes - The Three Modes

> **New to GitHub Copilot in VS Code?** This is your fastest entry point. Learn Ask, Plan, and Agent modes, then write your first prompt.

---

## 🚀 The Three Modes: Choose Your Tool

GitHub Copilot works in three distinct modes. Each is designed for a different job. You'll use all three in a typical week, but let's start with the one that feels most natural.

| ASK | PLAN | AGENT |
| --- | --- | --- |
| Quick Q&A | Design First | Autonomous Execution |
| Chat in VS Code | Review Plan | Edits Files |
|  | Approve First, Then Code | Runs Tests, Loops Until Done |
| "Explain this error" | "Design a login page" | "Build a complete user authentication system" |

---

## Mode 1: Ask - Your First Copilot Conversation (2 minutes)

**What it does:** You ask a question; Copilot explains, suggests, or generates code.

**When to use it:**
- ✅ Understand an error message
- ✅ Explain code someone else wrote
- ✅ Quick code snippet generation
- ✅ "What does `reduce()` do?"

### Try It Now

**Step 1:** Open VS Code and install the GitHub Copilot extension (if not already installed).

**Step 2:** Open any file in your project (or create a new `.ts` or `.py` file).

**Step 3:** Open the Copilot Chat panel:
- **Windows/Linux:** Press `Ctrl + I` (or `Ctrl + Alt + I` for inline)
- **Mac:** Press `Cmd + I`

**Step 4:** Type this question:
```
@workspace Explain what this codebase does in 2-3 sentences
```

**Step 5:** Wait for Copilot to respond. You should see:
- A summary of your project structure
- What the main files do
- What technologies are being used

✨ **You just had your first Copilot conversation!**

---

## Mode 2: Plan - Design Before Code

**What it does:** You describe what you want; Copilot creates a step-by-step plan before writing any code.

**When to use it:**
- ✅ Starting a new feature
- ✅ Refactoring a large section
- ✅ Uncertain where to start
- ✅ Need to align with team on approach

### Example Workflow

1. **You describe:** "Add dark mode support to the app"
2. **Copilot generates:** A numbered plan (10 steps)
3. **You review:** "Does this plan make sense?"
4. **You refine:** "Combine steps 3-4" or "Add a step for testing"
5. **You approve:** Click "Implement this plan"
6. **Copilot executes:** Writes code following the plan

**The magic:** You agree *before* code is written. This avoids the common problem where Copilot solves the wrong thing well.

---

## Mode 3: Agent - Let It Work Autonomously

**What it does:** A high-level goal; Copilot autonomously edits files, runs tests, fixes failures, and loops until done.

**When to use it:**
- ✅ Complex multi-file changes
- ✅ Writing test suites
- ✅ Setting up boilerplate
- ✅ Confident in what you want, want faster execution

### Why It's Powerful

Agent mode can:
- Create multiple files and folders
- Run terminal commands (build, tests, install)
- Read test output, see what failed
- Fix the code and re-run tests
- Keep working until tests pass
- All without you leaving the editor

**Note:** Start with Ask or Plan mode. Agent mode is most powerful once you understand what Copilot can do.

---

## 💡 Pro Tips Right Now

| Tip | What It Does |
|-----|-------------|
| **Add `@workspace`** | Copilot includes your entire project, not just current file |
| **Add `@vscode`** | Get answers about VS Code itself (settings, shortcuts, extensions) |
| **Use `/explain`** | Highlight code, then type `/explain` for a dedicated explanation |
| **Type `/tests`** | Copilot generates test files for the current file |
| **Check debug view** | Command Palette → "Toggle Chat Debug View" shows exactly what Copilot saw |

---

## ⚠️ Common First Mistakes

| Mistake | Why It's Wrong | What To Do Instead |
|---------|---|---|
| "Write code for my web app" (too vague) | Copilot doesn't know what you want | "Add a login form with email/password validation" |
| No context provided | Copilot can't see your codebase | Use `@workspace` or highlight relevant files |
| Asking in a new chat for continued work | Context gets lost | Keep asking in the same conversation thread |
| Expecting perfect code first time | AI is great but not magic | Use Ask mode to explain issues, iterate with Plan mode |
| Trusting every suggestion | Some suggestions might miss edge cases | Always review; test before shipping |

---

## 🎯 Your Next Step

**Choose your path:**

- **Path 1 (I want quick answers):** → [FAQ_For_Beginners.md](FAQ_For_Beginners.md) - Common questions answered in 1-2 sentences
- **Path 2 (I want structured learning):** → [Learning_Paths.md](Learning_Paths.md) - Choose based on your goal
- **Path 3 (I want hands-on tutorials):** → [Tutorials_Hands_On.md](Tutorials_Hands_On.md) - Step-by-step walkthroughs
- **Path 4 (I want deep technical understanding):** → [Session1_Building_The_Foundation.md](Session1_Building_The_Foundation.md) - Full theory and practice

---

## 📚 Still Have Questions?

- **"When should I use Plan vs Agent?"** → [FAQ_For_Beginners.md](FAQ_For_Beginners.md#when-should-i-use-plan-vs-agent)
- **"My Copilot suggestion looks wrong. What do I do?"** → [FAQ_For_Beginners.md](FAQ_For_Beginners.md#my-suggestion-looks-wrong-what-do-i-do)
- **"Can I customize Copilot for my team?"** → [Session1_Building_The_Foundation.md](Session1_Building_The_Foundation.md#part-5-custom-instructions) *(Advanced)*
- **"All the links in one place"** → [All_Links.md](All_Links.md)

---

**Ready?** Open VS Code, press `Ctrl+I` (or `Cmd+I`), and ask Copilot a question. You're already using it. 🚀
