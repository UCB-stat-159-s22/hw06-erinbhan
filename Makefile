env:
    mamba env create -f environment.yml -p ~/envs/ligo
    conda activate ligo
    python -m ipykernel install --user --name ligokernel --display-name "IPython - ligokernel"
    
html:
    jupyterbook build .

html-hub:
    jupyter-book config sphinx .
    sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
    cd _build
    cd html; python -m http.server

clean:
    rm -r _build/*
    rm -r audio/*
    rm -r figurs/*