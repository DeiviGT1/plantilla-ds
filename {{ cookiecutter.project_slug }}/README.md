# cookiecuter - Data Analysis project 

This is a Cookiecutter template for creating a data analysis project 
## Project Features
- Python 3.8+
- Git integration
- Python preset functions

## Requirements
- git >= 2.x
- Cookiecutter Python package >= 1.4.0: 

You could install cookiecutter depending on how you manage your Python packages (pip or conda), follow the code below:

- pip:  

```
pip install cookiecutter
```

- conda: 

```
conda install -c conda-forge cookiecutter
```

## Directories Distribution
```

├── README.md
├── cookiecutter.json
├── environment.yaml
├── hooks
│   └── post_gen_project.py
└── {{ cookiecutter.project_slug }}
    ├── LICENCE
    ├── README.md
    ├── data
    │   ├── 0_external
    │   ├── 0_raw
    │   ├── 1_intermediate
    │   └── 2_processed
    ├── docs
    ├── environment.yaml
    ├── notebooks
    │   └── 0.0-{{ cookiecutter.project_slug }}-introduction.ipynb
    ├── reports
    ├── requirements.txt
    ├── scripts
    ├── setup.py
    └── {{ cookiecutter.project_slug }}_packages
        ├── __init__.py
        ├── utils
        │   ├── __init__.py
        │   └── get_path.py
        └── visualization
            ├── __init__.py
            └── visualization.py
```

## Usage
In the directory that you create for the project, execute in terminal:
