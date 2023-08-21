# ai-for-beginner
This interface is perfect for beginners looking to explore ML basics in a fun, interactive manner.

## Getting Started
Python version `python3.10.1` with `gradio, scikit-learn, seaborn, pandas, numpy, matplotlib, joblib`

### Build `venv` for **MacOS**
```shell
$ pip3 install virtualenv
$ virtualenv venv --python=python3.10.1
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
$ rm -rf venv     # remove the venv
```

### Build `venv` for Windows
```shell
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ deactivate
$ rmdir /s venv     # remove the venv
```
### Build Docs
```shell
$ pip install mkdocs
$ pip install mkdocs-material
$ pip install pymdown-extensions
$ pip install mkdocstrings
$ pip install mkdocs-git-revision-date-plugin
$ pip install mkdocs-jupyter
```