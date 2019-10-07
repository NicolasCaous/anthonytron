from Levenshtein import distance


def LD(s, t):
    return distance(s.lower(), t.lower())


def LD_confidence(ld, length_album_name, length_artist_name):
    if ld > (length_album_name + length_artist_name):
        return 0
    else:
        return 1.0 - ld / (length_album_name + length_artist_name)

