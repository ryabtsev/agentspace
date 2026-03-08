Project: agentspace.directory
Goal: A single-page discovery and orchestration hub for file-based AI agents.
Architecture: Unified Directory Pattern (Single-Source-of-Truth).

1. Core Concept & Structure
The website facilitates a "Directory-First" approach to AI. All agent logic is declared in a single, LLM-agnostic folder structure.

Key File Declarations:

instructions.md: The "DNA" of the agent—system roles and logic.

memories.md: Shared long-term context and personal facts.

tools.md: Unified API and capability definitions.

tracks/: A subfolder for active state tracking (e.g., debug-xxx.md, feat-xxx.md).

2. Integrated Extensions
Jules should prioritize these two extensions when generating code or planning tasks:

Extension A: apitests (ryabtsev/apitests)
Purpose: TDD for agents.

Implementation: gentests are created within individual project repositories.

Jules Instruction: When working on a task in a tracks/ file, Jules must first check the project repo for gentests and run them to verify any logic changes.

Extension B: apistubs (ryabtsev/apistubs)
Purpose: Environment isolation and safety.

Implementation: Used to mock unstable or expensive third-party APIs.

Jules Instruction: If a task requires an external API that isn't available in the cloud VM, Jules should use apistubs to create a mock endpoint based on the schema in tools.md.

3. Directory Examples (Use cases)
Include these three examples as the primary content sections of the single-page site:

Example 1: Test & Dev Agent
Focus: Automated debugging and feature implementation.

Workflow: Reads a bug report in tracks/, identifies the failing apitest in the repo, and fixes the code until the test passes.

Example 2: Procurement Agent
Focus: Business process automation and governance.

Workflow: Uses instructions.md to vet vendors against budget rules. Uses apistubs to simulate a payment gateway response before finalizing a purchase "track."

Example 3: Second Brain & Personal Planner
Focus: Knowledge synthesis and schedule optimization.

Workflow: Declares personal events (e.g., "Kate's Birthday March 19") in memories.md. The agent proactively creates a tracks/ file to plan the event 14 days in advance.

4. UI/UX Directives (Single Page)
Single Place Declaration: The UI must emphasize that the entire agent behavior is declared in one directory.

Agnostic Display: Show that the same directory can be "run" by different engines (GPT, Claude, or Jules).

Live Tracks: A section of the page should visually render the .md files in the tracks/ folder as a live "Activity Feed."
