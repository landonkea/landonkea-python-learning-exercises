# BUILD_LOG.md

This is the story of how this repo got to its current state, and the exact
steps to rebuild that state from nothing. It's written for two audiences at
once: future-me trying to remember why something looks the way it does, and
an automated agent that needs to reconstruct this repo without a human
answering questions.

Everything below is pulled from real `git log` output, not guessed.

## How this repo actually happened

**False start.** The first two commits (`7c52d48`, `e0f522a`) added a
`greetings.py` file and then deleted it about two and a half hours later,
same evening, with the message "removed old file, going to add more later."
That file never really counted; the numbered exercises that followed are the
actual start.

**Fundamentals, one script per PR.** `01-greet.py` through `06_return.py`
were each built on their own branch (`01-greet`, `02-conditional`, and so on)
and merged into `main` through a GitHub PR (#2 through #7). Each script adds
exactly one concept on top of the last: `input()`/`print()`, then `if/else`,
then a `for` loop, then looping over a list, then a function, then a function
that returns a value instead of printing one.

**The task manager begins.** Starting at `07-add-list-tasks.py`, the
exercises stop being throwaway demos and become one continuous project: a
command-line task manager, still one branch and one PR per step (#8 through
#16). It evolves in a specific order that's worth remembering if you're
picking a next exercise:

1. `07-add-list-tasks.py`: a plain list of strings
2. `08_structured_tasks.py`: each task becomes a dict with `name` and `done`
3. `09_mark_complete.py`: search the list by name, flip `done` to `True`
4. `10_save_tasks.py`: persist to `tasks.json` with the `json` module
5. `11_load_and_menu.py`: load on startup, wrap everything in a menu loop
6. `12_edit_and_delete.py`: full CRUD (edit and delete by index)
7. `13_classes.py`: same app, rebuilt around a `Task` class instead of dicts
8. `14_error_handling.py`: `try`/`except` around bad input, `get_valid_index()`
9. `15_string_methods.py`: `.strip()` and empty-name rejection

**Hardening, no more PRs.** After exercise 15, work moved to direct commits
on `main`. `7177b0c` added a line-by-line comment to every single line of
all 15 files, in one pass. `baa4d89` made an implicit `None` return explicit
in `14_error_handling.py` and `15_string_methods.py`, because the comment
next to it claimed a `return` that wasn't actually there. `17b86b1` added
`tasks.json` to `.gitignore` after it turned out an earlier version of that
file had been committed with real personal task data in it; that data was
stripped from history separately with `git filter-repo` before this commit
landed, and the gitignore entry exists so it can't happen again.

**Automation.** `42c5529` added `.github/workflows/ci.yml`: it compiles
every `.py` file with `py_compile` on push and PR. That's it, no test
framework, because a folder of standalone teaching scripts doesn't have one
codebase to run pytest against yet (that came later). `e0c33c7` and
`bd6aaf7` added `.github/workflows/ai-attribution-check.yml`, which scans
commit authors, committers, and messages for AI tool names or
`Co-Authored-By` trailers and fails the build if it finds one. `3d2924e`
fixed that workflow so it stopped flagging its own file and ordinary GitHub
merge commits, which an earlier version of the pattern was catching by
accident.

**Docs and a writing pass.** `778e642` added `docs/DESIGN.md` with Mermaid
diagrams showing the exercise progression and the task manager's menu flow.
`2c3d881` removed em dashes from every markdown file and code comment (the
same rule this file follows) and added the repo's first pytest coverage:
`tests/conftest.py` and `tests/test_15_string_methods.py`.

**Housekeeping.** `8471a7c` is an empty commit, "chore: trigger GitHub
re-index," with no file changes. It exists purely to nudge GitHub's search
indexer after a run of doc changes.

One naming quirk worth flagging so nobody "fixes" it by accident: file
numbers 01 and 07 use a hyphen (`01-greet.py`, `07-add-list-tasks.py`) while
every other numbered file uses an underscore (`02_conditional.py`,
`08_structured_tasks.py`, etc). That's a real inconsistency from the actual
history, not a typo in this doc, and the branch names match it exactly
(`01-greet`, `07-add-list-tasks`).

## Rebuilding this repo from zero, with no human at the keyboard

Two different things are being rebuilt here, and they need different
treatment.

The **scaffolding** (`.gitignore`, README, CI workflows, design docs) is
short and fully specified, so the script below writes it out byte for byte.

The **15 lesson files and their tests** are the actual teaching content of
this repo, roughly 40KB of Python. Regenerating that from a text description
isn't "rebuilding," it's rewriting the lessons from scratch, which risks
losing the exact wording and comment style that makes them useful. So the
script instead copies them from a source location you provide, `main`, a
clone, a zip backup, wherever the files still exist. If they don't exist
anywhere, there's no shortcut: someone has to write 15_string_methods.py's
lesson again, and this document's job is to make sure everything *around*
that lesson comes back automatically once it does.

The same applies to this file, `FEATURE_IDEAS.md`, and `RELEASING.md`: a
document can't contain a byte-identical copy of itself, so those three also
get copied from source rather than written inline.

```bash
#!/usr/bin/env bash
set -euo pipefail

# Point this at any location that still has the 15 exercise files, the
# tests/ directory, and this repo's three top-level docs (BUILD_LOG.md,
# FEATURE_IDEAS.md, RELEASING.md). A git clone of this repo works. So does
# a plain directory copy.
SOURCE_DIR="${1:?Usage: rebuild.sh /path/to/source/checkout}"
TARGET_DIR="landonkea-python-learning-exercises"

mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR"
git init -q

# --- .gitignore ---
cat > .gitignore <<'EOF'
__pycache__/

# Personal task-manager output from the exercise scripts — not code,
# and previously contained real personal notes. Never commit this.
tasks.json
EOF

# --- CI: syntax check ---
mkdir -p .github/workflows
cat > .github/workflows/ci.yml <<'EOF'
name: CI

on:
  push:
  pull_request:

jobs:
  syntax-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Compile all Python files (syntax/import check)
        run: |
          find . -name "*.py" -not -path "*/__pycache__/*" -print0 \
            | xargs -0 -n1 python3 -m py_compile
EOF

# --- fundamentals + task manager source, tests, and top-level docs ---
cp "$SOURCE_DIR"/*.py .
cp -r "$SOURCE_DIR"/tests .
cp -r "$SOURCE_DIR"/docs .
cp "$SOURCE_DIR"/README.md .
cp "$SOURCE_DIR"/BUILD_LOG.md .
cp "$SOURCE_DIR"/FEATURE_IDEAS.md .
cp "$SOURCE_DIR"/RELEASING.md .
cp "$SOURCE_DIR"/.github/workflows/ai-attribution-check.yml .github/workflows/
cp "$SOURCE_DIR"/.github/workflows/release.yml .github/workflows/

# --- commit history, collapsed into logical phases rather than replaying
#     all ~28 original commits and their PR-merge shape, which depended on
#     GitHub itself and isn't worth faithfully reproducing ---
git add 01-greet.py 02_conditional.py 03_loop.py 04_list_loop.py \
        05_function.py 06_return.py .gitignore
git commit -q -m "add fundamentals: input/print, conditionals, loops, functions, return values"

git add 07-add-list-tasks.py 08_structured_tasks.py 09_mark_complete.py \
        10_save_tasks.py 11_load_and_menu.py 12_edit_and_delete.py \
        13_classes.py 14_error_handling.py 15_string_methods.py README.md
git commit -q -m "build task manager project: list -> dict -> JSON -> menu -> classes -> validation"

git add .github/workflows/ci.yml .github/workflows/ai-attribution-check.yml
git commit -q -m "ci: add syntax check and AI-attribution guard"

git add docs tests
git commit -q -m "docs: add design diagrams, add first pytest coverage"

git add BUILD_LOG.md FEATURE_IDEAS.md RELEASING.md .github/workflows/release.yml
git commit -q -m "docs: add build log, feature ideas, and release process"

# --- branch structure for the release process (see RELEASING.md) ---
git branch dev
git branch staging

echo "Done. $(git log --oneline | wc -l | tr -d ' ') commits, branches: $(git branch | tr '\n' ' ')"
```

Run it with `./rebuild.sh /path/to/a/checkout/that/still/has/the/files` and
it produces a working repo with no prompts, no manual edits, and no GitHub
account required. Pushing it to a remote and reopening the per-exercise
branches is a separate, optional step, not something this repo's actual
history depends on for the code to work.
