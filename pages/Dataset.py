import streamlit as st
import pandas as pd
from src.functions import load_data, load_sample_file


def load_data(file):
    if file is not None:
        data = pd.read_csv(file)
        return data
    else:
        return None


def main():
    st.set_page_config(page_title='Dataset', page_icon='⚽')
    st.title('Dataset')

    new_csv_file = st.file_uploader(
        "Upload .csv", type=['csv'], accept_multiple_files=False)

    if new_csv_file is not None:
        dataset = load_data(new_csv_file)
    else:
        dataset = load_sample_file()

    if dataset is not None:
        st.dataframe(dataset, width=1600, height=600)


if __name__ == '__main__':
    main()
