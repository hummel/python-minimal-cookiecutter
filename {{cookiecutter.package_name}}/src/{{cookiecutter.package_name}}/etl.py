"""
{{cookiecutter.project_name}} data preparation
"""
import pandas as pd

def load_data(path):
    return pd.read_csv(path)