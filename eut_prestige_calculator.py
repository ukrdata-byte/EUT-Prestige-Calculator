#  *************       ***                 ***        ***************************
#  *************       ***                 ***        ***************************
#  ***                 ***                 ***                  *********
#  ***                 ***                 ***                  *********
#  ***                 ***                 ***                  *********
#  *************       ***                 ***                  *********
#  *************       ***                 ***                  *********
#  ***                 ***                 ***                  *********
#  ***                 ***                 ***                  *********
#  ***                 ***                 ***                  *********
#  *************       ***********************                  *********
#  *************       ***********************                  *********
import time
import sys
import math

sys.set_int_max_str_digits(0)

WIDTH = 100
y_list = ["y", "yes", "yeah", "1", "yep"]
n_list = ["n", "no", "nah", "0", "nope"]
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def format_number(n):
    if n < 1000:
        return str(round(n, 2))
    units = [
        '', 'K', 'M', 'B', 'T', 'Qd', 'Qn', 'Sx', 'Sp', 'Oc', 'No', 'De',
        'UDe', 'DDe', 'TDe', 'QdDe', 'QnDe', 'SxDe', 'SpDe', 'OcDe', 'NoDe',
        'Vt', 'UVt', 'DVt', 'TVt', 'QdVt', 'QnVt', 'SxVt', 'SpVt', 'OcVt',
        'NoVt', 'Tg', 'UTg', 'DTg', 'TTg', 'QdTg', 'QnTg', 'SxTg', 'SpTg',
        'OcTg', 'NoTg', 'qg', 'Uqg', 'Dqg', 'Tqg', 'Qdqg', 'Qnqg', 'Sxqg',
        'Spqg', 'Ocqg', 'Noqg', 'Qg', 'UQg', 'DQg', 'TQg', 'QdQg', 'QnQg',
        'SxQg', 'SpQg', 'OcQg', 'NoQg', 'sg', 'Usg', 'Dsg', 'Tsg', 'Qdsg',
        'Qnsg', 'Sxsg', 'Spsg', 'Ocsg', 'Nosg', 'Sg', 'USg', 'DSg', 'TSg',
        'QdSg', 'QnSg', 'SxSg', 'SpSg', 'OcSg', 'NoSg', 'Og', 'UOg', 'DOg',
        'TOg', 'QdOg', 'QnOg', 'SxOg', 'SpOg', 'OcOg', 'NoOg', 'Ng', 'UNg',
        'DNg', 'TNg', 'QdNg', 'QnNg', 'SxNg', 'SpNg', 'OcNg', 'NoNg', 'Ce',
        'UCe'
    ]
    magnitude = int(math.floor(math.log10(n) / 3))
    if magnitude < len(units):
        res = n / (1000 ** magnitude)
        return f"{res:.2f}{units[magnitude]}"
    return f"{n:.2e}"


def delay_print(text, delay):
    print(text.center(WIDTH))
    time.sleep(delay)


def run_calculator():
    print("/// EUT Prestige Calculator ///".center(WIDTH))


user_input = (input("Enter your points: ")).strip()
try:
    points = float(user_input)
    PRESTIGE_REQ = 10 ** 16
    raw_prestige_points = (points / PRESTIGE_REQ) ** 0.16 + 1
    prestige_points_display = format_number(raw_prestige_points)
    if points == 0:
        delay_print("Calculating...", 0.1)
        print("Points can't be zero! (Check Automation (Bits) Baseplate!)")
    elif points > PRESTIGE_REQ:
        delay_print("Calculating...", 2)
        print(f"{GREEN}You can prestige for {prestige_points_display}!{RESET}")
        print("(Without multis!)")
        print("Do you want to see with multis? (y/n)")
        user_choice = input("Enter y (yes) / n (no): ").strip().lower()
        if user_choice in y_list:
            user_multi = input("Your multi is?: x").strip().replace("x", "")
            try:
                multi = float(user_multi)
                total_prestige_points = format_number(raw_prestige_points * multi)
                delay_print("Calculating multiplied prestige points...", 3)
                print(f"{GREEN}You can prestige for {total_prestige_points} prestige points!{RESET}")
            except ValueError:
                print(f"{user_multi} is not a number!")
        elif user_choice in n_list:
            print(f"You can do prestige for {prestige_points_display} prestige points!")
    else:
        delay_print("Calculating...", 1)
        print(f"You need {format_number(PRESTIGE_REQ):} points! You only have {format_number(points)} points!")
except ValueError:
    print(f"{user_input} is not a number!")
finally:
    print("\n" + "/// Calculation completed! ///".center(WIDTH))
if __name__ == "__main__":
    while True:
        user_choice_2 = input("Check again?: ")
        if user_choice_2 in y_list:
            print("Not available yet.")
            break
        elif user_choice_2 in n_list:
            print("///".center(WIDTH))
            break
