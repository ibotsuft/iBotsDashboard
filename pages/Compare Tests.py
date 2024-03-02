import streamlit as st
import pandas as pd


def main():
    st.set_page_config(page_title='Compare Tests', page_icon='⚽')
    st.title('Compare')
    st.markdown(
        "Upload your csv file below. Look in the About page for the file specification information")

    first_line = {
        'paramns': [
            "Our Goals", "Opp Goals",
            "Our Possession", "Opp Possession",
            "Our Passes", "Opp Passes",
            "Our Through Passes", "Opp Through Passes",
            "Our Successed Tackles", "Opp Successed Tackles",
            "Our Failed Tackles", "Opp Failed Tackles",
            "Our Shoots", "Opp Shoots",
            "Our Dribles", "Opp Dribles",
            "Our Yellow Cards", "Opp Yellow Cards"],
    }

    first_column_lines_data = [
        "our_final_team_point", "opp_final_team_point",
        "our_possession", "opp_possession",
        "our_pass_all", "opp_pass_all",
        "our_through_pass", "opp_through_pass",
        "our_successed_tackle", "opp_successed_tackle",
        "our_failed_tackle", "opp_failed_tackle",
        "our_shoot", "opp_shoot",
        "our_dribble", "opp_dribble",
        "our_yellow", "opp_yellow",
    ]

    new_csv_files = st.file_uploader(
        "Upload .csv", type=['csv'], accept_multiple_files=True)

    if new_csv_files:
        data_array = ["params"]
        dataframes = []
        mean_dataframes = []
        median_dataframes = []
        total_dataframes = []

        for file in new_csv_files:
            dataframe = pd.read_csv(file)

            if all(col in dataframe.columns for col in first_column_lines_data):
                dataframes.append(dataframe[first_column_lines_data])
                data_array.append(file.name.split(".csv")[0])
            else:
                st.error(
                    f"Columns in (file.name) do not match. Skipping this file.")

        for dataframe in dataframes:
            transposed_df = dataframe.transpose()
            mean_df = transposed_df.mean(axis=1)
            median_df = transposed_df.median(axis=1)
            total_df = transposed_df.sum(axis=1)

            mean_dataframes.append(mean_df)
            median_dataframes.append(median_df)
            total_dataframes.append(total_df)

        df_means = pd.DataFrame({
            'params': first_line['paramns'],
        })

        df_medians = pd.DataFrame({
            'params': first_line['paramns'],
        })

        df_totals = pd.DataFrame({
            'params': first_line['paramns'],
        })

        st.write("Compare the game sets:")

        for i, df in enumerate(mean_dataframes):
            for col_data in df.items():
                new_col_name = f"{data_array[i + 1]}"
                df_means[new_col_name] = df.values

        for i, df in enumerate(median_dataframes):
            for col_data in df.items():
                new_col_name = f"{data_array[i + 1]}"
                df_medians[new_col_name] = df.values

        for i, df in enumerate(total_dataframes):
            for col_data in df.items():
                new_col_name = f"{data_array[i + 1]}"
                df_totals[new_col_name] = df.values

        stats_choice = st.selectbox("Pick a stat", ["mean", "median", "total"])
        if stats_choice == 'mean':
            st.dataframe(df_means)
        elif stats_choice == 'median':
            st.dataframe(df_medians)
        else:
            st.dataframe(df_totals)


if __name__ == '__main__':
    main()
