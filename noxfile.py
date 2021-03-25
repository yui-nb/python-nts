import nox


locations = "src", "tests", "noxfile.py"
nox.options.sessions = "lint", "tests"


@nox.session(python=["3.9", "3.8", "3.7"])
def test(session):
    """Run test suite with pytest."""
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")


@nox.session(python=["3.9", "3.8"])
def lint(session):
    """Lint using flake8 and darglint."""
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
        "flake8-docstrings",
        "darglint",
    )
    session.run("flake8", *args)


@nox.session(python="3.9")
def black(session):
    """Run black code formatter."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
