# A Guide to Machine Learning Explainability

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?logo=apachespark)
[![Cookiecutter Data Science](https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter)](https://cookiecutter-data-science.drivendata.org)
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?logo=kaggle)
![Python](https://img.shields.io/badge/python-3670A0?logo=python)

In the era of Artificial Intelligence, there are a lot of Machine Learning models making decisions for us. The songs
that we are going to listen, the things that we are going to buy, how much credit we have or even medical diagnosis.
This repository aims to implement and explain some techniques and tools in order to help understand the decisions made
by these models, in a series of notebooks, code and datasets.

The information contained in this repository is heavily based on the excellent book [**Interpretable Machine Learning:
A Guide for Making Black Box Models Explainable**](https://christophm.github.io/interpretable-ml-book/) written by
Christoph Molnar.

## Motivation

Each passing days more and more machine learning models are deployed and are making decisions for us. However most of
the times there is no transparency on what are being decided and how, and I believe that transparency is this context
is very important in order to avoid bias and injustice. This repository aims to be a way for me to learn more about
this and if possible help others in this learning journey.

## Documentation

* [Interpretable Machine Learning: A Guide for Making Black Box Models Explainable (3ed)](https://christophm.github.io/interpretable-ml-book/)

## Installation

1. Clone this repository: [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2. Install the package and project manager: [Astral's uv](https://docs.astral.sh/uv/getting-started/installation/)
3. Run `make setup`

## Run Locally

<!-- TODO: Complete with the command-->
1. Download the data: `make`
2. To explore the notebooks locally: `make notebook` (or use any IDE of your preference)

## Contributing

Contributions are always welcome! Feel free to create an issue

## Running Tests

```bash
  make tests
```

## Project Organization

This repository was created using the
[Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) template
made by Driven Data and modified according to the project's needs.

```markdown
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
├── models             <- Trained and serialized models, model predictions, or model summaries
├── notebooks          <- Jupyter notebooks
├── pyproject.toml     <- Project configuration file
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
├── reports            <- Generated analysis as HTML, PDF, LaTeX, Figures etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
└── ml_explainability  <- Source code for use in this project.
    ├── ...
    ├── config.py      <- Store useful variables and configuration
    ├── dataset.py     <- Scripts to download or generate data
    ├── features.py    <- Code to create features for modeling
    ├── plots.py       <- Code to create visualizations
    ├── predict.py     <- Code to run model inference with trained models
    └── train.py       <- Code to train models
```
