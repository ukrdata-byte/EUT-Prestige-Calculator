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

# //// Increase max digit number
sys.set_int_max_str_digits(0)

width = 100
calc = "Calculating..."

print("/// EUT Prestige Calculator ///".center(width))

def format_number(n):
    if n < 1000:
        return str(n)
    for unit in ['K', 'M', 'B', 'T', 'Qd', 'Qa', 'Qi', 'Qn', 'Sx', 'Sp', 'Oc', 'No', 'De', 'UDe', 'DDe', 'TDe']:
        n /= 1000
        if n < 1000:
            return f"{n:.2f}{unit}"
    return f"{n:.2e}"
def delayprint(text, delay=0.5):
    print(text.center(width))
    time.sleep(delay)
userinput = (input("Enter your points: "))
try:
    points = float(userinput)
    prestige_req = 10 ** 16
    prestige_points = (points / prestige_req) ** 0.16 + 1
    prestige_p = format_number(prestige_points)
    if points == 0:
        delayprint("Calculating...", 0.5)
        print("Points can't be zero! (Check Automation (Bits) Baseplate!)")
    elif points > prestige_req:
        delayprint("Calculating...", 2)
        print(f"You can prestige for {format_number(prestige_points)} prestige points!")
        print("(Without multis!)")
        print("Do you want to see with multis? (y/n)")
        userchoice = input("Enter y (yes) / n (no): ").strip().lower()
        if userchoice == "y":
            rawmulti = input("Your multi is?: x").strip().replace("x", "")
            try:
                multi = float(rawmulti)
                prestigemulti = (prestige_points * multi)
                prestigemulti_points = format_number(prestigemulti)
                delayprint("Calculating multiplied prestige points...", 3)
                print(f"You can prestige for {prestigemulti_points} prestige points!")
            except ValueError:
                print(f"{rawmulti} is not a number!")
        elif userchoice == "n":
            print(f"You can do prestige for {prestige_p} prestige points!")
    else:
        delayprint("Calculating...", 2)
        print(f"You need {format_number(prestige_req):} points! You only have {format_number(points)} points!")
except ValueError:
    print(f"{userinput} is not a number!")
finally:
    print("\n" + "/// Calculation completed! ///".center(width))