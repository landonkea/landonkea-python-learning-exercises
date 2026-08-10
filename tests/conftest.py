# FILE: tests/conftest.py
# PURPOSE: pytest automatically loads this file before running any tests in
#          this directory. It provides shared setup used across test files,
#          here, a helper for importing exercise files whose names start with
#          a digit (e.g. "15_string_methods.py"), which Python's normal
#          `import` statement can't do because module names can't start with
#          a number.

import importlib.util
import pathlib

# Compute the repo root (one directory up from this tests/ folder) so tests
# can find exercise files regardless of what directory pytest is run from.
REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


def import_exercise(filename):
    # WHAT: dynamically loads a numbered exercise file (like "15_string_methods.py")
    # as an importable Python module, even though its filename isn't a legal
    # module name.
    # HOW: importlib.util lets us build a module from an explicit file path
    # instead of Python's usual name-based import search.
    # WHY: this is the standard workaround for importing files with names
    # that don't follow Python identifier rules (leading digits, hyphens).
    file_path = REPO_ROOT / filename

    # "exercise_module" is just an internal label, it doesn't need to match
    # the filename since we're loading by path, not by name.
    spec = importlib.util.spec_from_file_location("exercise_module", file_path)
    module = importlib.util.module_from_spec(spec)

    # Actually run the module's top-level code (imports, class/def statements).
    # Because 15_string_methods.py guards its interactive loop behind
    # `if __name__ == "__main__":`, this executes safely without blocking
    # on input() or starting the menu.
    spec.loader.exec_module(module)

    return module
