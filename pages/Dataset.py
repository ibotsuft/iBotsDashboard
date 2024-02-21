import streamlit as st
import pandas as pd
from src.functions import load_data, load_sample_file


def main():
    st.set_page_config(page_title='Dataset', page_icon='⚽')
    st.title('Dataset')

    dataset = load_sample_file()
    st.dataframe(dataset, width=1600, height=600)

    # resumed_df = df[['id', 'Título']]

    # selectbox_options = ['Resumed', 'Complete']

    # dataframe_options = st.selectbox(
    #     'Select the option', selectbox_options)

    # if (dataframe_options == 'Resumed'):
    #     st.dataframe(resumed_df)
    # else:
    #     st.dataframe(df)


if __name__ == '__main__':
    main()
