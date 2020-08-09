import pandas as pd
from tabulate import tabulate
import json
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

features = ['energy', 'liveness', 'tempo', 'speechiness', 'acousticness', 'instrumentalness', 'time_signature', 'danceability', 'key', 'loudness', 'valence']
df = pd.read_csv("audio_features.csv")
# print(tabulate(df[50:100], headers='keys', tablefmt='psql'))

x = df.loc[:, features].values
y = df.loc[:,['uri']].values

x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
pca.fit(x)
principalComponents = pca.fit_transform(x)
principal_df = pd.DataFrame(data = principalComponents, columns = ['PC1', 'PC2'])


# ax = sns.scatterplot(x=principal_df['PC1'], y=principal_df['PC2'], data=principal_df)
# plt.show()
# print(pca.explained_variance_ratio_)
# print(pca.components_)
# print(pca.explained_variance_)


def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrowprops=dict(arrowstyle='->',
                    linewidth=2,
                    shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)
# plot data
plt.scatter(principal_df['PC1'], principal_df['PC2'], alpha=0.2)
for length, vector in zip(pca.explained_variance_, pca.components_):
    v = vector * 3 * np.sqrt(length)

    draw_vector(pca.mean_, pca.mean_ + v)



plt.axis('equal');
plt.show()
