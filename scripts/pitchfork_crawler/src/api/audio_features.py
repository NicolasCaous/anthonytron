from colorama import Back, Fore, Style
from utils.better_pprint import pprint
from utils.better_requests import requests_retry_session
from yaspin import yaspin
import sys


def get_audio_features(
    track_id, credentials, abort_on_error=True, global_ident=6, index=1
):
    with yaspin(
        side="right",
        text=Fore.YELLOW
        + " " * global_ident
        + "[{}] GET https://api.spotify.com/v1/audio-features/{}".format(
            index, track_id
        )
        + Style.RESET_ALL,
        color="yellow",
    ) as spinner:
        res = requests_retry_session().get(
            "https://api.spotify.com/v1/audio-features/{}".format(track_id),
            headers={"Authorization": "Bearer {}".format(credentials["access_token"])},
            timeout=60,
        )
        if res.ok:
            spinner.text = (
                Fore.GREEN
                + " " * global_ident
                + "[{}] GET https://api.spotify.com/v1/audio-features/{}".format(
                    index, track_id
                )
                + Style.RESET_ALL
            )
            spinner.color = "green"
            spinner.ok("✓")
            return res.json()
        else:
            spinner.text = (
                Fore.RED
                + " " * global_ident
                + "[{}] GET https://api.spotify.com/v1/audio-features/{}".format(
                    index, track_id
                )
                + Style.RESET_ALL
            )
            spinner.color = "red"
            spinner.fail("✗")

            print()
            print(
                Fore.RED
                + " " * global_ident
                + " [{0}] {1}".format(res.status_code, res.reason)
                + Style.RESET_ALL
            )
            pprint(res.json(), color=Fore.RED)
            print()
            print()

            if abort_on_error:
                print(Fore.RED + "    Aborting!" + Style.RESET_ALL)
                sys.exit(1)
