# BBRL - ALGOS

## Description

This library is designed for education purposes, it is mainly used to perform some practical experiences with various RL algorithms. It facilitates using optuna for tuning hyper-parameters and using rliable and statistical tests for analyzing the results.

## Installation

git clone https://github.com/osigaud/bbrl_algos.git

cd bbrl_algos

pip install -e .

We suggest using your favorite python environment (conda, venv, ...) as some further installations might be necessary

## Usage

go to src/bbrl_algos, choose your algorithm and run python3 your_algorithm.py


## quelques remarques
Pour faire le test performance, il faut convertir les ficher .data en .txt en utilisant read_data.py qui est dans src.
Après avoir converti les fichiers, il faut les mettre dans le dossier rliable_stats/data_files puis lancer le script example_test_and_plot.py qui est dans rliable_stats. 

N'oublie pas de changer des chemins absolus dans les scripts.