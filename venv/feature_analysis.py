import pandas as pd
from tabulate import tabulate
import json
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
from sklearn import preprocessing
from sklearn.cluster import KMeans
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
from sklearn.metrics import silhouette_samples, silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer
from yellowbrick.datasets import load_nfl


df = pd.read_csv("final_audio_features.csv")
df1 = pd.read_csv("final_audio_features.csv")
df1.drop(['duration_ms', 'uri', 'genre', 'type', 'mode', 'key'], axis=1, inplace=True)


#  ----------------------------------------- Scaled Data  ---------------------
x = df1.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled1 = min_max_scaler.fit_transform(x)
df1 = pd.DataFrame(x_scaled1)
df1.columns = ["energy", "liveness", "tempo", "speechiness", "acousticness", "instrumentalness", "time_signature", "danceability", "loudness",'valence' ]


# --------------------------------- Violing plot and heat map --------------

# ax = sns.heatmap(df1.cov(),vmin=-0.08, vmax=0.08, annot = True)
# plt.show()

# df2 = df1.melt(var_name='groups', value_name='vals')
# ax = sns.violinplot(x="groups", y="vals", data=df2, linewidth = 0.6, inner = 'point', scale= 'width')
# plt.show()


#  -------------------------------- Finding k  -------------------------------

df1.drop(['liveness', 'speechiness', 'instrumentalness', 'loudness', 'time_signature'], axis=1, inplace=True)

x = df1.values #returns a numpy array
x_scaled2 = min_max_scaler.fit_transform(x)
df1 = pd.DataFrame(x_scaled2)

distortions = []
for i in range(1, 11):
    km = KMeans(
        n_clusters=i, init='random',
        n_init=10, max_iter=300,
        tol=1e-04, random_state=0
    )
    km.fit(x_scaled2)
    distortions.append(km.inertia_)

# plt.plot(range(1, 11), distortions, marker='o')
# plt.xlabel('Number of clusters')
# plt.ylabel('Distortion')
# plt.show()

#  ------------------------ k-means Clustering ---------------------

kmeans = KMeans(init="k-means++",
                n_clusters=3,
                random_state=15,
                max_iter = 500).fit(x_scaled2)
df1['kmeans'] = kmeans.labels_
df1.columns = ['energy', 'tempo', 'acousticness','danceability','valence', 'kmeans']

grouped = df1.groupby(['kmeans']).mean()
kmeans = df1['kmeans']
df['kmeans'] = kmeans
grouped = df.groupby(['kmeans']).count()


# ---------------------------------- Violin Plot for each cluster ------------------
c0 = df[df['kmeans']==0]
c1 = df[df['kmeans']==1]
c2 = df[df['kmeans']==2]
c0.drop(['kmeans','duration_ms', 'uri', 'genre', 'type', 'mode', 'key', 'liveness', 'speechiness', 'instrumentalness', 'time_signature', 'loudness'], axis=1, inplace=True)
c1.drop(['kmeans','duration_ms', 'uri', 'genre', 'type', 'mode', 'key', 'liveness', 'speechiness', 'instrumentalness', 'time_signature', 'loudness'], axis=1, inplace=True)
c2.drop(['kmeans','duration_ms', 'uri', 'genre', 'type', 'mode', 'key', 'liveness', 'speechiness', 'instrumentalness', 'time_signature', 'loudness'], axis=1, inplace=True)

x = c0.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
c0_scaled = min_max_scaler.fit_transform(x)
c0 = pd.DataFrame(c0_scaled)
c0.columns = ["energy", "tempo", "acousticness","danceability", 'valence' ]
c0=c0.melt(var_name='groups', value_name='vals')

x = c1.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
c1_scaled = min_max_scaler.fit_transform(x)
c1 = pd.DataFrame(c1_scaled)
c1.columns = ["energy", "tempo", "acousticness","danceability", 'valence' ]
c1=c1.melt(var_name='groups', value_name='vals')

x = c2.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
c2_scaled = min_max_scaler.fit_transform(x)
c2 = pd.DataFrame(c2_scaled)
c2.columns = ["energy", "tempo", "acousticness","danceability", 'valence' ]
c2=c2.melt(var_name='groups', value_name='vals')

# f, axes = plt.subplots(3, 1)
# ax = sns.violinplot( data=c1 ,x="groups", y="vals", linewidth = 0.6, inner = 'point', scale= 'width', ax=axes[0])
# ax = sns.violinplot( data=c2 ,x="groups", y="vals", linewidth = 0.6, inner = 'point', scale= 'width', ax=axes[1])
# ax = sns.violinplot( data=c0 ,x="groups", y="vals", linewidth = 0.6, inner = 'point', scale= 'width', ax=axes[2])
# plt.show()

# ---------------------------------- Genre -------------------------------------

d0 = df[df['kmeans']==0]
d1 = df[df['kmeans']==1]
d2 = df[df['kmeans']==2]

d1 = d1.astype(str)
d0 = d0.astype(str)
d2 = d2.astype(str)

words = ''
for i in d1.genre.values:
    words += '{} '.format(i.lower()) # save all words in a string

wd = pd.DataFrame(Counter(words.split()).most_common(20), columns=['word', 'frequency'])
data1 = dict(zip(wd['word'].tolist(), wd['frequency'].tolist()))

words = ''
for i in d2.genre.values:
    words += '{} '.format(i.lower()) # save all words in a string
wd = pd.DataFrame(Counter(words.split()).most_common(20), columns=['word', 'frequency'])
data2 = dict(zip(wd['word'].tolist(), wd['frequency'].tolist()))

words = ''
for i in d0.genre.values:
    words += '{} '.format(i.lower()) # save all words in a string
wd = pd.DataFrame(Counter(words.split()).most_common(20), columns=['word', 'frequency'])
data0 = dict(zip(wd['word'].tolist(), wd['frequency'].tolist()))

wc = WordCloud(background_color='white',
                width=800,
                height=400,
                max_words=100).generate_from_frequencies(data0)
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
# plt.show()

wc = WordCloud(background_color='white',
                width=800,
                height=400,
                max_words=100).generate_from_frequencies(data1)
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
# plt.show()

wc = WordCloud(background_color='white',
                width=800,
                height=400,
                max_words=100).generate_from_frequencies(data2)
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
# plt.show()