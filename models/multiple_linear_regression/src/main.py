import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

from pprint import pprint
from sklearn import linear_model
import json
import pandas as pd
import statistics

with open("/data/input", "r") as file:
    data = json.load(file)

columns = {
    "release_date": [],
    "popularity": [],
    "anthony_score": [],
    "acousticness": [],
    "danceability": [],
    "duration_ms": [],
    "energy": [],
    "instrumentalness": [],
    "key": [],
    "liveness": [],
    "loudness": [],
    "mode": [],
    "speechiness": [],
    "tempo": [],
    "time_signature": [],
    "valence": [],
}
for album_uri, album in data.items():

    def aggregate_mean():
        aggregated = {
            "release_date": int(album["release_date"][:4]),
            "popularity": int(album["popularity"]),
            "anthony_score": float(album["anthony_score"]) / 10,
            "acousticness": 0,
            "danceability": 0,
            "duration_ms": 0,
            "energy": 0,
            "instrumentalness": 0,
            "key": 0,
            "liveness": 0,
            "loudness": 0,
            "mode": 0,
            "speechiness": 0,
            "tempo": 0,
            "time_signature": 0,
            "valence": 0,
        }

        for track_uri, track in album["tracks"].items():
            if track is not None:
                aggregated["acousticness"] += track["acousticness"]
                aggregated["danceability"] += track["danceability"]
                aggregated["duration_ms"] += track["duration_ms"]
                aggregated["energy"] += track["energy"]
                aggregated["instrumentalness"] += track["instrumentalness"]
                aggregated["key"] += track["key"]
                aggregated["liveness"] += track["liveness"]
                aggregated["loudness"] += track["loudness"]
                aggregated["mode"] += track["mode"]
                aggregated["speechiness"] += track["speechiness"]
                aggregated["tempo"] += track["tempo"]
                aggregated["time_signature"] += track["time_signature"]
                aggregated["valence"] += track["valence"]

        aggregated["acousticness"] /= len(album["tracks"])
        aggregated["danceability"] /= len(album["tracks"])
        aggregated["duration_ms"] /= len(album["tracks"])
        aggregated["energy"] /= len(album["tracks"])
        aggregated["instrumentalness"] /= len(album["tracks"])
        aggregated["key"] /= len(album["tracks"])
        aggregated["liveness"] /= len(album["tracks"])
        aggregated["loudness"] /= len(album["tracks"])
        aggregated["mode"] /= len(album["tracks"])
        aggregated["speechiness"] /= len(album["tracks"])
        aggregated["tempo"] /= len(album["tracks"])
        aggregated["time_signature"] /= len(album["tracks"])
        aggregated["valence"] /= len(album["tracks"])

        return aggregated

    def aggregate_meadian():
        aggregated = {
            "release_date": int(album["release_date"][:4]),
            "popularity": int(album["popularity"]),
            "anthony_score": float(album["anthony_score"]) / 10,
            "acousticness": [],
            "danceability": [],
            "duration_ms": [],
            "energy": [],
            "instrumentalness": [],
            "key": [],
            "liveness": [],
            "loudness": [],
            "mode": [],
            "speechiness": [],
            "tempo": [],
            "time_signature": [],
            "valence": [],
        }

        for track_uri, track in album["tracks"].items():
            if track is not None:
                aggregated["acousticness"].append(track["acousticness"])
                aggregated["danceability"].append(track["danceability"])
                aggregated["duration_ms"].append(track["duration_ms"])
                aggregated["energy"].append(track["energy"])
                aggregated["instrumentalness"].append(track["instrumentalness"])
                aggregated["key"].append(track["key"])
                aggregated["liveness"].append(track["liveness"])
                aggregated["loudness"].append(track["loudness"])
                aggregated["mode"].append(track["mode"])
                aggregated["speechiness"].append(track["speechiness"])
                aggregated["tempo"].append(track["tempo"])
                aggregated["time_signature"].append(track["time_signature"])
                aggregated["valence"].append(track["valence"])

        aggregated["acousticness"] = statistics.median(aggregated["acousticness"])
        aggregated["danceability"] = statistics.median(aggregated["danceability"])
        aggregated["duration_ms"] = statistics.median(aggregated["duration_ms"])
        aggregated["energy"] = statistics.median(aggregated["energy"])
        aggregated["instrumentalness"] = statistics.median(
            aggregated["instrumentalness"]
        )
        aggregated["key"] = statistics.median(aggregated["key"])
        aggregated["liveness"] = statistics.median(aggregated["liveness"])
        aggregated["loudness"] = statistics.median(aggregated["loudness"])
        aggregated["mode"] = statistics.median(aggregated["mode"])
        aggregated["speechiness"] = statistics.median(aggregated["speechiness"])
        aggregated["tempo"] = statistics.median(aggregated["tempo"])
        aggregated["time_signature"] = statistics.median(aggregated["time_signature"])
        aggregated["valence"] = statistics.median(aggregated["valence"])

        return aggregated

    # aggregated = aggregate_mean()
    aggregated = aggregate_meadian()

    columns["release_date"].append(aggregated["release_date"])
    columns["popularity"].append(aggregated["popularity"])
    columns["anthony_score"].append(aggregated["anthony_score"])
    columns["acousticness"].append(aggregated["acousticness"])
    columns["danceability"].append(aggregated["danceability"])
    columns["duration_ms"].append(aggregated["duration_ms"])
    columns["energy"].append(aggregated["energy"])
    columns["instrumentalness"].append(aggregated["instrumentalness"])
    columns["key"].append(aggregated["key"])
    columns["liveness"].append(aggregated["liveness"])
    columns["loudness"].append(aggregated["loudness"])
    columns["mode"].append(aggregated["mode"])
    columns["speechiness"].append(aggregated["speechiness"])
    columns["tempo"].append(aggregated["tempo"])
    columns["time_signature"].append(aggregated["time_signature"])
    columns["valence"].append(aggregated["valence"])

df = pd.DataFrame(columns)
pprint(df)

print('"anthony_score" corr {} with "release_date"'.format(df["anthony_score"].corr(df["release_date"])))
print('"anthony_score" corr {} with "popularity"'.format(df["anthony_score"].corr(df["popularity"])))
print('"anthony_score" corr {} with "acousticness"'.format(df["anthony_score"].corr(df["acousticness"])))
print('"anthony_score" corr {} with "danceability"'.format(df["anthony_score"].corr(df["danceability"])))
print('"anthony_score" corr {} with "duration_ms"'.format(df["anthony_score"].corr(df["duration_ms"])))
print('"anthony_score" corr {} with "energy"'.format(df["anthony_score"].corr(df["energy"])))
print('"anthony_score" corr {} with "instrumentalness"'.format(df["anthony_score"].corr(df["instrumentalness"])))
print('"anthony_score" corr {} with "key"'.format(df["anthony_score"].corr(df["key"])))
print('"anthony_score" corr {} with "liveness"'.format(df["anthony_score"].corr(df["liveness"])))
print('"anthony_score" corr {} with "loudness"'.format(df["anthony_score"].corr(df["loudness"])))
print('"anthony_score" corr {} with "mode"'.format(df["anthony_score"].corr(df["mode"])))
print('"anthony_score" corr {} with "speechiness"'.format(df["anthony_score"].corr(df["speechiness"])))
print('"anthony_score" corr {} with "tempo"'.format(df["anthony_score"].corr(df["tempo"])))
print('"anthony_score" corr {} with "time_signature"'.format(df["anthony_score"].corr(df["time_signature"])))
print('"anthony_score" corr {} with "valence"'.format(df["anthony_score"].corr(df["valence"])))

Y = df["anthony_score"]

model = linear_model.LinearRegression()
model.fit(df[["release_date"]], Y)
print('R-squared {} using "release_date"'.format(model.score(df[["release_date"]], Y)))
model.fit(df[["popularity"]], Y)
print('R-squared {} using "popularity"'.format(model.score(df[["popularity"]], Y)))
model.fit(df[["acousticness"]], Y)
print('R-squared {} using "acousticness"'.format(model.score(df[["acousticness"]], Y)))
model.fit(df[["danceability"]], Y)
print('R-squared {} using "danceability"'.format(model.score(df[["danceability"]], Y)))
model.fit(df[["duration_ms"]], Y)
print('R-squared {} using "duration_ms"'.format(model.score(df[["duration_ms"]], Y)))
model.fit(df[["energy"]], Y)
print('R-squared {} using "energy"'.format(model.score(df[["energy"]], Y)))
model.fit(df[["instrumentalness"]], Y)
print('R-squared {} using "instrumentalness"'.format(model.score(df[["instrumentalness"]], Y)))
model.fit(df[["key"]], Y)
print('R-squared {} using "key"'.format(model.score(df[["key"]], Y)))
model.fit(df[["liveness"]], Y)
print('R-squared {} using "liveness"'.format(model.score(df[["liveness"]], Y)))
model.fit(df[["loudness"]], Y)
print('R-squared {} using "loudness"'.format(model.score(df[["loudness"]], Y)))
model.fit(df[["mode"]], Y)
print('R-squared {} using "mode"'.format(model.score(df[["mode"]], Y)))
model.fit(df[["speechiness"]], Y)
print('R-squared {} using "speechiness"'.format(model.score(df[["speechiness"]], Y)))
model.fit(df[["tempo"]], Y)
print('R-squared {} using "tempo"'.format(model.score(df[["tempo"]], Y)))
model.fit(df[["time_signature"]], Y)
print('R-squared {} using "time_signature"'.format(model.score(df[["time_signature"]], Y)))
model.fit(df[["valence"]], Y)
print('R-squared {} using "valence"'.format(model.score(df[["valence"]], Y)))

print()
print('"danceability" and "instrumentalness" are the best candidates')
print()

X = df[["popularity", "danceability", "instrumentalness"]]
model.fit(X, Y)

print('R-squared {} using "popularity", "danceability" and "instrumentalness"'.format(model.score(X, Y)))

print("Bad linear model, only explains %.2f%% of the data" % (model.score(X, Y) * 100))

ax = df.plot.scatter(x='release_date', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/release_date.png')
ax = df.plot.scatter(x='popularity', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/popularity.png')
ax = df.plot.scatter(x='acousticness', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/acousticness.png')
ax = df.plot.scatter(x='danceability', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/danceability.png')
ax = df.plot.scatter(x='duration_ms', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/duration_ms.png')
ax = df.plot.scatter(x='energy', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/energy.png')
ax = df.plot.scatter(x='instrumentalness', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/instrumentalness.png')
ax = df.plot.scatter(x='key', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/key.png')
ax = df.plot.scatter(x='liveness', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/liveness.png')
ax = df.plot.scatter(x='loudness', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/loudness.png')
ax = df.plot.scatter(x='mode', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/mode.png')
ax = df.plot.scatter(x='speechiness', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/speechiness.png')
ax = df.plot.scatter(x='tempo', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/tempo.png')
ax = df.plot.scatter(x='time_signature', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/time_signature.png')
ax = df.plot.scatter(x='valence', y='anthony_score', c='DarkBlue')
fig = ax.get_figure()
fig.savefig('/app/images/valencee.png')