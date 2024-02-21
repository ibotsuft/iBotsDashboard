import streamlit as st
from src.functions import load_data, load_sample_file


def main():
    st.set_page_config(page_title='Graphs', page_icon='⚽')
    st.title('Graphs')
    st.header("Goals per game")
    dataset = load_sample_file()
    st.line_chart(dataset, y=["our_final_team_point", "opp_final_team_point"])


if __name__ == '__main__':
    main()
