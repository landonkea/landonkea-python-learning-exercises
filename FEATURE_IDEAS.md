# FEATURE_IDEAS.md

Ideas for exercises 16 and up. Everything here builds on the same task
manager that's been growing since `07-add-list-tasks.py`, the same way each
existing exercise added exactly one new concept on top of the last. Filenames
follow the underscore convention (`16_fstrings.py`, not `16-fstrings.py`) to
match every numbered file except 01 and 07.

1. **`16_fstrings.py`.** Every `display()` method since exercise 13 builds
   its output with manual concatenation:
   `str(index + 1) + ". [" + status + "] " + self.name`. Rewrite it as
   `f"{index + 1}. [{status}] {self.name}"`. Not a new concept so much as
   fixing a habit that's been there since `07-add-list-tasks.py`, and it
   makes every later exercise easier to read.

2. **`17_sorting.py`.** Add a "sort" menu option that calls `sorted()` with
   a `key=` function, first by name, then by `done` status (incomplete
   tasks first). Low-stakes first exposure to `key=` and `lambda`.

3. **`18_priority.py`.** Give `Task` a `priority` attribute
   (`"low"` / `"medium"` / `"high"`, defaulting to `"medium"`), ask for it
   when adding a task, show it in `display()`, and use it as a second sort
   key alongside exercise 17's sort. Reinforces that adding a field means
   touching the constructor, `to_dict()`, `display()`, and the add-task
   flow, all four, every time.

4. **`19_due_dates.py`.** Add an optional `due_date` field, stored as an
   ISO string (`"2026-09-01"`) in the JSON. First real use of the
   `datetime` module: `date.fromisoformat()` to parse it back and a
   comparison against `date.today()` to flag overdue tasks in `display()`.

5. **`20_search.py`.** Add a "search" option that filters the task list by
   a substring match on the name, case-insensitive
   (`name.lower()` against `query.lower()`). A one-line list comprehension,
   but it's the first time the menu does something other than act on every
   task or one task by index.

6. **`21_tags.py`.** Let a task carry a list of tags
   (`["work", "urgent"]`) instead of a single scalar field. Add a
   filter-by-tag option. First exercise where a `Task` attribute is a list,
   and a natural place to introduce `set()` for deduping the tags seen so
   far across all tasks.

7. **`22_modules.py` + `task.py`.** Pull the `Task` class out into its own
   `task.py` and `import` it from `22_modules.py`. Every exercise so far
   has been one self-contained file; this is the first one that isn't, and
   it's the natural point to introduce `if __name__ == "__main__":`, which
   the earlier files have never needed because they were never imported.

8. **`23_argparse.py`.** Rebuild the interaction model itself: instead of
   the menu loop every exercise since `11_load_and_menu.py` has used, run
   `python 23_argparse.py add "Buy milk"` or
   `python 23_argparse.py list` directly from the shell using `argparse`
   with subparsers. Same `Task` class and JSON file underneath, genuinely
   different front end.

9. **`24_subtasks.py`.** Let a `Task` optionally hold a list of subtask
   `Task` objects. `display()` becomes recursive, indenting by depth. First
   real recursion in the repo, but grounded in an object model the student
   already understands cold by this point.

10. **`25_csv_export.py`.** Add an "export" option that writes the task
    list to `tasks.csv` with the built-in `csv` module. Worth doing because
    it's a format that opens directly in a spreadsheet, unlike
    `tasks.json`, so the payoff is visible outside the terminal.

11. **`26_undo.py`.** Keep a history list of previous task-list snapshots
    (`copy.deepcopy`, since a plain list of references won't work here) and
    add an "undo" option that pops the last snapshot back. Small, but it's
    the first exercise about managing state over time instead of just the
    current state.

12. **`27_sqlite.py`.** Swap `save_tasks()` / `load_tasks()` from JSON file
    I/O to a local SQLite database using the built-in `sqlite3` module.
    Same `Task` class, same menu, different storage layer underneath.
    First exposure to `CREATE TABLE`, `INSERT`, and `SELECT` from Python.

13. **`28_logging.py`.** Replace the bare `print()` error messages in
    `get_valid_index()` (`"That's not a valid number."`, and so on) with
    the `logging` module: warnings go to a `task_manager.log` file while
    the user-facing messages stay on screen. First look at the standard
    library's answer to scattering `print()` calls everywhere for
    debugging.

14. **`29_config.py`.** Add a small `config.json` for preferences, default
    sort order, whether completed tasks show at the top or bottom, loaded
    once at startup. The point isn't the feature, it's realizing that not
    every file a program reads has to be task data.

15. **`30_color_output.py`.** Use raw ANSI escape codes in `print()` (no
    dependency needed) to color overdue tasks red and completed tasks
    green. A small, visible payoff exercise that doesn't require pip
    installing anything, since every prior exercise has run on the
    standard library alone.

16. **`31_dataclass_refactor.py`.** Rewrite `Task` using `@dataclass` from
    the `dataclasses` module instead of a hand-written `__init__`. Works
    best right after a student has written `__init__` by hand a dozen
    times already (exercises 13 through whatever comes before this one),
    so they can actually appreciate what `@dataclass` is doing for them.

17. **`32_context_manager.py`.** Write a small custom context manager (a
    class with `__enter__` / `__exit__`, or `@contextmanager` from
    `contextlib`) that wraps a block of task edits and auto-saves on exit,
    even if an exception happens partway through. Ties error handling
    (exercise 14) and file I/O (exercise 10) together into one new concept.

18. **Catch up the test suite.** `tests/test_15_string_methods.py` is the
    only exercise file with real pytest coverage. Once a few of the ideas
    above exist, write `tests/test_1N_whatever.py` for them the same way,
    same `import_exercise()` helper from `conftest.py`, same
    monkeypatched-`input()` pattern for anything interactive. Not a lesson
    file, but the gap is real and worth closing before it gets bigger.

One thing worth fixing before any of this: `tests/test_15_string_methods.py`
currently can't even be collected. It imports `15_string_methods.py` at
module load time, which runs the file's top-level `while True:` menu loop
immediately and calls `input()` outside of any test, and it also references
`exercise.clean_task_name()`, a function that doesn't exist anywhere in
`15_string_methods.py` (the strip/empty check is inlined in the menu instead).
Running `pytest` right now fails during collection before a single test runs.
That's a pre-existing bug, not something introduced here, and it's outside
the scope of this pass, but idea 18 above depends on the test file actually
working first.
