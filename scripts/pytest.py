from os import system


def run_tests_with_coverage():
    system("pytest --cov=./app")
