import streamlit as st
import pandas as pd
import json


def main():
    st.set_page_config(page_title='iBots JSON Analyzer', page_icon='⚽')
    st.title('iBots JSON Analyzer')

    keys_to_use = [
        'ourTeamName', 'opponentTeamName',
        'ourBallPossession', 'opponentBallPossession',
        'ourBallPossessionPercentual', 'opponentBallPossessionPercentual',
        'ourPasses', 'opponentPasses',
        'ourCorrectPasses', 'opponentCorrectPasses',
        'ourPercentualCorrectedPasses', 'opponentPercentualCorrectedPasses',
        'ourMissedPasses', 'opponentMissedPasses',
        'ourShots', 'opponentShots',
        'ourShotsOnTarget', 'opponentShotsOnTarget',
        'ourCorners', 'opponentCorners',
        'ourFouls', 'opponentFouls']

    uploaded_files = st.file_uploader(
        "Upload JSON files", type="json", accept_multiple_files=True)

    if uploaded_files:
        data = {}

        for uploaded_file in uploaded_files:
            file_content = uploaded_file.getvalue().decode("utf-8")
            json_data = json.loads(file_content)

            row_values = []
            for key in keys_to_use:
                if key in json_data:
                    row_values.append(json_data[key])
                else:
                    row_values.append(None)

            data[uploaded_file.name] = row_values

        df = pd.DataFrame.from_dict(data, orient='index', columns=keys_to_use)
        columns_to_average = [col for col in df.columns if col not in [
            'ourTeamName', 'opponentTeamName']]
        df_mean = df[columns_to_average].mean()
        df_median = df[columns_to_average].median()
        df_total = df[columns_to_average].sum()
        summary_df = pd.DataFrame(
            {'mean': df_mean, 'median': df_median, 'total': df_total})
        st.header("Game set dataframe")
        st.write(df)

        st.header("Game set dataframe mean summary")
        st.write(summary_df)

        st.header("Compare with others game sets")
        new_uploaded_files = st.file_uploader(
            "Upload New JSON files", type="json", accept_multiple_files=True)

        stats_choice = st.selectbox("Pick a stat", ["mean", "median", "total"])
        if new_uploaded_files:
            data_new = {}

            for uploaded_file in new_uploaded_files:
                file_content = uploaded_file.getvalue().decode("utf-8")
                json_data = json.loads(file_content)

                row_values = []
                for key in keys_to_use:
                    if key in json_data:
                        row_values.append(json_data[key])
                    else:
                        row_values.append(None)

                data_new[uploaded_file.name] = row_values

            df_new = pd.DataFrame.from_dict(
                data_new, orient='index', columns=keys_to_use)

            # Escolha da estatística
            stats_choice = st.selectbox(
                "Pick a stat to compare", ["mean", "median", "total"])

            if stats_choice == 'mean':
                df_means = pd.concat(
                    [df_mean, df_new[columns_to_average].mean()], axis=1)
                df_means.columns = ['Game set 1', 'Game set 2']
                st.header("Mean comparison")
                st.write(df_means)

            elif stats_choice == 'median':
                df_medians = pd.concat(
                    [df_median, df_new[columns_to_average].median()], axis=1)
                df_medians.columns = ['Game set 1', 'Game set 2']
                st.header("Median comparison")
                st.write(df_medians)

            else:
                df_totals = pd.concat(
                    [df_total, df_new[columns_to_average].sum()], axis=1)
                df_totals.columns = ['Game set 1', 'Game set 2']
                st.header("Total comparison")
                st.write(df_totals)


if __name__ == '__main__':
    main()
