import pytest
from deepsort import deep_sorted
from testcases import parse_testcases

testcases = parse_testcases("testcases.txt")

def run_testcase(input:str):
    return deep_sorted(input)


@pytest.mark.parametrize("testcase", testcases, ids=[testcase["name"] for testcase in testcases])
def test_cases(testcase):
    actual_output = str(run_testcase(testcase["input"])).replace('"',"'")
    expected_output = str(testcase["output"]).replace('"',"'")
    assert actual_output == expected_output, f"Expected {expected_output}, got {actual_output}"


def test_new_cases():
    # single-element tuple must keep trailing comma
    assert deep_sorted((42,)) == "(42,)"

    # empty containers
    assert deep_sorted([]) == "[]"
    assert deep_sorted(()) == "()"

    # all four container types in one list — ordered by opening bracket ASCII:
    # tuple "(" (40) < int digit < list "[" (91) < set "{" (123)
    assert deep_sorted([(1,), 1, [1], {1}]) == "[(1,), 1, [1], {1}]"

    # set elements are sorted ascending
    assert deep_sorted({3, 1, 2}) == "{1, 2, 3}"

    # deeply nested dicts: keys sorted at every level, list values sorted too
    assert deep_sorted({"b": {"d": 4, "c": 3}, "a": [2, 1]}) == '{"a": [1, 2], "b": {"c": 3, "d": 4}}'

    # already-sorted input is returned unchanged
    assert deep_sorted([1, 2, 3]) == "[1, 2, 3]"

    # primitive values pass through as strings
    assert deep_sorted(7) == "7"
