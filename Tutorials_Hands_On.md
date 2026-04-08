# Hands-On Tutorials: Learn by Doing

> Three guided walkthroughs. You'll learn GitHub Copilot by actually using it. Each tutorial is 10-15 minutes.

---

## Tutorial 1: Ask Mode - Explain Code You Don't Understand

> **Goal:** Learn Ask mode by explaining existing code  
> **Duration:** 10 minutes  
> **Difficulty:** Beginner  
> **What you'll learn:** How to read code context, add `@workspace`, iterate on questions

### Setup
1. Open any project in VS Code (or use your current one)
2. Find a file with code you've never seen before or half-remember
3. Highlight 5-10 lines of that code

### Step 1: Ask Copilot to Explain (2 min)

Open the chat panel: **Ctrl+I** (Windows/Linux) or **Cmd+I** (Mac)

Copy this prompt:
```
Explain what this code does in plain English. Assume I'm new to this codebase.
```

Paste it into the chat. Your highlighted code will be included automatically.

**Expected output:** 2-3 sentences explaining the code, in simple language.

### Step 2: Ask a Follow-Up Question (3 min)

In the same chat (don't start a new one), ask:
```
Why would we use a try/catch here instead of just calling the function directly?
```

Copilot should reference the specific code and explain the design choice.

**Expected output:** Explanation of error handling, with examples.

### Step 3: Explore Project Context (3 min)

Ask:
```
@workspace Where else in this codebase is this same pattern used? Show me 3 examples.
```

The `@workspace` tells Copilot to search your entire project.

**Expected output:** List of 3 files where the same pattern appears.

### Step 4: Deepen Your Understanding (2 min)

Ask:
```
Give me a step-by-step explanation of what happens when this function is called.
```

**Expected output:** Numbered list of steps, line by line.

### ✅ You Just Did
- Opened Ask mode and asked a question
- Used context (highlighted code)
- Followed up in the same conversation
- Used `@workspace` for project-wide search
- Iterated to deepen understanding

**Next step:** Try this with real code in your codebase today.

---

---

## Tutorial 2: Plan Mode - Design a Feature Before Code

> **Goal:** Learn Plan mode by designing a new feature end-to-end  
> **Duration:** 15 minutes  
> **Difficulty:** Intermediate  
> **What you'll learn:** How to structure a plan, refine steps, and execute with approval

### Setup
1. Think of a small feature for your project (something that would take 2-4 hours normally)
2. Examples:
   - "Add a dark mode toggle to the settings page"
   - "Create an API endpoint for user login"
   - "Build a search bar that filters results in real-time"
   - "Add email notification preferences"

### Step 1: Open Plan Mode (1 min)

Open chat: **Ctrl+I**

Type:
```
/plan
```

Copilot will activate Plan mode (you'll see a different interface or indicator).

### Step 2: Describe What You Want (2 min)

Type your feature request in plain English:
```
Add a dark mode toggle to the settings page that persists in localStorage. 
When dark mode is enabled, apply dark CSS themes across the whole app.
```

**What to include:**
- What feature (dark mode toggle)
- Where it goes (settings page)
- How it behaves (persists in localStorage)
- What it affects (whole app)

Press Enter or send.

### Step 3: Review the Plan (2 min)

Copilot will generate a numbered plan with steps like:
```
1. Create a theme context provider
2. Add dark/light CSS variables
3. Create ToggleDarkMode component
4. Wire component to localStorage
5. Apply theme on app load
...
```

**Your job:** Read and judge. Does this make sense? Would you do it differently?

### Step 4: Refine the Plan (3 min)

Ask Copilot to adjust:
```
Can you add a step for writing unit tests?
```

Or suggest a different approach:
```
Instead of localStorage, let's use the server API to persist user preference.
Revise the plan.
```

Or reorder:
```
Move step 5 (apply theme on app load) to step 2, right after creating the context.
```

**Keep refining until the plan makes sense to you.**

### Step 5: Approve and Execute (3 min)

When the plan looks good, tell Copilot:
```
Approve this plan. Please implement all steps.
```

Or look for a button like "Mark as Approved" or "Implement Plan."

Copilot will begin writing code following the steps.

### Step 6: Monitor Execution (4 min)

As Copilot works through each step:
- Review the code it's writing
- Approve each change or ask for adjustments
- Watch the test output if it runs tests
- Stop it if you see something wrong

**You're not forced to approve everything.** Stop and ask for changes if needed.

### ✅ You Just Did
- Opened Plan mode
- Clearly described a feature
- Reviewed and refined a plan
- Approved before implementation
- Watched code get written to spec

**The magic:** You agreed on approach before code. No wasted work.

---

---

## Tutorial 3: Agent Mode - Let Copilot Execute Autonomously

> **Goal:** Learn Agent mode by delegating a full task  
> **Duration:** 10-15 minutes  
> **Difficulty:** Intermediate  
> **What you'll learn:** How Agent mode works autonomously, when to intervene

### Setup
1. Choose a small, well-defined task that Agent can complete:
   - "Create a utility function for converting dates to format MM/DD/YYYY with full test coverage"
   - "Add a `.env.example` file with all required environment variables"
   - "Create an API response handler that catches common errors"
   - "Write a unit test file for the authentication module"
2. Make sure your code is on `git` and clean (no uncommitted changes)

### Step 1: Open Agent Mode (1 min)

Open chat: **Ctrl+I**

Look for an **Agent button** or type:
```
Let me use agent mode.
```

(The exact method depends on your VS Code version. Check the UI for "Agent" button.)

### Step 2: Give a Clear Goal (2 min)

Type:
```
Create a utility function that converts UTC timestamps to human-readable format (e.g., "2 hours ago", "yesterday", "March 5, 2024"). 
Include full JSDoc comments. 
Write comprehensive unit tests.
Place in src/utils/time.ts.
```

**What to include:**
- Exact task (what you want built)
- Any tech preferences (utility library? vanilla JS? TypeScript?)
- Where to put it (file path)
- Any standards (tests, comments, format)

Press Enter or send.

### Step 3: Review Each Decision (5-10 min)

Agent will work through these steps (you might see them as they happen):

1. **Create file** - You see: "I'm creating `src/utils/time.ts`"  
   - Action: Approve or ask "Make sure it uses moment.js"

2. **Write function** - You see the code  
   - Action: Review. If it looks right: Approve. If it's missing edge cases: Ask "Add error handling for null timestamps"

3. **Write tests** - You see test file  
   - Action: Review. Ask for more coverage if needed

4. **Run tests** - You see terminal output  
   - If tests pass: Agent closes the task  
   - If tests fail: Agent diagnoses and fixes

5. **Iterate** - If something fails, Agent tries again. You can stop it or guide it.

### Step 4: Review the Result (2 min)

When Agent finishes, you'll see:
- Files created/modified
- A summary of what was built
- Any warnings or caveats

**Check:**
- Are the files in the right place?
- Is the code quality acceptable?
- Do the tests pass?
- Is it ready to commit?

### Step 5: Commit (1 min)

If everything looks good:
```bash
git add .
git commit -m "feat: add time format utility with tests"
```

If something's wrong:
```bash
git reset
```

Copilot can try again.

### ✅ You Just Did
- Opened Agent mode
- Gave a clear, end-to-end task
- Reviewed and approved each step
- Let Copilot loop until tests passed
- Got a complete, tested feature

**The power:** Multi-file changes, tests, refactoring - all without leaving the editor.

---

---

## 🎯 What's Next?

After these three tutorials, you're ready to:

1. **Ask mode daily** - Explain errors, understand APIs, generate snippets
2. **Use Plan mode for features** - Design first, code second, collaborate
3. **Deploy Agent mode** - Complex refactors, test suites, multi-file changes
4. **Read Session 1** - Deep technical understanding
5. **Customize Copilot** - Make it work your way ([Path 3 in Learning_Paths.md](Learning_Paths.md#path-3-advanced-workflows))

---

## 💡 Pro Tips While Working

| Tip | Why It Matters |
|-----|---|
| **Use the debug view** | Confused by Copilot's response? Command Palette → "Toggle Chat Debug View" to see exactly what it saw |
| **Keep chats focused** | One question per chat (or 5-6 related follow-ups max). Long chats get slow. |
| **Give context** | Use `@workspace` when you need project overview, `#file:name.ts` for specific files |
| **Review before shipping** | Don't trust any suggestion 100%. Read the code, understand it, test it. |
| **Ask for iteration** | "That's close, but change X to Y" is faster than starting over |

---

## 🚀 Ready?

Pick one tutorial and run through it today. You'll be surprised how much you learn by just *doing* it.

Start with **Tutorial 1** (Ask mode) - it's the fastest and builds confidence.
