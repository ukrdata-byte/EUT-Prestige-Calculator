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


def format_number(n):
    if n < 1000: return str(round(n, 2))
    units = ['' 'K', 'M', 'B', 'T', 'Qd', 'Qn', 'Sx', 'Sp', 'Oc', 'No', 'De', 'UDe', 'DDe', 'TDe', 'QdDe', 'QnDe',
             'SxDe', 'SpDe', 'OcDe', 'NoDe', 'Vt', 'UVt', 'DVt', 'TVt', 'QdVt', 'QnVt', 'SxVt', 'SpVt', 'OcVt',
             'NoVt', 'Tg', 'UTg', 'DTg', 'TTg', 'QdTg', 'QnTg', 'SxTg', 'SpTg', 'OcTg', 'NoTg', 'qg', 'Uqg',
             'Dqg',
             'Tqg', 'Qdqg', 'Qnqg', 'Sxqg', 'Spqg', 'Ocqg', 'Noqg', 'Qg', 'UQg', 'DQg', 'TQg', 'QdQg', 'QnQg',
             'SxQg', 'SpQg', 'OcQg', 'NoQg', 'sg', 'Usg', 'Dsg', 'Tsg', 'Qdsg', 'Qnsg', 'Sxsg', 'Spsg', 'Ocsg',
             'Nosg', 'Sg', 'USg', 'DSg', 'TSg', 'QdSg', 'QnSg', 'SxSg', 'SpSg', 'OcSg', 'NoSg', 'Og', 'UOg',
             'DOg',
             'TOg', 'QdOg', 'QnOg', 'SxOg', 'SpOg', 'OcOg', 'NoOg', 'Ng', 'UNg', 'DNg', 'TNg', 'QdNg', 'QnNg',
             'SxNg', 'SpNg', 'OcNg', 'NoNg', 'Ce', 'UCe']
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


run_calculator()
user_input = (input("Enter your points: ")).strip()

try:
    points = float(user_input)
    PRESTIGE_REQ = 10 ** 16
    PRESTIGE_FORMULA = (points / PRESTIGE_REQ) ** 0.16 + 1
    prestige_p = format_number(PRESTIGE_FORMULA)
    if points == 0:
        delay_print("Calculating...", 0.1)
        print("Points can't be zero! (Check Automation (Bits) Baseplate!)")
    elif points > PRESTIGE_REQ:
        delay_print("Calculating...", 2)
        print(f"You can prestige for {prestige_p} prestige points!")
        print("(Without multis!)")
        print("Do you want to see with multis? (y/n)")
        user_choice = input("Enter y (yes) / n (no): ").strip().lower()
        if user_choice in ["y", "yes"]:
            user_multi = input("Your multi is?: x").strip().replace("x", "")
            try:
                multi = float(user_multi)
                PRESTIGE_MULTI_FORMULA = (PRESTIGE_FORMULA * multi)
                prestige_multi_points = format_number(PRESTIGE_MULTI_FORMULA)
                delay_print("Calculating multiplied prestige points...", 3)
                print(f"You can prestige for {prestige_multi_points} prestige points!")
            except ValueError:
                print(f"{user_multi} is not a number!")
        elif user_choice in ["n", "no"]:
            print(f"You can do prestige for {prestige_p} prestige points!")
    else:
        delay_print("Calculating...", 1)
        print(f"You need {format_number(PRESTIGE_REQ):} points! You only have {format_number(points)} points!")
except ValueError:
    print(f"{user_input} is not a number!")
finally:
    print("\n" + "/// Calculation completed! ///".center(WIDTH))
