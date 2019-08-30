from colorama import Back, Fore, Style
from yaspin import yaspin
from pprint import pprint
import sys
import requests
import sys


def get_credentials(client_id, client_secret):
    with yaspin(
        side="right",
        text=Fore.YELLOW
        + "    POST https://accounts.spotify.com/api/token"
        + Style.RESET_ALL,
        color="yellow",
    ) as spinner:
        res = requests.post(
            "https://accounts.spotify.com/api/token",
            auth=(client_id, client_secret),
            data={"grant_type": "client_credentials"},
        )
        if res.ok:
            spinner.text = (
                Fore.GREEN
                + "    POST https://accounts.spotify.com/api/token"
                + Style.RESET_ALL
            )
            spinner.color = "green"
            spinner.ok("✓")

            print(Fore.GREEN + "     → Got credentials!" + Style.RESET_ALL)
            print()
            return res.json()
        else:
            spinner.text = (
                Fore.RED
                + "    POST https://accounts.spotify.com/api/token"
                + Style.RESET_ALL
            )
            spinner.color = "red"
            spinner.fail("✗")

            print()
            print(
                Fore.RED
                + "     [{0}] {1}".format(res.status_code, res.reason)
                + Style.RESET_ALL
            )
            pprint(res.json())
            print()
            print()

            print(Fore.RED + "    Aborting!" + Style.RESET_ALL)
            sys.exit(1)

