# Anthonytron

The true bot of Anthony Fantano!

## Collecting Data

1. Have [docker](https://docs.docker.com/install/) installed
2. Just run:

```
./scripts/spotify_crawler/run.sh $PWD/data/Music_Classification_Sheet_Classification_of_URI_and_Score.csv
```

```
./scripts/pitchfork_crawler/run.sh $PWD/data/pitchfork.sqlite
```

## Running Models

### Multiple Linear Regression

```
./models/multiple_linear_regression/run.sh $PWD/data/crawler_output.json
```

### Tensorflow

```
./models/tensorflow/run.sh $PWD/data/crawler_output.json
```
