[run-pycode]: https://github.com/elmokulc/run-pycode.git

run-pycode
=============

run-pycode package for pre-commit.

For pre-commit: see https://github.com/pre-commit/pre-commit

# Description
 run-code allow you to run some python scripts before commit.

### Using run-pycode with pre-commit

Add this to your `.pre-commit-config.yaml`:

    -   repo: https://github.com/elmokulc/run-pycode.git
        rev: ''  # Use the sha / tag you want to point at
        hooks:
        -   id: run-pycode
            args: ["--files-to-run=[path0/to/script0.py,
                                    path1/to/script1.py]"]


