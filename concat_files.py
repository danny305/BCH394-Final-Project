import pandas as pd
from glob import glob
from matplotlib import pyplot as plt




pd.set_option('display.max_columns', None)


all_files = glob('./RNAseq-data/*.txt')
#print(all_files)

print([file[15:19] for file in all_files])

all_df = [pd.read_csv(file, sep='\t', header=None,names=['Org-Gene',file[14:18]]) for file in all_files]

all_df_iter = iter(all_df)

merge_df = next(all_df_iter)
for df in all_df_iter:
    merge_df = pd.merge(merge_df, df, on='Org-Gene')

merge_df.set_index('Org-Gene', inplace=True)

print(merge_df.columns)
#Setting the column order
merge_df = merge_df[['DIC1','DIC2','DIC3','DIC4',
                'DIT1','DIT2','DIT3','DIT4','DIT5',
                'DMC1','DMC2','DMC3',
                'PIC1','PIC2','PIC3','PIC4',
                'PIT2','PIT3','PIT4','PIT5',
                'PMC1','PMC2','PMC3','PMC4']]



## Created PIE Chart

labels = ['HPA', 'AT']

experiments = ['PMC','PIC','PIT', 'DIC','DIT']

for re in experiments:
    df = merge_df.filter(regex=re)
    sum_df = df.apply(sum, axis=1)
    hpa_sum = sum_df[sum_df.index.str.contains('^Hpa')].sum()
    at_sum = sum_df[sum_df.index.str.contains('^AT')].sum()
    sizes = [hpa_sum, at_sum]
    colors = ['red', 'gold']
    plt.title(re, fontweight='bold',fontsize=16)
    plt.pie(sizes, colors=colors, labels=labels, explode=(0.05,0), shadow=True, autopct='%1.3f%%',
            textprops={'fontsize': 12})
    #plt.legend(patches,labels, loc='best')
    plt.axis('equal')
    #plt.show()
    plt.savefig(f'./plots/{re}_pie_plot.pdf')
    plt.clf()



# dmc_df = merge_df.filter(regex='PMC')
# print(dmc_df.head())
# dmc_sum_df = dmc_df.apply(sum, axis=1)
#
# hpa_dmc_sum_df = dmc_sum_df[dmc_sum_df.index.str.contains('^Hpa')]
# hpa_dmc_sum = hpa_dmc_sum_df.sum()
#
# at_dmc_sum_df = dmc_sum_df[dmc_sum_df.index.str.contains('^AT')]
# at_dmc_sum = at_dmc_sum_df.sum()
#
# print(hpa_dmc_sum, at_dmc_sum, hpa_dmc_sum/(hpa_dmc_sum + at_dmc_sum)*100)

#print(dmc_sum_df)


#
#print(merge_df.head())


#merge_df.to_csv('./project-data/HPA_RNA_Gene_Counts.counts', sep='\t')


# df2 = next(all_df_iter)
# print(df.head())
# print(df2.head())

#print(all_df[1].head())
