from functions_twiter import open_and_login, scroll, scroll_to_bottom
from functions_twiter import collect_full_timeline
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

print("WARNING", "\n", "You can enter your username and password here or you can read it in through a separate file called pw.py. ", "\n",
      "Note that there is no error control on this part. If you provide wrong login credentials that's your problem :)", "\n",
      "If you plan on using a pw.py file, just leave at least one of the fields empty", "\n")
login = input("input login: ")
pw = input("input password: ")

if len(login) == 0 or len(pw) == 0:
    print("trying to read credentials from pw.py file")
    import pw
    login = pw.login
    pw = pw.psw

driver = open_and_login('firefox', login, pw)
scroll_to_bottom(driver, security=1)

timeline = collect_full_timeline(driver, testing=False, test_runs=2, return_cleaned=True, write_csv=True)
#print(timeline)