# Pull Request

## Describe your changes

## Issue number if applicable

## Checklist before requesting a review

Github actions will check that these tasks were performed but it will reduce friction if you deal with them beforhand

- [ ] Code style follows black conventions (Checked by [pre-commit]({{ cookiecutter.github_url }}/blob/main/.github/workflows/CI.yaml#L82) job)
- [ ] Type hints are consistent (Checked by [pyright]({{ cookiecutter.github_url }}/blob/main/.github/workflows/CI.yaml#L67) job)
- [ ] New lines are covered by tests (Checked by [pytest coverage]({{ cookiecutter.github_url }}/blob/main/.github/workflows/CI.yaml#L26) job).
- [ ] If documentation is added, it does not raise a warning in sphinx (checked by [sphinx-build]({{ cookiecutter.github_url }}/blob/main/.github/workflows/CI.yaml#L65) job)
