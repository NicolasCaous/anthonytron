from colorama import Back, Fore, Style
from utils.better_pprint import pprint
from utils.better_requests import requests_retry_session
from yaspin import yaspin
import sys


def get_tracks_of_album(
    album_id, credentials, abort_on_error=True, global_ident=4, href=None
):
    if href != None:
        print_output = "GET {}".format(href)
    else:
        href = "https://api.spotify.com/v1/albums/{}/tracks".format(album_id)
        print_output = "GET https://api.spotify.com/v1/albums/{}/tracks".format(
            album_id
        )
    with yaspin(
        side="right",
        text=Fore.YELLOW + " " * global_ident + print_output + Style.RESET_ALL,
        color="yellow",
    ) as spinner:
        res = requests_retry_session().get(
            href,
            headers={"Authorization": "Bearer {}".format(credentials["access_token"])},
            timeout=60,
        )
        ret = res.json()
        if res.ok:
            spinner.text = (
                Fore.GREEN + " " * global_ident + print_output + Style.RESET_ALL
            )
            spinner.color = "green"
            spinner.ok("✓")
        else:
            spinner.text = (
                Fore.RED + " " * global_ident + print_output + Style.RESET_ALL
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
            pprint(ret, color=Fore.RED)
            print()
            print()

            if abort_on_error:
                print(Fore.RED + "    Aborting!" + Style.RESET_ALL)
                sys.exit(1)

    if "next" in ret:
        if ret["next"] != None:
            return [
                *ret["items"],
                *get_tracks_of_album(
                    album_id, credentials, abort_on_error, global_ident, ret["next"]
                ),
            ]
        else:
            return ret["items"]
    else:
        return ret
