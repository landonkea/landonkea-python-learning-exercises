# FILE: tests/test_15_string_methods.py
# PURPOSE: Real automated test coverage for 15_string_methods.py, the most
#          polished version of the task manager (classes + error handling +
#          input validation all combined). Before this file, the repo had NO
#          automated tests at all, only a CI syntax check. These tests catch
#          real regressions (e.g. the earlier missing `return None` bug in
#          get_valid_index would have been caught immediately by a test like
#          test_get_valid_index_rejects_non_numeric_input below).

import builtins

import pytest

from conftest import import_exercise

# Load the exercise file once for all tests in this module.
exercise = import_exercise("15_string_methods.py")


# ---------------------------------------------------------------------------
# Task class
# ---------------------------------------------------------------------------


def test_task_defaults_to_not_done():
    # WHAT/WHY: a freshly created Task should start incomplete unless told
    # otherwise, this is the documented default in Task.__init__.
    task = exercise.Task("Buy groceries")

    assert task.name == "Buy groceries"
    assert task.done is False


def test_task_complete_and_uncomplete_toggle_done():
    task = exercise.Task("Call the bank")

    task.complete()
    assert task.done is True

    task.uncomplete()
    assert task.done is False


def test_task_to_dict_round_trips_name_and_done():
    task = exercise.Task("Finish project", done=True)

    assert task.to_dict() == {"name": "Finish project", "done": True}


# ---------------------------------------------------------------------------
# clean_task_name, the extracted validation helper
# ---------------------------------------------------------------------------


def test_clean_task_name_strips_whitespace():
    assert exercise.clean_task_name("  Buy milk  ") == "Buy milk"


def test_clean_task_name_rejects_blank_input():
    # A name that's empty, or only whitespace, must be rejected (returns None)
    # so the menu loop knows not to create a Task from it.
    assert exercise.clean_task_name("") is None
    assert exercise.clean_task_name("    ") is None


# ---------------------------------------------------------------------------
# save_tasks / load_tasks, file I/O round trip
# ---------------------------------------------------------------------------


def test_save_and_load_round_trip(tmp_path, monkeypatch):
    # WHY monkeypatch.chdir: save_tasks/load_tasks hardcode the filename
    # "tasks.json" relative to the current directory. Running the test from
    # a temp directory keeps it from touching the real repo's tasks.json.
    monkeypatch.chdir(tmp_path)

    original = [exercise.Task("Buy groceries"), exercise.Task("Call the bank", done=True)]
    exercise.save_tasks(original)

    loaded = exercise.load_tasks()

    assert [t.to_dict() for t in loaded] == [t.to_dict() for t in original]


def test_load_tasks_returns_empty_list_when_no_file_exists(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    # No tasks.json has been written in this fresh temp directory.
    assert exercise.load_tasks() == []


# ---------------------------------------------------------------------------
# get_valid_index, safe user-input handling
# ---------------------------------------------------------------------------


def _fake_input(return_value):
    # Small helper that returns a function usable with monkeypatch.setattr
    # to stand in for the built-in input(), always returning `return_value`
    # regardless of the prompt text passed to it.
    return lambda prompt="": return_value


def test_get_valid_index_accepts_valid_1_based_number(monkeypatch):
    monkeypatch.setattr(builtins, "input", _fake_input("2"))
    tasks = [exercise.Task("a"), exercise.Task("b"), exercise.Task("c")]

    # User typed "2" (1-based) -> should resolve to index 1 (0-based).
    assert exercise.get_valid_index(tasks, "prompt") == 1


def test_get_valid_index_rejects_out_of_range_number(monkeypatch, capsys):
    monkeypatch.setattr(builtins, "input", _fake_input("99"))
    tasks = [exercise.Task("a")]

    assert exercise.get_valid_index(tasks, "prompt") is None
    assert "doesn't exist" in capsys.readouterr().out


def test_get_valid_index_rejects_non_numeric_input(monkeypatch, capsys):
    # This is the exact scenario the earlier "missing return None" bug broke:
    # typing letters instead of a number used to fall through the except
    # block without an explicit return, relying on Python's implicit None,
    # this test locks in the correct, explicit behavior.
    monkeypatch.setattr(builtins, "input", _fake_input("abc"))
    tasks = [exercise.Task("a")]

    assert exercise.get_valid_index(tasks, "prompt") is None
    assert "not a valid number" in capsys.readouterr().out


def test_get_valid_index_rejects_negative_number(monkeypatch):
    monkeypatch.setattr(builtins, "input", _fake_input("0"))
    tasks = [exercise.Task("a")]

    # User typed "0" -> 0 - 1 = -1, which is out of range (negative).
    assert exercise.get_valid_index(tasks, "prompt") is None
