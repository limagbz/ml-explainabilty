# A Guide to Machine Learning Explainability

[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
[![Cookiecutter Data Science](https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter)](https://cookiecutter-data-science.drivendata.org)
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?logo=kaggle)
![Python](https://img.shields.io/badge/python-3670A0?logo=python)

In the Artificial Intelligence era, there are a lot of Machine Learning models making (or at least, guiding) decisions
for us every day. The products we are going to buy, the next song of our playlists, how much credit the bank should
give to us and even diagnosis when we feel sick. However most of the times there is no transparency on how the models
are making these decisions and what factors they are considering to do so.

We live in a world that is full of biases and injustice, and most of the times these bias are reflected on the data
that we use on our daily lives and jobs. There are multiple ways to fight these problems, and one of them is Knowledge.
Knowledge to understand the tools that we have, the models that we train, the data that we explore.

This repository aims to explain the theory and practice of machine learning explainability (XAI) tools that we have in
Python's ecosystem.

## Motivation

When I started to study some years ago, there wasn't a lot of accessible information about Explainable AI, sure there
were research papers but it was very difficult to understand how to apply these concepts on the real world. Time have
passed, my career went to another path. But now I decided to go back to the field and open-source my study path to
anyone that it can reach, hoping that help someone in the same path as me.

## Documentation

The information contained here is heavily based on the excellent book [**Interpretable Machine Learning:
A Guide for Making Black Box Models Explainable (3ed)**](https://christophm.github.io/interpretable-ml-book/) written by
Christoph Molnar.

## How to use this repository

The easiest way is to read the Jupyter notebooks found in the [notebooks](notebooks/)
directory from Github. But if you still want to install and run this project locally,
refer to [_Installation_](#installation) and [_Run Locally_](#run-locally) sections

## Installation

1. Clone this repository (if you don't know how to do see: [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository));
2. Install the package and project manager: [Astral's uv](https://docs.astral.sh/uv/getting-started/installation/)
3. Run `make setup` to install the dependencies and configure the required tools

## Configuration

Create a .env file with the following variables

```env
KAGGLE_API_TOKEN = "INSERT_TOKEN_HERE"
PYTHONPATH=src
```

## Run Locally

This repository already contains the data and the models used in this project. However
if you want to re-download the data you can use the command `make dataset`.

> [!NOTE]
> Use the command `make help` to all the available commands.

## Running Tests

```bash
  make tests
```

## Contributing

Contributions are always welcome! Feel free to create an issue

## Project Organization

This repository was created using the
[Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) template
made by Driven Data and modified according to the project's needs.

```markdown
├── data
│   ├── external            <- Data from third party sources.
│   ├── interim             <- Intermediate data that has been transformed.
│   ├── processed           <- The final, canonical data sets for modeling.
│   └── raw                 <- The original, immutable data dump.
├── models                  <- Trained and serialized models, model predictions, or model summaries
├── notebooks               <- Jupyter notebooks
├── references              <- Data dictionaries, manuals, and all other explanatory materials.
├── scripts                 <- Standalone scripts to execute some task (e.g. download datasets)
├── src                     <- Source code for the project
├── tests                   <- Unit tests
├── .gitignore              <- The top-level README for developers using this project.
├── .logger.conf            <- Standard library logging configuration
├── .pre-commit-config.yaml <- Pre-commit configurations
├── .python-version         <- Python Version for the project
├── LICENSE                 <- Open-source license
├── Makefile                <- Makefile with convenience commands like `make data` or `make train`
├── uv.lock                 <- Lock file for uv's package manager
├── README.md               <- This file!
└── pyproject.toml          <- Project configuration file
```
