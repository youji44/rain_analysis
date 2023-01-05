# For this project you will read in 
# and analyze actual rain data from NOAA for the Seattle Area 
# and compute average daily rain total on monthly basis.

import matplotlib.pyplot as plt

# Gloabl variables
DATA_RAIN = "seattle_weather.csv"

# read file and analyze rain, compute the averages for precipitation
def analyze_rain(filename):
    # precipitation 2dimensional list dictionary
    prec_list = {}
    # months list
    months = []
    # averages list
    averages = []

    # open and read csv file as text
    with open(filename, "r") as text:
       input_rain = text.readlines()
    
    for line in input_rain[1:]:
        line_data = line.split(",")
        (year, month, day) = line_data[0].split("-")

        month_str = convert_month(month)        
        if prec_list.get(month_str) is None:
            prec_list[month_str] = []

        prec_list[month_str].append(float(line_data[1]))
    
    # calculate average values
    for month,precs in prec_list.items():
        total = 0
        sum_prec = 0
        for prec in precs:
            sum_prec += prec
            total += 1
        if total == 0: total = 1
        averages.append(sum_prec/total)
        months.append(month)

    # return months  and averages list
    return months, averages

# convert 01, 02,..., 12 -> Jan, Feb,..., Dec
def convert_month(month):
    if month == "01": return "Jan"
    if month == "02": return "Feb"
    if month == "03": return "Mar"
    if month == "04": return "Apr"
    if month == "05": return "May"
    if month == "06": return "Jun"
    if month == "07": return "Jul"
    if month == "08": return "Aug"
    if month == "09": return "Sep"
    if month == "10": return "Oct"
    if month == "11": return "Nov"
    if month == "12": return "Dec"

# drawing the plot for average precipitation by month
def visual_plot(months, averages):
    # x: months, y: averages
    plt.bar(months,averages)
    plt.title("Analyze Rain Precipitation of Seattle Area")
    plt.show()

# main function
def main():
    filename = input("Please input Rain data file:")
    try:
        months, averages = analyze_rain(filename)
    except IOError:
        print("Occured opening or reading from the data file!")
        return
    else:
        print("Read file successfully")
    
    # drawing plots
    visual_plot(months,averages)
    
if __name__ == '__main__':
    main()
