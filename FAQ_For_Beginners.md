# FAQ for GitHub Copilot Beginners

> Quick answers to the questions new Copilot users ask most often. Practical, jargon-free, actionable.

---

## 🚀 Getting Started

### Q: I've never used GitHub Copilot. Where do I start?

**A:** Start here → [Getting_Started_Primer.md](Getting_Started_Primer.md). Read it in 5 minutes, then try Ask mode. That's it.

After that, choose a [Learning_Path](Learning_Paths.md) based on what you want to learn.

---

### Q: Do I need to install anything special?

**A:** You need:
1. VS Code (free)
2. GitHub Copilot extension (free with GitHub account, or paid subscription for more usage)
3. A GitHub account (free)

That's it. Install the extension from the VS Code marketplace and sign in with GitHub.

---

### Q: Is GitHub Copilot the same as ChatGPT?

**A:** No, but they use similar AI models under the hood.

**Difference:**
- **ChatGPT**: Web-based chat, general purpose, doesn't see your code
- **Copilot**: Built into VS Code, sees your codebase, context-aware, designed for coding

Think of it as ChatGPT+context+IDE integration.

---

## 💬 Ask Mode

### Q: What does "Ask Mode" mean?

**A:** It's just chat with Copilot, right in VS Code. You type a question; it replies. Like texting a coding expert sitting next to you.

### Q: How do I open Ask Mode?

**A:**
- **Windows/Linux:** Press `Ctrl + I` (in-editor) or `Ctrl + Alt + I` (inline)
- **Mac:** Press `Cmd + I`

Or click the Copilot icon in the activity bar (left sidebar of VS Code).

---

### Q: When should I use Ask Mode?

**A:** Use Ask when you need **quick answers**:
- ✅ "What does this error mean?"
- ✅ "Explain how Promise.all() works"
- ✅ "Write a regex for email validation"
- ✅ "How do I test async code?"

**Don't use Ask for:** Big features or multi-file refactors → use Plan or Agent instead.

---

### Q: My suggestion looks wrong. What do I do?

**A:** Three options:

1. **Ask for clarification:** Type "Why did you suggest X? Wouldn't Y be better?" and iterate.
2. **Provide more context:** Type your question again with more details: "@workspace where do we handle authentication in this codebase?"
3. **Use debug view:** Command Palette → "Toggle Chat Debug View" to see exactly what Copilot saw.

**Rule of thumb:** If it looks wrong, it probably is. Always review and test before shipping.

---

### Q: What does `@workspace` do?

**A:** It tells Copilot to include your **entire project** in context, not just the current file.

**Examples:**
- `@workspace what authentication pattern do we use?` - Copilot searches all your code
- `@workspace where should I add a dark mode toggle?` - Copilot understands your full structure

Use `@workspace` when you need project-wide context.

---

## 📋 Plan Mode

### Q: What's the difference between Ask and Plan?

**A:**

| Ask | Plan |
|-----|------|
| "Quick answer" | "Create a detailed roadmap" |
| You see a response | You see numbered steps to follow |
| Immediate | Slower, more thorough |
| Single question | Multi-phase workflow |
| **Use for:** Quick code snippets | **Use for:** Feature design |

---

### Q: When should I use Plan Mode?

**A:** Use Plan when:
- ✅ Starting a new feature and uncertain how to approach it
- ✅ Refactoring a large section and want to align first
- ✅ You want Copilot to think through the whole approach before coding
- ✅ You want to review and approve before implementation

**Don't use Plan for:** Small, obvious changes (Ask mode is faster).

---

### Q: How do I use Plan Mode?

**A:**

1. Open chat (Ctrl+I)
2. Type: `/plan` (slash-plan)
3. Describe what you want: "Add a dark mode toggle to the settings page"
4. Review the numbered plan Copilot creates
5. Ask for changes if needed: "Can you combine steps 3 and 4?"
6. Click "Approve plan" or "Implement this plan"
7. Copilot writes the code

---

### Q: Can I edit the plan after Copilot generates it?

**A:** Yes! That's the whole point of Plan mode. If the plan doesn't look right, tell Copilot:
- "Reverse the order of steps 2 and 3"
- "Add a step for writing tests"
- "Don't use Redux; use Context API instead"

Edit the plan until you agree with it, then approve.

---

## 🤖 Agent Mode

### Q: What's Agent Mode?

**A:** Copilot works autonomously. You give a high-level goal; it:
- Creates/edits files
- Runs terminal commands
- Sees the output
- Fixes errors
- Keeps looping until done

You stay in the editor, reviewing each decision.

---

### Q: When should I use Agent Mode?

**A:** Use Agent when:
- ✅ Complex multi-file changes (entire feature, refactor)
- ✅ Writing test suites
- ✅ Creating boilerplate scaffolding
- ✅ You're confident what you want, just want faster execution
- ✅ Task requires running commands (tests, builds, installs)

**Don't use Agent for:** Simple one-file changes (Ask mode is faster).

---

### Q: Is Agent Mode safe? Can it break my code?

**A:** Agent mode is safe-ish:
- ✅ It can only edit files you open in VS Code
- ✅ You review every change before it's committed
- ✅ You can undo (Ctrl+Z)
- ✅ You can stop it at any time

**Recommendation:** Commit your code before using Agent mode, so you can revert if something goes wrong.

---

### Q: How do I use Agent Mode?

**A:**

1. Open chat (Ctrl+I)
2. Press Ctrl+I again or click the "Agent" button
3. Describe what you want: "Create a new API endpoint for user login"
4. Review each change Copilot suggests
5. Click "Approve" or "Make change"
6. Let it work; it handles multiple files, tests, etc.

---

## 🔧 Customization & Advanced

### Q: Can I customize Copilot for my team?

**A:** Yes! This is advanced but powerful:

- **Custom Instructions** (`.instructions.md`) - Tell Copilot your coding style, practices, tech stack
- **Prompt Files** (`.prompt.md`) - Reusable templates for common tasks
- **Custom Agents** (`.agent.md`) - Specialized AI personas for different roles (Security agent, Testing agent, etc.)

**Example:** Create a `.instructions.md` file in your project root:

```markdown
# Project: E-Commerce Backend

## Stack
- Node.js 18, Express.js, TypeScript strict mode
- Database: PostgreSQL with Prisma ORM
- Testing: Jest with 80%+ coverage requirement

## Code Standards
- All API responses use { data, error } shape
- Error handling: never throw, always return error in response
- All functions: JSDoc comments required
- All routes: must have authorization checks

## Naming Conventions
- Database tables: plural (users, products, orders)
- API endpoints: RESTful (POST /users, GET /users/:id)
- Environment variables: SCREAMING_SNAKE_CASE
```

**Result:** Every time you ask Copilot for code, it automatically follows these standards without you typing them each time.

---

### Q: What's "Context Engineering"?

**A:** Fancy way of saying: **designing what Copilot sees** to get better results.

Simple example:
- ❌ Bad: "Write a function" (Copilot doesn't know your style)
- ✅ Good: "Write a function using TypeScript with error handling and JSDoc comments, following our team's naming conventions" (Copilot knows exactly what you want)

More context → better, faster suggestions.

---

### Q: What's "Context Rot"?

**A:** When your chat conversation gets so long that:
1. Old messages aren't relevant anymore
2. Copilot gets confused (too much to read)
3. Responses slow down
4. Quality degrades

**Solution:** Start a fresh chat after ~20-30 exchanges. Real work typically spans multiple focused chats, not one epic conversation.

---

## 🐛 Troubleshooting

### Q: Copilot is giving me bad suggestions. How do I fix it?

**A:** Try these (in order):

1. **Be more specific:** Instead of "write a function," say "write a function that validates email format using regex"
2. **Add context:** Use `@workspace` to give project context
3. **Reference files:** Type `#file:config.ts` to tell Copilot to include that file
4. **Check debug view:** Command Palette → "Toggle Chat Debug View" to see what Copilot actually sees
5. **Start fresh chat:** If the conversation is long, start a new one

---

### Q: Copilot won't load. What's wrong?

**A:** Check:
- ✅ GitHub Copilot extension is installed
- ✅ You're signed in (Copilot icon shows your avatar)
- ✅ You have an active GitHub Copilot subscription (or free trial)
- ✅ Your internet connection is working
- ✅ Try restarting VS Code

Still broken? Check the official [GitHub Copilot Status Page](https://www.githubstatus.com/).

---

### Q: Can I use Copilot offline?

**A:** No. Copilot requires internet to communicate with GitHub's servers. It's cloud-based.

---

## � POWER Framework Examples

### Example 1: Bad vs. Good Prompt

**❌ Bad (vague):**
```
Write a function
```

**✅ Good (POWER applied):**
```
You are a senior backend engineer. Write a TypeScript function that validates HTTP request headers for security.
The function should check for: Content-Type, Authorization, and X-Request-ID headers.
It should throw an error if any required header is missing.
Use strict TypeScript types. Include JSDoc comments.
Return a boolean indicating whether all headers are valid.
```

**What changed:**
- **P (Purpose):** Specific goal = validate HTTP headers
- **O (Operating Context):** Backend engineer, TypeScript, HTTP requests
- **W (What Constraints):** Check specific headers, throw on missing, strict types
- **E (Expected Format):** Boolean return, JSDoc comments
- **R (Role & Tone):** Senior engineer mindset

### Example 2: Real-World POWER Prompt

**Scenario:** You want to refactor a messy authentication function

**❌ Without POWER:**
```
Fix this authentication code
```

**✅ With POWER:**
```
You are a security-focused TypeScript architect. I need to refactor this authentication function following JWT best practices.

Context: We're using Express.js with Node.js 18, PostgreSQL for user storage, and jsonwebtoken v9.

Constraints:
- Must validate JWT tokens
- Must handle expired tokens gracefully  
- Must check user roles (admin, user, guest)
- Security: never expose secret keys in logs
- Use TypeScript strict mode

Expected output: Refactored function with:
1. Type-safe JWT payload
2. Error handling for each failure case
3. JSDoc explaining parameters and return types

Role: Think like someone implementing OAuth2 standards, not a quick-and-dirty solution.
```

**Result:** Copilot now generates production-grade code instead of a hack.

### Example 3: Using POWER in Plan Mode

**The scenario:** You want to add dark mode to your React app

**❌ Without structure:**
```
Add dark mode
```

**✅ With POWER (in Plan mode, type `/plan` first):**
```
You are a senior React architect. Plan how to add dark mode to our Next.js 14 app.

Context:
- Frontend: Next.js 14 with App Router
- Styling: Tailwind CSS
- State management: React Context API
- Target browsers: Chrome, Firefox, Safari (last 2 versions)

Constraints:
- Must persist user preference to browser localStorage
- Must respect system dark mode preference as default
- Must not cause flash of wrong theme on page load  
- All pages must support both light and dark modes

Expected output: A numbered implementation plan with:
1. Setup steps first
2. Component changes
3. Testing steps
4. Deployment considerations

Role: Think like you're planning this for a large team, with details a junior dev can follow.
```

Copilot now generates a clear, step-by-step, team-ready plan.

---

### Q: Is there a structured learning path?

**A:** Yes! See [Learning_Paths.md](Learning_Paths.md) for three paths:
- "I'm brand new" - Start simple, build skills
- "I want advanced stuff" - Skip basics, jump to orchestration
- "I want quick answers" - FAQ-focused

---

### Q: Where can I find more examples and tutorials?

**A:** Check:
1. [Getting_Started_Primer.md](Getting_Started_Primer.md) - 5-minute intro
2. [Tutorials_Hands_On.md](Tutorials_Hands_On.md) - Step-by-step walkthroughs
3. [Session 1: Building the Foundation](Session1_Building_The_Foundation.md) - Deep dives
4. [All_Links.md](All_Links.md) - Curated reference links

---

### Q: How do I know if I'm using Copilot well?

**A:** Good signs:
- ✅ You're getting relevant suggestions in 2-3 tries max
- ✅ You understand why Copilot made each suggestion
- ✅ You're using different modes (Ask, Plan, Agent) for different jobs
- ✅ You're iterating: "That's close, but change X to Y"
- ✅ You rarely ask the same question twice

If you're struggling, see ["My suggestion looks wrong"](#my-suggestion-looks-wrong-what-do-i-do) above.

---

## 📞 Still Stuck?

- **Ask in the chat itself:** Type your problem; Copilot can often debug itself
- **Check the debug view:** Command Palette → "Toggle Chat Debug View"
- **Read [Session 1](Session1_Building_The_Foundation.md)** for deeper understanding
- **Explore [All_Links.md](All_Links.md)** for official documentation

---

**Remember:** Copilot is a tool. Like any tool, the first month involves learning. After that, you'll wonder how you coded without it. 🚀
