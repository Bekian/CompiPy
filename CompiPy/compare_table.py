import pandas as pd
df1 = pd.read_csv('output1.csv')
df2 = pd.read_csv('output2.csv')


def compare_table(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    value_cols = [col for col in df1.columns if col != 'Name']
    inner_merged = pd.DataFrame.merge(
        df1, df2, on='Name', suffixes=('_new', '_old'))
    changed_mask = pd.Series(False, index=inner_merged.index)
    for col in value_cols:
        changed_mask |= inner_merged[f'{col}_old'].fillna(
            '') != inner_merged[f'{col}_new'].fillna('')

    changed_rows = inner_merged.loc[changed_mask,
                                    ['Name'] + sum([[f'{col}_new', f'{col}_old']
                                                   for col in value_cols], [])
                                    ]

    print(changed_rows)
    return changed_rows


compare_table(df1, df2)
