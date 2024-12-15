# acme-hello-api

Example Hello World API using FastAPI

# Dev environment

The project comes with a python development environment.
To generate it, after checking out the repo run:

    chmod +x create_env.sh

Then to generate the environment (or update it to latest version based on state of `uv.lock`), run:

    ./create_env.sh

This will generate a new python virtual env under `.venv` directory. You can activate it via:

    source .venv/bin/activate

If you are using VSCode, set to use this env via `Python: Select Interpreter` command.

## Example usage

### For development

Using the `.venv` python env you may run:

    fastapi dev src/acme_hello_api

Or to run the code in docker container in a development mode:

    docker compose up --watch

### For production

Using the `.venv` python env you may run:

    fastapi run src/acme_hello_api

Also see setup in dir `k8` for Kubernetes deployment setup:

    minikube start
    kubectl apply -k k8
    kubectl config set-context --current --namespace=acme-namespace
    minikube tunnel
    curl http://localhost:80

# Project template

This project has been setup with `acme-project-create`, a python code template library.

# Required setup post use

* Enable GitHub Pages to be published via [GitHub Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow) by going to `Settings-->Pages-->Source`
* Create `release` environment for [GitHub Actions](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#creating-an-environment) to enable uploads of the library to PyPi
* Setup auth to PyPI for the GitHub Action implemented in `.github/workflows/release.yml`: [Link](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) `uv publish` [doc](https://docs.astral.sh/uv/guides/publish/#publishing-your-package)