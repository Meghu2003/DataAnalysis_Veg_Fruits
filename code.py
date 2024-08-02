#imported the pandas and mysql connector
import pandas as pd
import mysql.connector as my
import matplotlib.pyplot as plt
import numpy as np
TPURPLE = '\033[35m'
ENDC = '\033[m'
my_conn = my.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'root',
                     database = 'CONSUMER_GOODS')

#conversion of data in mysql to dataframe
wholesale = pd.read_sql("select * from Veg_Fru_WholesaleRate;",
                        my_conn)
consumption = pd.read_sql("select * from ConsumptionRate_1",
                          my_conn)
vegetables = wholesale.head()
fruits = wholesale.tail()
#submenu represents Data Visualisation
def submenu():
    choice1 = 0
    while choice1!=7:
        print()
        print("-X-"*20)
        print(TPURPLE+"COMPARISON BETWEEN VARIOUS VEGETABLES AND FRUITS USING GRAPHS",ENDC)
        print("-X-"*20)
        print("1.bar_graph\n2.line_graph\n3.histogram")
        print("4.step frequency\n5.pie chart\n6.scatter plot")
        choice1 = int(input("choose any of the graphs::"))
        x1 = vegetables.Name
        y1 = vegetables.Rate_perkg
        x2 = fruits.Name
        y2 = fruits.Rate_perkg
        x3 = consumption.Region
        y3 = consumption.Mean_Veg_Fru_intake
        A,B = np.arange(len(y1)),np.arange(len(y2))
        if choice1 == 1:
            plt.bar(A, y1, color = 'g',
                    width = 0.3, label = 'Vegetables')
            plt.bar(B+0.25, y2, color = 'red',
                    width = 0.3, label = 'Fruits')
            plt.title("MULTI BARGRAPH FOR VEGETABLES&FRUITS")
            plt.legend(loc = 'upper right')
            plt.show()
            plt.barh(x3, y3, color = 'olive')
            plt.title("CONSUMPTION RATE IN EACH REGION")
            plt.show()

        elif choice1 == 2:
            plt.plot(A, y1, color = 'g',
                     label = 'Vegetables')
            plt.plot(A+0.25, y2, color = 'red',
                     linestyle = 'dashdot', label = 'Fruits')
            plt.legend(loc = 'upper right')
            plt.show()

        elif choice1 == 3:
            plt.hist([y1, y2], bins = None,
                     cumulative = False, histtype = 'bar',
                     color = ['r','b'], label = ['Vegetables','Fruits'])
            plt.legend(loc = 'upper right')
            plt.title('HISTOGRAM FOR WHOLESALE')
            plt.show()

        elif choice1 == 4:
            plt.hist(y3, bins = None,
                     cumulative = True, histtype = 'step')
            plt.show()
        
        elif choice1 == 5:
            expl = [0,0,2,0,0.2]
            plt.pie(y1, labels = x1,
                    explode = expl, autopct = '%2.1f%%')
            plt.title('PIE CHART FOR DIFFERENT VEGETABLES')
            plt.show()
            plt.pie(y2, labels = x2,
                    explode = expl, autopct = '%2.1f%%')
            plt.title('PIE CHART FOR DIFFERENT FRUITS')
            plt.show()
            plt.pie(y3, labels = x3,
                    autopct = '%2.1f%%')
            plt.title('PIE CHART FOR DIFFERENT REGIONS')
            plt.show()

        elif choice1 == 6:
            plt.scatter(A, y1, s = 100,
                        c = 'blue', marker = '+')
            plt.scatter(B, y2, s = 100,
                        c = 'green', marker = 's')
            plt.title("SCATTER PLOT FOR WHOLESALE PRICES")
            print()
            plt.xlabel("Fruits and Vegetables")
            plt.ylabel("Wholesale Prices")
            plt.show()
            plt.scatter(x3, y3, s = 100,
                        c = 'green', marker = 's')
            plt.title("SCATTER PLOT FOR CONSUMPTION RATES")
            plt.xlabel("Regions in India")
            plt.ylabel("Consumption Rates")
            plt.show()
        
        else:
            mainmenu()

#Data Analysis
def submenu3():
    choice3 = 0
    while choice3!=5:
        print("-"*60)
        print(TPURPLE+"ANALYSING THE WHOLESALE AND CONSUMPTION RATES",ENDC)
        print('-'*60)
        print("1.Maximum, Minimum and Average of the wholesale rates.")
        print("2.Ascending order of the wholesale rates.")
        print("3.Maximum, Minimum and Average of the consumption rates.")
        print("4.Ascending order of the consumption rates.")
        choice3 = int(input("Choose any of the above::"))
        if choice3 == 1:
            print("Maximum wholesale price among them::",wholesale['Rate_perkg'].max())
            print()
            print("Minimum wholesale price among them::",wholesale['Rate_perkg'].min())
            print()
            print("Average wholesale price among them::",wholesale['Rate_perkg'].mean())
            print()

        elif choice3 == 2:
            print("The ascending order by wholesale rate::\n",wholesale.sort_values('Rate_perkg'))

        elif choice3 == 3:
            print("Maximum consumption rate among them::",consumption['Mean_Veg_Fru_intake'].max())
            print()
            print("Minimum consumption rate among them::",consumption['Mean_Veg_Fru_intake'].min())
            print()
            print("Average consumption rate among them::",consumption['Mean_Veg_Fru_intake'].mean())
            print()

        elif choice3 == 4:
            print("The ascending order by consumption rate::\n",consumption.sort_values('Mean_Veg_Fru_intake'))

        else:
            mainmenu()    

#Main Menu
def mainmenu():
    choice = 0
    while choice!=4:
        print("-"*60)
        print("CONTENTS")
        print('-'*60)
        print("1.Contents\n2.Data Visualisation\n3.Data Analysis\n4.Exit")
        choice = int(input("Choose a option from above::"))
        if choice == 1:
            print(TPURPLE+"Contents of WHOLESALE Rates",ENDC)
            print(wholesale)
            print("-"*35)
            print(TPURPLE+"Contents of CONSUMPTION Rates",ENDC)
            print(consumption)

        elif choice == 2:
            submenu()

        elif choice == 3:
            submenu3()

        else:
            print("That's the end of project")

mainmenu()