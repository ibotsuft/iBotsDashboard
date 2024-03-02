import streamlit as st
from src.functions import load_data, load_sample_file


def load_data(file):
    if file is not None:
        data = pd.read_csv(file)
        return data
    else:
        return None


def main():
    st.set_page_config(page_title='Graphs', page_icon='⚽')
    st.title('Graphs')
    st.header("Goals per game")

    new_csv_file = st.file_uploader(
        "Upload .csv", type=['csv'], accept_multiple_files=False)

    if new_csv_file is not None:
        dataset = load_data(new_csv_file)
    else:
        dataset = load_sample_file()

    if dataset is not None:
        st.line_chart(
            dataset, y=["our_final_team_point", "opp_final_team_point"])


if __name__ == '__main__':
    main()
