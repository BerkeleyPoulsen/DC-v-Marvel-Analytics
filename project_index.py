import pandas as pd
import matplotlib as plt

console = 0
data = pd.read_csv("comicmovies.csv")

def start():
    print(" == Type any one of the phrases below to get started ==\n")

print("\n WELCOME TO: \n")
print(
"████████╗██╗  ██╗███████╗    ██████╗  ██████╗    ██╗   ██╗    ███╗   ███╗ █████╗ ██████╗ ██╗   ██╗███████╗██╗         ██████╗  █████╗ ████████╗ █████╗ ██████╗  █████╗ ███████╗███████╗\n"
"╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔════╝    ██║   ██║    ████╗ ████║██╔══██╗██╔══██╗██║   ██║██╔════╝██║         ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝\n"
"   ██║   ███████║█████╗      ██║  ██║██║         ██║   ██║    ██╔████╔██║███████║██████╔╝██║   ██║█████╗  ██║         ██║  ██║███████║   ██║   ███████║██████╔╝███████║███████╗█████╗  \n"
"   ██║   ██╔══██║██╔══╝      ██║  ██║██║         ╚██╗ ██╔╝    ██║╚██╔╝██║██╔══██║██╔══██╗╚██╗ ██╔╝██╔══╝  ██║         ██║  ██║██╔══██║   ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══╝  \n"
"   ██║   ██║  ██║███████╗    ██████╔╝╚██████╗     ╚████╔╝     ██║ ╚═╝ ██║██║  ██║██║  ██║ ╚████╔╝ ███████╗███████╗    ██████╔╝██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║███████║███████╗\n"
"   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝      ╚═══╝      ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝\n")
start()

def general():

    # Start General
    movie_amt_all = data["Studio"]

    movie_amt_DC = len(data.loc[(data["Studio"] == "DC")])
    gross_income_DC = data.loc[(data["Studio"] == "DC")]
    DCMean = int(round(gross_income_DC["Domestic"].mean() * 100000))
    DCMeanFinal = "{:,}".format(DCMean)
    print("The gross income average of DC per movie is: $", DCMeanFinal, "domestically")

    movie_amt_MV = len(data.loc[(data["Studio"] == "Marvel")])
    gross_income_MV = data.loc[(data["Studio"] == "Marvel")]

    MVMean = int(round(gross_income_MV["Domestic"].mean() * 100000))
    MVMeanFinal = "{:,}".format(MVMean)
    print("The gross income average of Marvel per movie is: $", MVMeanFinal, "domestically")

    DCMeanInt = int(round(gross_income_DC["Worldwide"].mean() * 100000))
    DCMeanIntFinal = "{:,}".format(DCMeanInt)
    print("The gross income average of DC per movie is: $", DCMeanIntFinal, "worldwide")

    MVMeanInt = int(round(gross_income_MV["Worldwide"].mean() * 100000))
    MVMeanIntFinal = "{:,}".format(MVMeanInt)
    print("The gross income average of Marvel per movie is: $", MVMeanIntFinal, "worldwide\n")

    print("Marvel has made", movie_amt_MV, "Movies total")
    print("DC has made", movie_amt_DC, "Movies total\n")

    Difference = MVMeanInt - DCMeanInt
    CleanDifference = "{:,}".format(Difference)
    print("The difference of the two studios international revenue is about, $", CleanDifference, " on average, with DC making more on average \n")
    start()
    # End General

def advance():
    print("This will display advanced information")

def graph():
    print("This will display graphs")

def main_terminal():
    while True:
        try:
            if console == 0:
                terminal = input(" | general | general data\n | graph   | display graphs\n | advance | display advanced data \n | done    | type done to finish \n\n >: ")
                if terminal == "graph":
                    graph()
                if terminal == "advance":
                    advance()
                if terminal == "general":
                    general()
                if terminal == "done":
                    break
        except:
            print("* ERROR *")
            break

def AA_terminal():
    while True:
        try:
            if console == 1:
                terminal = input(" This is the general terminal, type done to go back one")
                if terminal == "next graph":
                    graphs()
                if terminal == "next advance":
                    advance()
                if terminal == "next general":
                    general()
                if terminal == "done":
                    break
        except:
            print("* ERROR *")
            break

if console == 0:
    main_terminal()
elif console == 1:
    AA_terminal()
else:
    exit()