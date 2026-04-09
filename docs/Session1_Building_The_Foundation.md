---
layout: default
title: Session 1 - Building the Foundation
nav_order: 3
---

# Session 1: Building the Foundation

`[FOUNDATIONAL]` - Start here if you're learning Copilot. Master the basics before moving to Session 2.

> **"Low Code or No Code" · "Prompt to Production"**
>
> This session covers the complete foundation layer of GitHub Copilot - the three interaction modes, how the context window is assembled, and the three primitives you use to engineer it. Master these and everything else in your AI development workflow becomes easier, faster, and more predictable.

ℹ️ **New to Copilot?** Start with [Getting_Started_Primer.md](./Getting_Started_Primer.md) instead. Come back here once you've tried the three modes.

---

## What You Will Learn

- The **three interaction modes** - Ask, Plan, and Agent - and when to use each
- How to control what Copilot sees using chat context, the POWER framework, and the debug view
- The **context engineering** discipline: designing what the model sees, not just what you say
- How the four-layer context window is assembled before your message reaches the model
- **Custom Instructions** - persistent background knowledge injected on every request
- **Prompt Files** - reusable workflow templates invoked with a slash command
- **Custom Agents** - persona + tools + workflow definitions for consistent behaviour
- The context window budget, **context rot**, and practical strategies to design around both

---

## Part 1: The Three Interaction Modes

Before diving into the mechanics of how Copilot assembles its context, you need to know the three fundamental ways to interact with it. Every tool has a mode for every job - these are GitHub Copilot's.

### Ask Mode - Instant Answers in Your Editor

Ask mode is a conversational interface. You type a question or highlight a block of code, and Copilot responds with an explanation, suggestion, or code snippet inline. It reads your current file, imports, and open tabs as implicit context.

**How to use it:**
1. **Open chat:** Press `Ctrl+I` (Windows/Linux) or `Cmd+I` (Mac)
   - Alternative: Click the Copilot icon in the VS Code activity bar (left sidebar)
   - For inline chat: Press `Ctrl+Alt+I` (Windows/Linux) or `Cmd+Alt+I` (Mac)
2. Type a natural-language question
3. Copilot reads the active file and any referenced context
4. Receive an explanation, fix, or generated snippet
5. Follow up with refinements in the same thread

**Best use cases:**
- Explain unfamiliar code or error messages
- Understand library APIs without leaving the editor
- Write unit test descriptions or generate regex patterns
- Quick one-shot code generation for small tasks

💡 **Pro Tip:** Add `@workspace` to your question to search your entire project, not just the current file. Example: `@workspace where do we handle authentication?`

---

### Plan Mode - Design First, Code Second

Plan mode separates thinking from doing. You describe what you want to build, and Copilot produces a step-by-step implementation plan you can review before a single line of code is written. This mode prevents scope creep and keeps the implementation grounded in an agreed approach.

**The four-step flow:**

| Step | What Happens |
|------|-------------|
| **1. Describe** | Write your feature or problem in plain English |
| **2. Review Plan** | Copilot generates a step-by-step implementation plan |
| **3. Refine** | Adjust, re-order steps, or ask Copilot to reconsider alternatives |
| **4. Execute** | Approve and let Copilot scaffold the code |

> **Rule:** Always agree on the implementation plan before Copilot writes a single line of code. This single habit eliminates the most common AI coding frustration - the model solving the wrong problem well.

---

### Agent Mode - Autonomous Multi-Step Execution

Agent mode is the most powerful. You hand Copilot a high-level goal; it autonomously edits files, runs terminal commands, reads test output, fixes failures, and loops until the task is done. You stay in the editor reviewing each decision.

**What Agent mode can do autonomously:**
- Create new files, folders, and boilerplate scaffolding
- Refactor and modernise code across the full codebase
- Write complete test suites, run them, and fix failures until they pass
- Execute build and install commands without you switching contexts

**The three-level comparison:**

| Feature | Ask Mode | Plan Mode | Agent Mode |
|---------|----------|-----------|-----------|
| Interaction | Conversational Q&A | Structured planning | Autonomous execution |
| Best for | Quick questions & explanations | Feature design & architecture | Multi-file tasks & refactors |
| Output | Text answers & snippets | Ordered task list | Working code changes |
| Control level | High - you decide all edits | Medium - you approve plan | Lower - Copilot drives |
| Ideal when | Stuck on a concept or bug | Starting a new feature | Implementing known design |

---

### The Daily Development Cycle

The three modes are designed to work together. A typical feature will flow through all three:

```
Explore (Ask) → Design (Plan) → Build (Agent) → Review (Ask)
```

1. **Ask**: Explain unfamiliar APIs, understand error messages, brainstorm approaches
2. **Plan**: Walk through the implementation steps before any code is written
3. **Agent**: Scaffold files, write functions, run tests, fix failures
4. **Ask** again: Review diffs, explain what changed, write documentation or commit messages

This cycle is repeatable. Start any feature with Ask, design with Plan, build with Agent, then loop back to Ask to review and document.

---

## Part 2: Chat Context and Prompting

### Controlling What Copilot Sees

When you send a message, VS Code automatically includes implicit context (the active file, selected text, current editor state). But you can be deliberate about what else you add.

| Syntax | What It Does |
|--------|--------------|
| `/` (slash) | Invoke a prompt file or built-in command (e.g., `/fix`, `/explain`, `/tests`) |
| `#` (hashtag) | Reference a specific file, symbol, or variable (e.g., `#file:server.ts`, `#selection`) |
| `@` (at) | Reference a chat participant for domain-specific context (e.g., `@workspace`, `@vscode`) |

> **Context window awareness:** Every piece of context you attach consumes tokens from the model's context budget. Add what is relevant; skip what is not. More context is not always better - irrelevant content dilutes the model's attention.

---

### The POWER Framework for Effective Prompts

The difference between average results and excellent results is almost never the model - it's the prompt. The same AI gives average answers to vague questions and excellent answers to structured ones.

**The five elements of a great prompt:**

| Element | Question to Answer |
|---------|--------------------|
| **P - Purpose** | What exactly do you want? Be specific. |
| **O - Operating Context** | What tech stack, architecture, and environment? |
| **W - What Constraints** | What rules, limits, or standards must be followed? |
| **E - Expected Format** | How should the output be structured (list, table, code, explanation)? |
| **R - Role & Tone** | At what expertise level should the AI think (junior, senior, architect)? |

**Example - Bad prompt vs. power prompt:**

> ❌ `Write about micro-frontends`

> ✅ `You are a senior frontend architect. Explain micro-frontends for a React enterprise application with 50+ repos. Compare module federation vs iframe approach. Give pros/cons and a final recommendation.`

The second prompt applies all five elements: the role is defined (senior architect), the context is specific (React enterprise, 50+ repos), the format is clear (comparison + recommendation), and the purpose is precise.

---

### The Chat Debug View

The debug view is one of the most underused tools in the VS Code Copilot toolbox. Open it via the Command Palette → **"Toggle Chat Debug View"**.

It shows the exact prompt that was assembled and sent to the model, broken into layers:

| Layer | What to Check |
|-------|--------------|
| **System prompt** | Which custom instructions and agent instructions were loaded |
| **User prompt** | The prompt you sent, exactly as the model received it |
| **Context** | Which files, symbols, and attachments were included |
| **Response** | The model's full response and any reasoning steps |
| **Tool responses** | Inputs and outputs of every tool called (edit, terminal, search) |

Use the debug view to diagnose unexpected behaviour: if Copilot ignored a file you expected to be in context, or failed to follow an instruction, the debug view will show you exactly what the model saw.

---

## Part 3: From Prompt Engineering to Context Engineering

### The Shift

💡 **Key Insight:** There's a phrase circulating since late 2024: *"prompt engineering is dead; context engineering is what matters now."* It's an overstatement, but it points at something real.

**Prompt engineering** = Writing good messages  
**Context engineering** = Designing *everything the model sees* before it even reads your message  

It's the difference between **choosing the right words** vs. **architecting the right environment**.

### The Definition

Context engineering is the practice of **deliberately designing what goes into the context window**:

✅ What information the model needs at this step  
❌ What information it does *not* need (irrelevant data hurts quality)  
🎯 How information is structured and placed  
⏰ When to refresh the context and start fresh  

**Think of it like designing an information system, not writing an email.** You're deciding where data lives, when it loads, and when it expires.

### Why Models Are Sensitive to Context: The Counterintuitive Core

⚠️ **Critical:** Adding the *wrong* information to the context is not neutral. **It actively hurts results.**

Here's why: Language models read the *entire* context window and produce responses shaped by the overall distribution of content. Every token is like a vote for a certain kind of answer.

**Real examples:**
- ❌ Include a marketing document when asking about backend code → Model suggests marketing-friendly but technically wrong solutions
- ❌ 50-message chat history from 3 hours ago → Old context dilutes focus on today's problem
- ✅ Include only relevant files and recent messages → Model votes unanimously for good code

**Context engineering = Making sure all the votes point in the same direction.**

---

## Part 4: The System Prompt You Never Write

### What Happens When You Send a Message

Before your words reach the language model, Copilot assembles a complete prompt. Every layer of that assembly affects the output.

| Prompt Layer | Contents |
|-------------|----------|
| System Prompt | 1. Core identity & global rules (2-3 lines)<br>2. General instructions (model-specific quirks)<br>3. Tool use instructions (edit, terminal, todos…)<br>4. Output format instructions (file pills, parsing)<br>5. YOUR custom instructions ← you control this<br>6. YOUR custom agent instructions ← you control this |
| User Message #1 | Environment info (OS, VS Code version)<br>Workspace info (project structure, file tree) |
| User Message #2 | Context info (current date/time, open terminals)<br>YOUR prompt file contents (if used) ← you control this<br>Editor context (any files you attached)<br>YOUR actual message |

The model sees all of this as a single continuous document. It has no sense of "the system prompt" or "the user message" - those are protocol-level labels. What the model processes is the full concatenation.

### The System Prompt Layers

**Layers 1–4 - Copilot's built-in content.** Core identity, model-specific quirks, tool call syntax, and output formatting. You don't write these, and you don't see them in normal use. The chat debug view is the only way to inspect them.

**Layers 5 & 6 - Your additions.** Custom instructions and custom agent instructions land at the very end of the system prompt - always. No matter how many instruction files you have, `copilot-instructions.md` is the last one in. No matter which custom agent you're using, its instructions follow yours.

### The User Messages

Two user messages are appended before your actual words appear. The first contains **environment info** (OS, VS Code version) and **workspace info** (your project file tree - this is why Copilot can refer to your file structure without you mentioning it). The second contains **context info** (date, open terminals), any **prompt file contents** if you invoked one, and your **attached files**. Your actual message comes last.

---

## Part 5: Custom Instructions

### What They Are

Custom instructions are persistent context you inject into the system prompt automatically - no slash commands, no manual invocation. Every single request you send includes them.

The canonical use case is project-level knowledge: your architecture patterns, your preferred libraries, your team's naming conventions, your framework version. Anything that should quietly inform every response.

VS Code can **generate** instructions for you. Click the gear icon in Copilot chat and choose "Generate Chat Instructions". It will analyse your project and produce a starting file.

### Where They Live

```
.github/
  instructions/
    copilot-instructions.md   ← global project instructions
    nextjs.instructions.md    ← additional instructions
    typescript.instructions.md
```

You can have as many instruction files as you like. They all land in the system prompt, with `copilot-instructions.md` always last. Instructions can also be placed in the user data folder (outside the project), making them globally available across all workspaces.

### What Goes in Them

Good custom instructions are **informational, not instructional**. They tell the agent what is true about the project, not how to behave.

```markdown
# Project: E-commerce Platform
## Architecture
- Backend: Node.js with Express, TypeScript strict mode
- Frontend: Next.js 14 with App Router
- Database: PostgreSQL via Prisma ORM
- Auth: NextAuth v5

## Patterns
- All API routes return { data, error } shaped responses
- Services live in /src/services/, controllers in /src/controllers/
- Tests use Vitest; run with `npm test`
```

### What Not to Put in Them

- Behavioural overrides ("always write tests") - that's the job of custom agents
- Workflow steps ("first plan, then implement") - that's the job of prompt files
- Large document content - pays token cost on every request, most of which are irrelevant

Write for structure, not prose. The model weights structured content more effectively than dense paragraphs.

```markdown
# DON'T (requires reading to extract structure):
We're a Next.js team working with TypeScript and we prefer to use Prisma for
our database interactions. Our tests are written in Vitest...

# DO (structure is immediately visible):
## Stack
- Next.js 14 (App Router), TypeScript strict
- Prisma ORM (PostgreSQL)
- Vitest for unit tests
```

### The Awesome Copilot Repository

`github.com/github/awesome-copilot` is a curated collection of instruction files, prompt files, and custom agents contributed by developers worldwide. If you work with a popular stack, check here before writing your own - there are likely high-quality instructions you can install directly.

---

## Part 6: Prompt Files

### What They Are

A prompt file is a reusable prompt template stored as a `.prompt.md` file. Where custom instructions are always active and invisible, prompt files are **explicitly invoked** - you call them with a `/` slash command in chat.

The most useful mental model: a prompt file is a **saved workflow step**. Instead of typing the same complex prompt over and over, you define it once, give it a name, and invoke it with a slash.

### Anatomy of a Prompt File

```markdown
---
description: Generate a new React component with tests
mode: agent
model: claude-sonnet-4-5
---

You are creating a new React component. Follow these steps precisely:

1. Analyse the existing components in /src/components/ for style patterns
2. Create the component file at /src/components/{{name}}/{{name}}.tsx
3. Create a test file at /src/components/{{name}}/{{name}}.test.tsx
4. Export from /src/components/index.ts

The component should follow the project's existing patterns exactly.
```

The YAML front matter is where the power lives:
- `description`: shown in the `/` command picker so you remember what each prompt does
- `mode`: `agent` (full tool access), `ask` (conversational), or `edit` (direct file editing)
- `model`: the model to use when this prompt runs - **overrides whatever model is currently selected**

That last point - automatic model switching - is significant. You can write a planning prompt file that forces a switch to Claude Opus 4.5, and an implementation prompt file that switches to a smaller, cheaper model. The user types a slash command and Copilot handles the model routing automatically.

### Where They Live

```
.github/
  prompts/
    generate-component.prompt.md
    plan.prompt.md
    generate-implementation-plan.prompt.md
    remember.prompt.md
```

### Where They Land in the Prompt

Prompt files go into the **user message** - above the context info section, before your actual message. This matters because every message you send with a prompt file re-inserts that file's contents. Over a long conversation, this accumulates. Keep prompt files focused to manage this cost.

### The Best Use Cases

- **Planning steps**: Research the codebase and produce a branch-level implementation plan
- **Code generation**: Generate a component, endpoint, or migration following your project's precise conventions
- **Memory capture**: Takes what you tell it and writes it to a persistent instructions file
- **Review templates**: Code review prompt that checks security, performance, and conventions consistently

---

## Part 7: Custom Agents

### What They Are

Custom agents define a **persona and workflow** for the agent. Where custom instructions add background knowledge and prompt files define reusable tasks, a custom agent changes who the agent *is* - what tools it has, how it approaches problems, what workflow it follows.

Copilot ships with built-in agents: the default Agent mode, Plan mode, and Edit mode. You can create your own to match your specific workflows.

### Anatomy of a Custom Agent

```yaml
---
name: implement
description: Implements code from an implementation plan document step by step
tools:
  - edit
  - terminal
  - read
model: gpt-4.1-mini
---

You are an implementation agent. You receive an implementation plan document
and execute it precisely, step by step.

Rules:
- Never deviate from the plan
- Implement exactly one step, then stop and report completion
- Run tests after each step
- If a step fails, diagnose and fix before moving to the next
- Mark each step complete with [x] in the document
```

Key elements:
- `tools`: the tools this agent can use - you can restrict access intentionally
- `model`: the model this agent uses by default
- The body: the agent's identity, workflow, and constraints

### Where They Live and Land

```
.github/
  agents/
    planner.agent.md
    implement.agent.md
    review.agent.md
```

Custom agent instructions land in the system prompt **after your custom instructions** - always last. This position gives your agent instructions high contextual weight relative to everything that precedes them.

### Handoffs

Custom agents support **handoffs** - a mechanism to pass control from one agent to another with clickable buttons after a response.

```yaml
---
name: planner
handoffs:
  - agent: implement
    label: "Implement this plan"
  - agent: review
    label: "Review this plan"
---
```

### Restricting Tool Access

One of the most valuable things a custom agent can do is **restrict** what tools it has. A planning agent that cannot run terminal commands cannot accidentally execute anything during the planning phase.

```yaml
tools:
  - read
  - search
  # No edit, no terminal - research only
```

This is not just safety - it also improves focus. An agent that knows it can only read files will approach its task differently from one with full tool access.

### The Three Primitives Are Building Blocks

Custom instructions, prompt files, and custom agents are not alternatives to each other - they are **layers of a stack**. The most effective Copilot workflows use all three, each in its appropriate role.

| Primitive | Role | When Active |
|-----------|------|-------------|
| Custom Instructions | Background knowledge | Always - every request |
| Prompt Files | Workflow steps | When explicitly invoked |
| Custom Agents | Identity and tools | When the agent is selected |

### A Real Workflow Example: Plan → Generate → Implement

**Stage 1 - Plan** (new chat session)
- Invoke the `/plan` prompt file - automatically switches to Claude Opus 4.5
- The agent researches the codebase and produces a `plan.md` with commit-level steps
- Result: a structured, commit-by-commit implementation plan

**Stage 2 - Generate** (new chat session - prevents context rot)
- Invoke `/generate`, attach `plan.md`
- The large model writes all implementation code into `implementation-plan.md` - not into the project files
- Code lives in markdown, each step with a checkbox
- Result: a complete implementation document written by the best available model

**Stage 3 - Implement** (new chat session)
- Switch to the `implement` custom agent, attach `implementation-plan.md`
- This agent uses a small, fast, free model
- It implements one step at a time, marks the checkbox, tests, and stops
- Result: production-ready code delivered by a free model executing high-quality instructions

This workflow extracts maximum quality from expensive models while executing with minimum cost.

---

## Part 8: The Context Window Budget

### Thinking in Tokens

A token is roughly three-quarters of a word. The context window is a finite budget shared by everything the model sees.

| Source | Typical Token Cost |
|--------|--------------------|
| Custom instructions (lean) | 200–500 tokens |
| Custom instructions (verbose) | 1,000–5,000 tokens |
| Workspace info (small project) | 500–1,500 tokens |
| Workspace info (large project) | 2,000–10,000 tokens |
| Prompt file | 500–3,000 tokens |
| A medium-sized attached file | 2,000–10,000 tokens |
| A full conversation history (30 turns) | 20,000–80,000 tokens |

Notice what consumes the most budget: **conversation history**. Every exchange accumulates. A long, productive conversation is also a context-hungry one.

### The Budget Allocation Strategy

| Allocation | What It Covers | Target % |
|-----------|----------------|----------|
| Static | Instructions, agent configs, workspace info | ~20% |
| Task context | Files and data relevant to the current task | ~40% |
| Conversation history | Accumulated exchanges | ~40% |

When conversation history starts crowding out task context - when you're attaching files and they're getting lost because the conversation is 50,000 tokens - that's the signal to start a fresh chat.

---

## Part 9: Context Rot

### The Core Phenomenon

Context rot is not a VS Code bug. It is a fundamental property of transformer language models at scale. As the context window grows, **the model's effective attention becomes diluted** - older instructions compete for attention with the latest exchange, and older instructions tend to lose.

The degradation is predictable:

| Context Size | Typical Effect |
|-------------|----------------|
| 2K–8K tokens | Accurate, focused, instruction-following |
| 16K–32K tokens | Drift begins - occasional lapses, less precision |
| 32K–64K tokens | Significant degradation - instructions ignored |
| 64K+ tokens | Severe - model responds to most recent context only |

### What Context Rot Looks Like

You have experienced context rot if:
- Copilot starts writing code in a style you explicitly told it to avoid
- It re-introduces a library you already removed and said not to use
- It ignores a constraint you established at the beginning of the conversation
- Responses become longer and less targeted over time
- It proposes approaches that contradict decisions you've already made

These are not random failures. They are the signature of a diluted context.

### Strategies for Managing Context

**Design for phase boundaries.** Every complex task has natural phases. Each phase boundary is a candidate for a new chat session. The overhead of a few words of context hand-off is almost always worth the quality gain.

```
Phase 1: Research and plan         → New chat after phase completes
Phase 2: Write implementation doc  → New chat after phase completes
Phase 3: Execute implementation    → New chat per step or per commit
Phase 4: Review and test           → New chat
```

**Use subagents for heavy lifting.** When a task requires deep exploration (reading dozens of files, generating large amounts of code), a subagent absorbs that token cost in an isolated context window. Only its final summary returns to your main conversation. (Covered fully in Session 2.)

**Keep custom instructions lean.** Instructions are paid on every request. A 3,000-token instruction file is 3,000 tokens you cannot use for anything else, in every conversation, forever. Ruthlessly edit what's not actively changing responses.

**Attach files selectively.** The most common budget mistake is attaching entire files when only a section is relevant. Be specific about what you attach. Reference files by name when the model knows your project structure already.

**Write for retrieval, not comprehension.** Use headings and bullet lists. The model weights structured content more efficiently than dense prose.

---

## Part 10: Reference

### Context Window Assembly Order

```
SYSTEM PROMPT (assembled once):
  1. Core identity & global rules
  2. General instructions (model-tuned)
  3. Tool use instructions
  4. Output format instructions
  5. Custom instructions (all *.instructions.md files, alphabetical)
  6. copilot-instructions.md (always last among instructions)
  7. Active custom agent instructions (always last of all)

USER MESSAGE #1:
  - Environment info (OS, version)
  - Workspace info (file tree)

USER MESSAGE #2:
  - Context info (date, terminals)
  - Prompt file contents (if invoked)
  - Attached file contents
  - Your actual message

CONVERSATION HISTORY (grows per turn):
  - [Accumulating exchanges, tool call results, responses]
```

### Key File Locations

```
Project-scoped:
  .github/instructions/         ← custom instructions
  .github/prompts/              ← prompt files
  .github/agents/               ← custom agents
  .github/skills/               ← agent skills (Session 2)

User-scoped (global across all projects):
  ~/Library/Application Support/Code/User/prompts/   (macOS)
  %APPDATA%\Code\User\prompts\                       (Windows)
```

### The Four Context Primitives at a Glance

| Primitive | File Pattern | Location in Prompt | Activation | Context Cost |
|-----------|-------------|-------------------|-----------|-------------|
| Custom Instructions | `*.instructions.md` | System prompt (end) | Always | Per-request |
| Prompt Files | `*.prompt.md` | User message (top) | Manual `/slash` | Per-invocation |
| Custom Agents | `*.agent.md` | System prompt (last) | Mode switch | While active |
| Agent Skills | `SKILL.md` folder | Progressive load | Auto-discovered | On-demand |

### Quick Decision Guide

| You want to... | Use this |
|----------------|----------|
| Share project architecture with every request | Custom instruction |
| Enforce a library version or coding pattern globally | Custom instruction |
| Invoke a complex multi-step prompt with one slash command | Prompt file |
| Switch models automatically for a specific task | Prompt file (set `model:` in front matter) |
| Give the agent a specific persona, tools, and workflow | Custom agent |
| Restrict what tools the agent can use in a given mode | Custom agent |
| Teach the agent a domain capability (PDF, Excel, etc.) | Agent skill (Session 2) |

### Signs That Context Needs a Reset

- Copilot ignores constraints you specified earlier
- Responses become generic despite specific instructions
- The agent re-introduces rejected approaches
- Code drifts away from established project patterns
- VS Code prompts you that the context limit is approaching

### Context Reset Approaches

| Approach | Use When |
|----------|----------|
| New chat session | Phase boundary, task complete, context feels contaminated |
| Subagent (Session 2) | Single heavy subtask within a larger workflow |
| Compact summary handoff `/compact` | Continuing work that started in another session |
| Clear + re-attach | Files changed, want model to see current state |

---

## Summary

Every time you send a message to Copilot, you contribute a few words to a document that Copilot is largely assembling itself. The system prompt, workspace structure, environment info, and your persistent instructions are all there before your cursor reaches the end of your sentence.

Understanding this architecture changes how you work. You stop treating Copilot as a chatbot and start treating it as a composable system. You write concise instructions because you understand they persist forever. You start new chats deliberately because you know that context rot is real. You reach for prompt files when you find yourself typing the same thing repeatedly. You build custom agents when you want repeatable, scoped behaviour.

The foundation is not just knowing what these primitives are. It is knowing *where they go* and *when that matters*. Everything in Session 2 - subagents, agent skills, hooks - builds on this mental model. Get the foundation right and everything else clicks into place.

---

## Reference Links

See [All_Links.md](All_Links.md) - **Session 1** section for all documentation, guides, and community resources referenced in this session.

**Key starting points:**
- [GitHub Copilot Customization Cheat Sheet](https://docs.github.com/en/copilot/customizing-copilot/copilot-customization-cheat-sheet)
- [Awesome GitHub Copilot (community hub)](https://github.com/github/awesome-copilot)
- [VS Code Agent Mode docs](https://code.visualstudio.com/docs/copilot/chat/agent-mode)
- [Custom Instructions - GitHub Docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)
- [Prompt Files - VS Code docs](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Custom Agents - GitHub Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)
