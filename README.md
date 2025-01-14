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

   fastapi run src/acme_hello_api

Also see setup in dir `k8` for Kubernetes deployment setup:

    minikube start
    kubectl config use-context minikube
    kubectl apply -k k8 --prune -l app=acme-hello-api
    kubectl config set-context --current --namespace=acme-namespace
    kubectl get services
    # to access LoadBalancer service
    # see: https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fbinary+download#LoadBalancer
    minikube tunnel
    curl http://localhost:80

# GitHub Action `release_k8.yml`

`release_k8.yml` pipeline implements a CD pattern to a K8 cluster running on DigitalOcean.
The full auth procedure is explained here: [Link](https://docs.digitalocean.com/products/kubernetes/how-to/connect-to-cluster/#authenticate).
You need to generate new API token in DigitalOcean by going to "API" section, click "Generate New Token", add "read" and "access_cluster" scope for "kubernetes" resource. Copy the token value, this is the value for `DIGITALOCEAN_ACCESS_TOKEN` secret.
Copy the name of the k8 cluster, this is the value for `DIGITALOCEAN_K8_CLUSTER_NAME` secret.

The pipeline relies on `release-k8` environment to exist in the GitHub repository. To create it, navigate to repository `Settings`, click `Environments` and `New environment`.

After this add secrets `DIGITALOCEAN_ACCESS_TOKEN`, `DIGITALOCEAN_K8_CLUSTER_NAME` under `Environment secrets` of the `release-k8` environment.

# Project template

This project has been setup with `acme-project-create`, a python code template library.

# Required setup post use

* Enable GitHub Pages to be published via [GitHub Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow) by going to `Settings-->Pages-->Source`
* Create `release` environment for [GitHub Actions](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment#creating-an-environment) to enable uploads of the library to PyPi
* Setup auth to PyPI for the GitHub Action implemented in `.github/workflows/release.yml` via [Trusted Publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) `uv publish` [doc](https://docs.astral.sh/uv/guides/publish/#publishing-your-package)
* Once you create the python environment for the first time add the `uv.lock` file that will be created in project directory to the source control and update it each time environment is rebuilt