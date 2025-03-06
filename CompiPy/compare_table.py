import pandas as pd
df1 = pd.read_csv('output1.csv')
df2 = pd.read_csv('output2.csv')


def compare_table(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    primary_key = df1.columns[0]
    value_cols = [col for col in df1.columns if col != primary_key]

    inner_merged = pd.DataFrame.merge(
        df1, df2, on=primary_key, suffixes=('_new', '_old'))

    changed_mask = pd.Series(False, index=inner_merged.index)
    for col in value_cols:
        old_col = f'{col}_old'
        new_col = f'{col}_new'
        if old_col in inner_merged and new_col in inner_merged:
            changed_mask |= inner_merged[old_col] != inner_merged[new_col]

    changed_rows = inner_merged[changed_mask]
    print(changed_rows)
    return changed_rows


compare_table(df1, df2)
