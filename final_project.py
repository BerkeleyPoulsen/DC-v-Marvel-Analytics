#Import and Init
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Making sure the csv is read, and the console is initialized
console = 0
data = pd.read_csv("comicmovies.csv")

#This function will display the prompt for the user to type something
def start():
    print(">>> Type any one of the phrases below to get started <<<\n")

### Defining various instances that will be used later:

#Welcome block
print("\n WELCOME TO: \n")
print(
" ████████╗██╗  ██╗███████╗    ██████╗  ██████╗    ██╗   ██╗    ███╗   ███╗ █████╗ ██████╗ ██╗   ██╗███████╗██╗         ██████╗  █████╗ ████████╗ █████╗ ██████╗  █████╗ ███████╗███████╗\n"
" ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔════╝    ██║   ██║    ████╗ ████║██╔══██╗██╔══██╗██║   ██║██╔════╝██║         ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝\n"
"    ██║   ███████║█████╗      ██║  ██║██║         ██║   ██║    ██╔████╔██║███████║██████╔╝██║   ██║█████╗  ██║         ██║  ██║███████║   ██║   ███████║██████╔╝███████║███████╗█████╗  \n"
"    ██║   ██╔══██║██╔══╝      ██║  ██║██║         ╚██╗ ██╔╝    ██║╚██╔╝██║██╔══██║██╔══██╗╚██╗ ██╔╝██╔══╝  ██║         ██║  ██║██╔══██║   ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══╝  \n"
"    ██║   ██║  ██║███████╗    ██████╔╝╚██████╗     ╚████╔╝     ██║ ╚═╝ ██║██║  ██║██║  ██║ ╚████╔╝ ███████╗███████╗    ██████╔╝██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║███████║███████╗\n"
"    ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝      ╚═══╝      ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝\n")
start()

#Used for testing
#START Test BLOCK
#END Test BLOCK

#This is the general statistics function, defined using ("general") in the console.
def general():

    # Code Berkeley Poulsen Start

    # Start General
    movie_amt_DC = len(data.loc[(data["Studio"] == "DC")])
    gross_income_DC = data.loc[(data["Studio"] == "DC")]

    # We took the data frame from where studio = either DC or marvel, and did essentially the same things for each.
    print("\n>>> STATISTICS ABOUT THEIR REVENUE <<<")
    DCMean = int(round(gross_income_DC["Domestic"].mean() * 1000000))
    DCMeanFinal = "{:,}".format(DCMean)
    print("The gross income average of DC per movie is: $", DCMeanFinal, "domestically")
    movie_amt_MV = len(data.loc[(data["Studio"] == "Marvel")])
    gross_income_MV = data.loc[(data["Studio"] == "Marvel")]
    MVMean = int(round(gross_income_MV["Domestic"].mean() * 1000000))
    MVMeanFinal = "{:,}".format(MVMean)
    print("The gross income average of Marvel per movie is: $", MVMeanFinal, "domestically")
    DCMeanInt = int(round(gross_income_DC["Worldwide"].mean() * 1000000))
    DCMeanIntFinal = "{:,}".format(DCMeanInt)
    print("The gross income average of DC per movie is: $", DCMeanIntFinal, "worldwide")
    MVMeanInt = int(round(gross_income_MV["Worldwide"].mean() * 1000000))
    MVMeanIntFinal = "{:,}".format(MVMeanInt)
    print("The gross income average of Marvel per movie is: $", MVMeanIntFinal, "worldwide")
    Difference = MVMeanInt - DCMeanInt
    CleanDifference = "{:,}".format(Difference)
    print("The difference of the two studios international revenue is about, $", CleanDifference, " on average, with DC making more on average \n")

    # Code Berkeley Poulsen End

    # Code Costa Borsas Start

    # This is simply the row amount, and not much more
    print(">>> STATISTICS ABOUT THE AMOUNT OF MOVIES <<<")
    print("Marvel has made", movie_amt_MV, "Movies total")
    print("DC has made", movie_amt_DC, "Movies total")
    movie_amt_all = len(data["Studio"])
    print("Both studios have made a combined,", movie_amt_all ,"since their inception\n")

    # Get the mean rating for each, and then display that
    print(">>> STATISTICS ABOUT TOTAL RATINGS <<<")
    DCratingsFactor = data.loc[(data["Studio"] == "DC")]
    MVratingsFactor = data.loc[(data["Studio"] == "Marvel")]
    DCratings = int(round(DCratingsFactor["Review"].mean()))
    print("The average Review score for a DC movie is:", DCratings)
    MVratings = int(round(MVratingsFactor["Review"].mean()))
    print("The average Review score for a Marvel movie is:", MVratings,"\n")

    start()

    # Code Costa Borsas End

    # End General

# Code made by Berkeley Poulsen Start

def advance():
    search = (input("\n This is the advanced terminal; \n Type in a movie to view its statistics \n\n >: ").lower())

    print(">>>", search, "<<<\n")

    searchlist = []
    searchbase = data[data.columns[0]]
    for item in searchbase:
        searchlist.append(item)

    cleanedlist = []
    for index in searchlist:
        termindex = 0
        for item in index:
            termindex += 1
            if item == "(":
                lastplace = termindex
        index = index[0:(lastplace - 2)]
        cleanedlist.append(index.lower())

    datafinal = {}
    num = 0
    for index in cleanedlist:
        datafinal[index] = num
        num += 1

    if search == "list":
        for index in cleanedlist:
            print(index)

    if search in datafinal:
        searchkey = datafinal[search]
    else:
        print("$1$ : We could not find that movie")

    try:
        if searchkey > 0:
            movie = data.iloc[searchkey, 0]
            print("This is the movie we found |", movie)
            year = data.iloc[searchkey, 1]
            print("\nThis is the year it was made |", year)
            studio = data.iloc[searchkey, 2]
            print("\nThe studio that made it was |", studio)
            domestic_diy = int(round(1000000 * data.iloc[searchkey, 3]))
            domestic = "{:,}".format(domestic_diy)
            print("\nThe amound that movie made domestically was | $", domestic)
            international_diy = int(round(1000000 * data.iloc[searchkey, 4]))
            international = "{:,}".format(international_diy)
            print("\nThe amount that movie made worldwide was | $", international)
            rating = data.iloc[searchkey, 5]
            print("\nThis movies' aggregrate rating was |", rating, "/ 100\n")

    except:
        print("$2$ : we could not search that term")
    else:
        pass
    start()

# Code made by Berkeley Poulsen End

def graph():

    # Code made by Costa Borsas and Omar Start

    loc_data_MV = data.loc[(data["Studio"] == "Marvel")]
    dates_rev_MV = loc_data_MV[["Worldwide", "Year"]]

    loc_data_DC = data.loc[(data["Studio"] == "DC")]
    dates_rev_DC = loc_data_DC[["Worldwide", "Year"]]

    plt.scatter(x=dates_rev_MV["Year"], y=dates_rev_MV["Worldwide"], label="Marvel", color="red")
    plt.scatter(x=dates_rev_DC["Year"], y=dates_rev_DC["Worldwide"], label="DC", color="blue")
    plt.ylabel("Revenue in 100,000 dollars")
    plt.xlabel("Year of Production")
    plt.legend()
    plt.title("Scatter Plot between Worldwide Revenue and Year")
    plt.show()

    # Code made by Costa Borsas End

    # Code made by Chris Higgins Start

    loc_data_MV = data.loc[(data["Studio"] == "Marvel")]
    dates_rev_MV = loc_data_MV[["Review", "Year"]]

    loc_data_DC = data.loc[(data["Studio"] == "DC")]
    dates_rev_DC = loc_data_DC[["Review", "Year"]]

    plt.scatter(x=dates_rev_MV["Year"], y=dates_rev_MV["Review"], label="Marvel", color="red")
    plt.scatter(x=dates_rev_DC["Year"], y=dates_rev_DC["Review"], label="DC", color="blue")
    plt.ylabel("Review on a scale 0f 0 - 100")
    plt.xlabel("Year of Production")
    plt.legend()
    plt.title("Scatter Plot between Ratings of Movies and Year")
    plt.show()

    start()

    # Code made by Chris Higgins and Omar End

# Code By Berkeley Start

def main_terminal():
    while True:
        try:
            if console == 0:
                terminal = input(" | general | general data\n "
                                 "| graph   | display graphs\n "
                                 "| advance | search for specific movies\n "
                                 "| done    | type done to finish\n\n "
                                 ">: ")
                if terminal == "graph":
                    graph()
                if terminal == "advance":
                    advance()
                if terminal == "general":
                    general()
                if terminal == "done":
                    break
        except:
            print("Try running this again")
            break

if console == 0:
    main_terminal()
elif console == 1:
    AA_terminal()
else:
    exit()

