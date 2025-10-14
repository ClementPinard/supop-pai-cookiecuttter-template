# supop-pai-cookiecuttter-template

A cookiecutter template that you can use to start your project.

This template is part of a lecture given at [Institut d'Optique](https://www.institutoptique.fr/).
Students are expected to use last good practice coding tools, including cookiecutter. This template will help them get started with everything installed.

See official website (in French) : https://sites.google.com/view/supop-pai

## Features

- NiceGUI basic app
- QT basic app
- Docs website with sphinx
- pre-commit linting
- pyright type checking
- Unit tests with pytest
- Github CI that will run pre-commit, pytest and pyright for each pushed commit
- Issue and Pull Request templates

## How to use

The following indications assume you have `uv` and `git` installed and usable within your terminal.
See [Install instructions](https://docs.astral.sh/uv/getting-started/installation/).

1. Create your own repo on github, keep it empty. Optionally, add a License (this template does not have any).
2. Clone it, and note the github http address.
3. Call the following command

    ```bash
    uvx cookiecutter https://github.com/ClementPinard/supop-pai-cookiecuttter-template
    ```

    It will ask for:

    - The project name
    - the repo name: make it so it matches the repo name on github
    - the github http adress of your project

4. copy paste everything in the newly created "cookiecutter_output" folder created in your
previously cloned repo

    ```bash
    cp -r cookiecutter_output/* <my cloned repo>
    ```

5. You can now commit and push to have a first version of your project

```bash
git add .
git commit -m "First commit applying template"
git push
```
