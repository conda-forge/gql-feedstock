import sys
from subprocess import call

FAIL_UNDER = "95"
COV = ["coverage"]
RUN = ["run", "--source=gql", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = [
    # https://github.com/conda-forge/gql-feedstock/pull/24
    "test_hero_name_query",
    "test_query_with_variable",
    "test_named_query",
    "test_header_query",
    "test_get_introspection_query_ast",
]


SKIP_OR = " or ".join(SKIPS)
K = ["-k", f"not ({SKIP_OR})"]


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST, *K])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
