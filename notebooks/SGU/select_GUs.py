
import pandas as pd

# input catalog
# folder - change to the local path
fn = '../../results/4FGL-DR4_v34_4classes_GMM_no_bcu_spp_no_coord_features_probabilistic_catalogs/'
# catalog
fn += '4FGL-DR4_v34_4classes_GMM_no_bcu_spp_no_coord_features_unas_unk_prior_shift_npar4_1Gauss_prob_cat.csv'
cat_df = pd.read_csv(fn, index_col=0)

# output filename
fn_out = fn.replace('.csv', '_select_Gauss.csv')


# select sources
mask = (cat_df['Gauss_PDF'] > 0.5) & (cat_df['Signif_Avg'] > 10) & (cat_df['CLASS1'] == 'unas')
df_out = cat_df[mask]

# sort sources
df_out = df_out.sort_values(by='Signif_Avg', ascending=False)

# save selected sorted sources
print('Save the selected sources to file:')
print(fn_out)
df_out.to_csv(fn_out)


