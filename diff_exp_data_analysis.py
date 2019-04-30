import pandas as pd
from glob import glob

pd.set_option('display.max_columns', None)


all_files = glob('./*.csv')
print(all_files)

all_df = pmt_dit_df, pit_dit_df = [pd.read_csv(file, header=0, usecols=[num for num in range(1,8)], index_col='gene.id') for file in all_files]



print(pmt_dit_df[pmt_dit_df.index.str.contains('^Hpa')].head())
all_hpa_df = hpa_pmt_dit_df, hpa_pit_dit_df = [df[df.index.str.contains('^Hpa')] for df in all_df]
all_at_df = at_pmt_dit_df, at_pit_dit_df = [df[df.index.str.contains('^AT')] for df in all_df]


print(all_hpa_df[0].head())
print(all_at_df[0].head())

for hpa_df, at_df in zip(all_hpa_df, all_at_df):
    hpa_df.sort_values('padj', inplace=True,)
    at_df.sort_values('padj', inplace=True,)


print(all_hpa_df[0]['padj'].head(20))
print(all_at_df[0]['padj'].head(20))


print(all_hpa_df[0].index[:20])
print(all_at_df[0].index[:20])

# print([df.baseMean.sum() for df in all_df])
# print([df.baseMean.sum() for df in all_hpa_df])
# print([df.baseMean.sum() for df in all_at_df])

