# Contributing to TypoFlip

Thanks for your interest in contributing! Please follow these guidelines to make collaboration smooth.

Getting started
- Fork the repository and create a feature branch: `git checkout -b my-feature`
- Keep changes small and focused; open separate PRs for unrelated work.
- Write tests for new behavior and run the test suite locally.

Development
- Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

- Run tests:

```bash
pytest -q
```

Code style
- Follow consistent formatting; `black` is the recommended formatter (included in requirements-dev.txt).

Pull requests
- Ensure all tests pass and add changelog entries if applicable.
- Describe the why and what in the PR description, and include screenshots for UI changes.
- Assign reviewers and link any relevant issues.

License
- By contributing you agree that your contributions will be licensed under the project's GPLv3 license.
