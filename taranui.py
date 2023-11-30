"""
accessory module used to design and color the output text for pretty terminal
output.
"""
import sys
import rich
import threading
import multiprocessing

from time import sleep
from rich import print as rprint
from rich.progress import Progress

logo_art = """
 _______                             _______         __
|_     _|.---.-..----..---.-..-----.|   _   |.-----.|__|
  |   |  |  _  ||   _||  _  ||     ||       ||  _  ||  |
  |___|  |___._||__|  |___._||__|__||___|___||   __||__|
                                             |__|
"""

ascii_art = """
 _______                             _______         __
|_     _|.---.-..----..---.-..-----.|   _   |.-----.|__|
  |   |  |  _  ||   _||  _  ||     ||       ||  _  ||  |
  |___|  |___._||__|  |___._||__|__||___|___||   __||__|
                                             |__|

.+++++++++++++++++++++++++++++++++++++++++++++++++.
 *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
  #@@@@@==================================%@@@@@%.
  .@@@@@*                                -@@@@@@:
   -@@@@@:                              .%@@@@@=
    +@@@@%                              +@@@@@*
     -----:                            .::::::
          .:.........                 .:
                 :@@%.       :@%%-::...
                  +@@+       #%.   :
                   %@@:     -@=   :.
                   :@@#    .%@#=::.
                    *@@=   +@:   :
                    .%@@. :@*   ::
                     -@@* #@=   ::
                      *@@*@@- .:
                      .%@@@+.:.
                       -@@#:.
                        *@#

"""

info1 = """
TARAN API
OPEN SOURCE OSINT
//

"""

info2 = """
//

BOOT TARLAN ON HARD DISK
PARTITION TOOLS
KERNEL 1.1.0 - x64
ANDROID LIVE + INSTALL(1)
CONSOLE MODE(2)
"""
def start(banner: str, delay=0.2):
    """
    Parameters:
        banner
        delay=0.2
    """
    # import random
    from time import sleep
    from rich import print as rprint

    for line in banner.split("\n"):
        for character in line:
            if character in ["#", "@", "%", "&"]:
                rprint(f"[yellow]{character}", end="", flush=True)
            else:
                rprint(f"[bright_red]{character}", end="", flush=True)
        print()

    animation(info1)
    sleep(0.5)
    rprint("[on red][black]BOOTING...                                        ")
    animation("TARAN LIVE + INSTALL")
    rprint("")
    sleep(0.5)
    progress()
    animation(info2)
    sleep(delay)

def logo(banner: str):
    """
    Parameters:
        logo
    """
    # import random
    from rich import print as rprint

    for line in banner.split("\n"):
        for character in line:
            if character in ["#", "@", "%", "&"]:
                rprint(f"[yellow]{character}", end="", flush=True)
            else:
                rprint(f"[bright_red]{character}", end="", flush=True)
        print()

def load():
	for i in range(10):
		rprint("[red]Loading: ", i * 10, "[red]%", end="\r", flush=True)
		sleep(0.5)
	rprint("[red]Progress DONE 100%")

def progress():
	with Progress() as progress:
		task1 = progress.add_task("[red3][+] Connecting System", total=100)
		task2 = progress.add_task("[red3][+] Connecting Console", total=100)

		while not progress.finished:
			progress.update(task1, advance=1)
			progress.update(task2, advance=2)
			sleep(0.02)

def animation(text):
	for char in text:
		rprint(f"[red]{char}", end='', flush=True)
		sleep(0.02)


class Notify:
	"A helper class for notifications of TaranAPI process"

	@staticmethod
	def start():
		start(ascii_art, delay=2)

	@staticmethod
	def logo():
		logo(logo_art)

if __name__ == "__main__":
	start(ascii_art)
