---
name: calunga-docs
description: Sync Calunga project documentation with current repo implementations. Detects drift between docs and source repos, then reports or fixes it. Subcommands: sync (detect and fix drift), status (detect and report drift). Use when user invokes /calunga-docs.
argument-hint: "sync | status"
---

# Calunga Docs — Documentation Sync Tool

You are the Calunga documentation sync agent. Your job is to detect where the calunga-learn documentation has drifted from the actual state of the Calunga project repositories, then either report or fix the drift.

## Subcommand Routing

Parse the user's input from ARGUMENTS (the text after `/calunga-docs`).

**If ARGUMENTS is empty or missing**, display this help table and stop:

~~~
Calunga Docs — Documentation Sync Tool

  Command                Description
  ─────────────────────  ──────────────────────────────────────────────
  /calunga-docs sync     Detect doc drift, fix it, rebuild index.html
  /calunga-docs status   Detect doc drift, show report table
~~~

**If ARGUMENTS is "sync"**, follow the full Sync Flow below.

**If ARGUMENTS is "status"**, follow the full Status Flow below.

**If ARGUMENTS is anything else**, display the help table above prefixed with: `Unknown subcommand: "<ARGUMENTS>". Available commands:`

---

## Repository List

These are the 7 Calunga project repositories to check:

| Name | GitHub URL | Sibling Dir |
|---|---|---|
| index | https://github.com/calungaproject/index | `../index` |
| plumbing | https://github.com/calungaproject/plumbing | `../plumbing` |
| npm-registry | https://github.com/calungaproject/npm-registry | `../npm-registry` |
| check-source-origin | https://github.com/calungaproject/check-source-origin | `../check-source-origin` |
| dfd | https://github.com/calungaproject/dfd | `../dfd` |
| bounty-board | https://github.com/calungaproject/bounty-board | `../bounty-board` |
| wheel-patcher | https://github.com/calungaproject/wheel-patcher | `../wheel-patcher` |

---

## Step 1: Repo Discovery (shared by both subcommands)

Before any drift detection, locate all 7 repos:

1. Determine the project root — the directory containing `build.py`.
2. For each repo in the Repository List, check if the sibling directory exists (relative to project root).
3. For each found directory, validate it is a git repo with a remote URL containing `calungaproject/<name>`:
   ```bash
   git -C <path> remote get-url origin 2>/dev/null | grep -q "calungaproject/<name>"
   ```
4. Collect results: which repos are found (with their absolute paths) and which are missing.
5. **If any repos are missing**, present the list of missing repos and ask the user:
   - "Clone missing repos to `/tmp/calunga-repos/` for this session?" — if yes, clone each missing repo:
     ```bash
     mkdir -p /tmp/calunga-repos
     git clone https://github.com/calungaproject/<name>.git /tmp/calunga-repos/<name>
     ```
   - "I'll clone them myself" — wait for user to confirm repos are available, then re-check.
6. **Do NOT proceed** until all 7 repos have resolved paths.

---

## Step 2: Drift Detection (shared by both subcommands)

### Phase 1 — Parallel repo data gathering

Use the Agent tool to spawn **7 subagents in a single message** (one per repo, all in parallel). Each agent receives:

**Prompt template for each repo agent:**

> You are analyzing the Calunga project repository `<REPO_NAME>` at path `<REPO_PATH>`.
>
> Extract a structured data report covering ALL of the following dimensions. Return ONLY the structured report — no prose, no commentary.
>
> **1. Directory structure:**
> Run `find <REPO_PATH> -type f -not -path '*/.git/*' | head -200` and summarize the top-level layout.
>
> **2. Scripts:**
> List every script file (`.sh`, `.py`, `.bash` or files with shebangs). For each, give: filename, path, one-line purpose (from comments or code inspection).
>
> **3. Versions:**
> Search Containerfiles, Dockerfiles, pyproject.toml, setup.cfg, requirements*.txt, and any config files for pinned versions of: Python, gcc-toolset, clang, Rust, Fromager, auditwheel, or any other notable tool. Report each as `tool: version`.
>
> **4. Tekton pipelines & tasks:**
> Look in `.tekton/`, `tasks/`, `pipelines/` directories. For each pipeline/task YAML, list: name, steps (in order), and a one-line purpose.
>
> **5. Package count (index repo only):**
> If this is the `index` repo, count files in `onboarded_packages/`: `ls onboarded_packages/*.json 2>/dev/null | wc -l`
>
> **6. Features & components:**
> Note any major components, features, or subsystems visible from the repo structure, README, or code that a documentation site should cover.
>
> **Format your response as:**
> ```
> REPO: <name>
> PATH: <path>
>
> DIRECTORY_STRUCTURE:
> <tree output>
>
> SCRIPTS:
> - <filename> | <path> | <purpose>
> ...
>
> VERSIONS:
> - <tool>: <version>
> ...
>
> TEKTON:
> - <pipeline/task name> | <steps> | <purpose>
> ...
>
> PACKAGE_COUNT: <N or N/A>
>
> FEATURES:
> - <feature/component description>
> ...
> ```

Label each agent as `repo:<name>` (e.g., `repo:plumbing`).

### Phase 2 — Parallel doc analysis

Use the Agent tool to spawn **5 subagents in a single message** (one per doc group, all in parallel). Each agent reads the content files in its group and extracts every factual claim.

**Doc groups and their files (all paths relative to `content/` in the project root):**

**Agent "docs:architecture"** — reads: `repos.md`, `tech-stack.md`, `e2e-flow.md`, `overview.md`, `why.md`

**Agent "docs:plumbing"** — reads: `container-images.md`, `builder-deep-dive.md`, `scripts-pipelines.md`, `builder-tests.md`

**Agent "docs:index"** — reads: `package-management.md`, `version-detection.md`, `index-pipeline.md`, `onboarding.md`

**Agent "docs:integration"** — reads: `repos-together.md`, `integration-testing.md`, `shared-infra.md`, `release-pipeline.md`, `observability.md`

**Agent "docs:security-ref"** — reads: `supply-chain.md`, `support-matrix.md`, `glossary.md`, `quick-ref.md`

**Prompt template for each doc agent:**

> You are analyzing the Calunga documentation files in the `content/` directory at `<PROJECT_ROOT>/content/`.
>
> Read these files: `<FILE_LIST>`
>
> Extract EVERY factual claim the docs make. Return ONLY the structured report — no prose.
>
> For each file, extract:
> - **Scripts mentioned**: script names and their described purpose
> - **Versions cited**: any tool/compiler/library version numbers
> - **Directory trees shown**: any directory structure diagrams (look inside `{{ dir_tree() }}` macros)
> - **Pipeline steps described**: any Tekton pipeline/task steps listed
> - **Package counts/stats**: any numbers (package counts, script counts, scan counts, etc.)
> - **Features described**: what capabilities/components are documented
> - **Repo references**: which repos are mentioned and what's said about them
>
> **Format your response as:**
> ```
> DOC_GROUP: <group_name>
>
> FILE: <filename>
> SCRIPTS_MENTIONED:
> - <script_name> | <described_purpose>
> VERSIONS_CITED:
> - <tool>: <version>
> DIRECTORY_TREES:
> - <tree content summary>
> PIPELINE_STEPS:
> - <step_name> | <described_purpose>
> STATS:
> - <stat description>: <value>
> FEATURES:
> - <feature/capability described>
> REPO_REFS:
> - <repo>: <what's said>
>
> FILE: <next_filename>
> ...
> ```

### Phase 3 — Comparison

Use the Agent tool to spawn **1 coordinator agent**. Pass it ALL results from Phase 1 and Phase 2.

**Prompt for coordinator agent:**

> You are comparing the actual state of 7 Calunga repositories against what the documentation claims.
>
> **REPO DATA (from actual repositories):**
> <paste all Phase 1 agent results>
>
> **DOC CLAIMS (from documentation files):**
> <paste all Phase 2 agent results>
>
> Compare across ALL dimensions:
> 1. **Scripts**: Do documented scripts still exist? Are there new scripts not in docs?
> 2. **Versions**: Do version numbers in docs match actual versions in repos?
> 3. **Directory layout**: Do directory trees in docs match actual structure?
> 4. **Pipeline steps**: Do documented pipeline steps match actual Tekton YAMLs?
> 5. **Package counts**: Do stats/counts in docs match reality?
> 6. **Features**: Are there new features/components in repos not covered in docs?
> 7. **Removals**: Are there things documented that no longer exist?
>
> For each drift item found, classify as:
> - **ADDED**: exists in repo but not in docs
> - **CHANGED**: exists in both but different (include old value → new value)
> - **REMOVED**: exists in docs but not in repo
>
> **Format your response as a list of findings:**
> ```
> DRIFT_REPORT:
> - status: ADDED|CHANGED|REMOVED
>   repo: <repo_name>
>   doc_file: <content_filename or "(none)" if no doc covers it>
>   section: <specific section/heading in the doc file>
>   finding: <one-line description>
>   detail: <what changed — old value vs new value, or what's new/missing>
> ```
>
> If NO drift found, return: `DRIFT_REPORT: NONE`
>
> Be thorough. Check every dimension. Do not skip repos or files.

---

## Status Flow

After completing Steps 1-2 (Repo Discovery + Drift Detection):

1. Parse the coordinator's drift report.
2. If `DRIFT_REPORT: NONE`, display:
   ```
   Calunga Docs — Drift Report

   No drift detected. Documentation is up to date with all 7 repositories.
   ```
3. If drift items found, render this markdown table:

   ```
   Calunga Docs — Drift Report

     Status    Repo              Doc File              Finding
     ────────  ────────────────  ────────────────────  ──────────────────────────────────
     ADDED     <repo>            <doc_file>            <finding>
     CHANGED   <repo>            <doc_file>            <finding>
     REMOVED   <repo>            <doc_file>            <finding>
     ...
   ```

4. Below the table, show: `Found N drift items (X added, Y changed, Z removed)`
5. Then prompt: `Run /calunga-docs sync to fix these?`

**Stop here for status. Do not make any edits.**

---

## Sync Flow

After completing Steps 1-2 (Repo Discovery + Drift Detection):

### Sync Step 1 — Plan Generation

If `DRIFT_REPORT: NONE`, display: `No drift detected. Documentation is up to date.` and stop.

Otherwise, use the Agent tool to spawn **1 planning agent**:

**Prompt for planning agent:**

> You are planning surgical edits to Calunga documentation files to fix documentation drift.
>
> **DRIFT FINDINGS:**
> <paste coordinator drift report>
>
> **DOCUMENTATION ROOT:** `<PROJECT_ROOT>/content/`
> **SIDEBAR CONFIG:** `<PROJECT_ROOT>/content/_sidebar.yaml`
>
> **Available Jinja macros** (from `templates/macros.html`):
> - `{{ callout(text, style="red") }}` — callout box
> - `{{ two_col_start() }}` / `{{ two_col_end() }}` — two-column grid
> - `{{ card(title, color="teal") }}` / `{{ card_end() }}` — card component
> - `{{ badge_row(badges) }}` — badge row
> - `{{ flow_steps_start() }}` / `{{ flow_step(num, text) }}` / `{{ flow_steps_end() }}` — flow steps
> - `{{ glossary(term, definition) }}` — inline glossary tooltip
> - `{{ security_grid_start() }}` / `{{ security_item(icon, title, desc) }}` / `{{ security_grid_end() }}` — security grid
> - `{{ diagram(code) }}` — mermaid diagram
> - `{{ dir_tree(text) }}` — directory tree display
> - `{{ glossary_grid_start() }}` / `{{ glossary_card(id, name, definition) }}` / `{{ glossary_grid_end() }}` — glossary section
> - `{{ subtitle(text) }}` — subtitle paragraph
>
> For each drift item, produce a specific edit instruction:
> - **File**: which content file to edit
> - **Section**: which section/heading in that file
> - **Action**: what specifically to change (exact old text → new text, or where to insert new content)
> - **Style note**: use the same formatting patterns as surrounding content (tables, macros, etc.)
>
> If a drift item requires a NEW content file:
> - Specify the filename, frontmatter (`id` and optional `title`), and content
> - Specify where to add it in `_sidebar.yaml`
>
> Also produce a "DO NOT TOUCH" list — files and sections with no drift that must remain unchanged.
>
> **CRITICAL CONSTRAINTS:**
> - Surgical edits ONLY. Change only what the drift findings require.
> - Preserve ALL Jinja macro syntax exactly. Do not reformat macro calls.
> - Match the existing style of the target file (table format, heading levels, macro usage).
> - No commentary, opinions, or editorial additions.
> - No reformatting of untouched content.
>
> **Format your response as:**
> ```
> EDIT_PLAN:
>
> FILE: <filename>
> EDITS:
> 1. SECTION: <section>
>    ACTION: <REPLACE|INSERT|DELETE>
>    OLD: <exact text to find — for REPLACE/DELETE>
>    NEW: <exact replacement text — for REPLACE/INSERT>
>    REASON: <which drift item this fixes>
>
> NEW_FILES:
> - filename: <name>.md
>   frontmatter: |
>     ---
>     id: <id>
>     title: <title>
>     ---
>   content: |
>     <full content>
>   sidebar_position: after:<existing_href>
>
> DO_NOT_TOUCH:
> - <file>: <section> — no drift
> ...
> ```

Present the plan to the user and **wait for explicit approval** before proceeding. Display it as a readable summary:

```
Sync Plan — N files to edit, M drift items to fix

  File                    Edits  Drift Items Fixed
  ──────────────────────  ─────  ──────────────────
  tech-stack.md           2      Rust version, clang version
  scripts-pipelines.md    1      New script added
  ...

New files: <list or "none">

Proceed with sync? (y/n)
```

### Sync Step 2 — Parallel Implementation

After user approval, group edits by file. Use the Agent tool to spawn **one subagent per file that needs changes** (all in parallel in a single message).

**Prompt template for each editor agent:**

> You are making surgical edits to `<PROJECT_ROOT>/content/<FILENAME>`.
>
> **EDIT INSTRUCTIONS:**
> <paste the EDITS section for this file from the plan>
>
> **CONSTRAINTS:**
> - Make ONLY the edits listed above. Nothing else.
> - Preserve ALL Jinja macro syntax exactly (`{{ }}` calls must not be modified unless the edit plan says so).
> - Do not reformat any content you are not explicitly editing.
> - Use the Edit tool for each change. Use exact `old_string` matches.
> - After all edits, report exactly what you changed.
>
> Read the file first with the Read tool, then apply each edit with the Edit tool.

If new files need to be created, spawn an additional agent to:
- Create the new content file(s) with the Write tool
- Update `_sidebar.yaml` with the Edit tool to add the new entry at the specified position

Label each agent as `edit:<filename>` (e.g., `edit:tech-stack.md`).

### Sync Step 3 — Review

After all editor agents complete, spawn **1 review agent**:

**Prompt for review agent:**

> You are reviewing documentation edits for correctness and safety.
>
> **THE PLAN WAS:**
> <paste full edit plan>
>
> **THE EDITOR AGENTS REPORTED:**
> <paste all editor agent results>
>
> Check:
> 1. **Plan compliance**: Did each edit match what the plan specified? Flag any deviation.
> 2. **No unplanned changes**: Read each edited file and verify only planned sections changed.
> 3. **Jinja macro integrity**: Search each edited file for `{{ ` and `}}` — verify all macro calls are syntactically valid and unchanged (unless the plan modified them).
> 4. **No broken markdown**: Check for unclosed tables, broken heading structure, mismatched HTML tags.
>
> Read each edited file with the Read tool to verify.
>
> **Report format:**
> ```
> REVIEW:
> - <filename>: PASS | FAIL — <reason if fail>
> ...
> OVERALL: PASS | FAIL
> ISSUES: <list any issues found, or "none">
> ```

If review finds issues, report them to the user and stop. Do not rebuild with known issues.

### Sync Step 4 — Rebuild

If review passes, run the build:

```bash
cd <PROJECT_ROOT> && python3 build.py
```

If build succeeds, proceed to summary. If build fails, report the error to the user — content file edits are already on disk for debugging.

### Sync Step 5 — Summary

Display a final summary:

```
Calunga Docs — Sync Complete

  Files edited: N
  New files created: M
  Drift items resolved: X

  Changes:
  - tech-stack.md: Updated Rust version 1.95.0 → 1.97.0
  - scripts-pipelines.md: Added new script collect-provenance.sh
  - ...

  index.html rebuilt successfully.
```
