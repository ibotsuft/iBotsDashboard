import streamlit as st
import pandas as pd
from src.functions import load_data, load_sample_file


def main():
    st.set_page_config(page_title='iBots Dashboard', page_icon='⚽')
    st.header("Game Resumed Stats")
    dataset = load_sample_file()

    columns_game = {
        'our': ["our_team", "our_final_team_point", "our_possession", "our_yellow", "our_pass_all", "our_through_pass", "our_successed_tackle", "our_failed_tackle", "our_shoot", "our_dribble"],
        'atribbute': ["Team Name", "Goals", "Possession", "Yellow Cards", "Passes", "Through Passes", "Successed Tackles", "Failed Tackles", "Shoots", "Dribles"],
        'opp': ["opp_team", "opp_final_team_point", "opp_possession", "opp_yellow", "opp_pass_all", "opp_through_pass", "opp_successed_tackle", "opp_failed_tackle", "opp_shoot", "opp_dribble"]
    }

    columns = {
        'our': ["our_final_team_point", "our_possession", "our_yellow", "our_pass_all", "our_through_pass", "our_successed_tackle", "our_failed_tackle", "our_shoot", "our_dribble"],
        'atribbute': ["Goals", "Possession", "Yellow Cards", "Passes", "Through Passes", "Successed Tackles", "Failed Tackles", "Shoots", "Dribles"],
        'opp': ["opp_final_team_point", "opp_possession", "opp_yellow", "opp_pass_all", "opp_through_pass", "opp_successed_tackle", "opp_failed_tackle", "opp_shoot", "opp_dribble"]
    }

    our_means = [dataset[col].mean() for col in columns['our']]
    opp_means = [dataset[col].mean() for col in columns['opp']]

    our_medians = [dataset[col].median() for col in columns['our']]
    opp_medians = [dataset[col].median() for col in columns['opp']]

    our_totals = [dataset[col].sum() for col in columns['our']]
    opp_totals = [dataset[col].sum() for col in columns['opp']]

    df_means = pd.DataFrame({
        'our': our_means,
        'atribbute': columns['atribbute'],
        'opp': opp_means
    })

    df_medians = pd.DataFrame({
        'our': our_medians,
        'atribbute': columns['atribbute'],
        'opp': opp_medians
    })

    df_totals = pd.DataFrame({
        'our': our_totals,
        'atribbute': columns['atribbute'],
        'opp': opp_totals
    })

    game_selected = st.slider("Select a game", 0, len(dataset)-1, 0)
    st.write("Selected Game Data:")

    our_game_info = [dataset[col][game_selected]
                     for col in columns_game['our']]
    opp_game_info = [dataset[col][game_selected]
                     for col in columns_game['opp']]

    df_game_info = pd.DataFrame({
        'our': our_game_info,
        'atribbute': columns_game['atribbute'],
        'opp': opp_game_info
    })

    st.table(df_game_info)

    st.header("General Resumed Stats")

    stats_choice = st.selectbox("Pick a stat", ["mean", "median", "total"])
    if stats_choice == 'mean':
        st.table(df_means)
    elif stats_choice == 'median':
        st.table(df_medians)
    else:
        st.table(df_totals)

    st.header("Resumed Info")

    num_rows = dataset.shape[0]
    num_wins = (dataset['our_final_team_point'] >
                dataset['opp_final_team_point']).sum()
    num_losses = (dataset['our_final_team_point'] <
                  dataset['opp_final_team_point']).sum()
    num_draws = (dataset['our_final_team_point'] ==
                 dataset['opp_final_team_point']).sum()

    st.write(f"Games analyzed: {num_rows}")
    st.write(f"Number of our wins: {num_wins}")
    st.write(f"Number of opponnent wins: {num_losses}")
    st.write(f"Number of draws: {num_draws}")
    st.write(f"% of wins: {(num_wins/num_rows)*100}%")


if __name__ == '__main__':
    main()
