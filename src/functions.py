import pandas as pd
import streamlit as st


def load_data(file_path):
    return pd.read_csv(file_path)


def load_sample_file():
    df = load_data('IBots_x_HeliosBase_original.csv')
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d%H%M')
    df_sorted = df.sort_values(by='date')

    return df_sorted
