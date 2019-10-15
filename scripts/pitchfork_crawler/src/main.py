from api.credentials import get_credentials
from api.search import search_album
from colorama import init as colorama_init
from colorama import Back, Fore, Style
from utils.better_pprint import pprint
from utils.cache import CacheManager
from utils.levenshtein_distance import LD, LD_confidence
import csv
import json
import sqlite3
import sys
import time

cache = CacheManager("/cache")

conn = sqlite3.connect("/app/input.sqlite")

cur = conn.cursor()
cur.execute("ALTER TABLE reviews ADD COLUMN COLNEW TEXT;")
conn.commit()

colorama_init()
print()

print(Fore.GREEN + "    Data:" + Style.RESET_ALL)
i = 1
for row in cur.execute("SELECT * FROM reviews LIMIT 10"):
    print(
        Fore.GREEN
        + "     [{0}]: ".format(i)
        + Style.RESET_ALL
        + "{0} by {1}".format(row[1], row[2])
    )
    i += 1

if next(cur.execute("SELECT COUNT(*) FROM reviews"))[0] > 10:
    print(Fore.GREEN + "     ..." + Style.RESET_ALL)

print()
print()

print(Fore.GREEN + "    Continue? [y/n]: " + Style.RESET_ALL, end="")
confirm = input()

if confirm.lower() != "y":
    print(Fore.RED + "    Aborting!" + Style.RESET_ALL)
    sys.exit(1)
else:
    print()
    print()

print(
    Fore.YELLOW
    + "    [HINT] Create your Client ID at https://developer.spotify.com/dashboard"
    + Style.RESET_ALL
)
print(Fore.GREEN + "    Client ID: " + Style.RESET_ALL, end="")
client_id = input()

print(Fore.GREEN + "    Client Secret: " + Style.RESET_ALL, end="")
client_secret = input()
print()
print()

start_time = time.time()
credentials_time = time.time()

credentials = get_credentials(client_id, client_secret)

output = {}

search_count = 0
percentile95 = 0
db_size = next(cur.execute("SELECT COUNT(*) FROM reviews"))[0]
for row in cur.execute(
    "SELECT * FROM reviews WHERE title IS NOT NULL AND title != '' AND title != '*' AND artist IS NOT NULL AND artist != ''"
):
    search_count += 1

    if cache[row[0]] is not None:
        output[row[0]] = cache[row[0]]
        print(
            Fore.GREEN
            + "    [{}/{}] FROM CACHE Album: {} by {}.".format(
                search_count, db_size, row[1], row[2]
            )
            + Style.RESET_ALL
        )

    else:
        print()
        print(
            Fore.GREEN
            + "    [{}/{}] Album: {} by {}.".format(
                search_count, db_size, row[1], row[2]
            )
            + Style.RESET_ALL
        )

        output[row[0]] = []

        albums = search_album("{0}".format(row[1]), credentials)["albums"]["items"]
        for album in albums:
            ld1 = LD(row[1], album["name"])
            ld2 = (
                LD(row[2], album["artists"][0]["name"])
                if row[2].lower() != "various artists"
                else 0
            )
            output[row[0]].append(
                (
                    album["uri"],
                    ld1 + ld2,
                    ld1,
                    ld2,
                    LD_confidence(ld1 + ld2, len(row[1]), len(row[2])),
                )
            )

        output[row[0]].sort(key=lambda tup: tup[1])
        cache[row[0]] = output[row[0]]

        if len(output[row[0]]) > 0:
            print(
                Fore.GREEN
                + "     → Got search! best candidate: "
                + str(output[row[0]][0])
                + Style.RESET_ALL
            )
        else:
            print(Fore.YELLOW + "     → No search result!" + Style.RESET_ALL)

    if len(output[row[0]]) > 0:
        if output[row[0]][0][4] <= 0.95:
            percentile95 += 1
        else:
            pass

print()
print()
print(
    Fore.GREEN
    + "     ☮ {0} searches ({1} bigger than 95%% in confidence) completed in {2:.3f} seconds! ☮".format(
        search_count, search_count - percentile95, time.time() - start_time
    )
    + Style.RESET_ALL
)
print()

with open("output.json", "w") as file:
    json.dump(output, file)
