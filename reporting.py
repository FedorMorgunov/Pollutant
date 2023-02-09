# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def daily_average(data, monitoring_station, pollutant):
    """The daily_average function takes a data set, a monitoring station, and a pollutant as input. It first
    determines the index of the data for the specified pollutant in the rows of data for the specified monitoring
    station. It then iterates over the rows of data in the data set, grouping the rows into sets of 24 rows
    corresponding to a single day. For each day, it calculates the average of the pollutant data for that day,
    skipping any rows that have missing data. If all rows for a day have missing data, it appends the string 'No
    data' to the list of daily averages. Finally, it returns the list of daily averages. """

    index = 2
    if pollutant == 'pm25':
        index += 1
    elif pollutant == 'pm10':
        index += 2

    avg = []

    rows = data[monitoring_station]
    for i in range(1, 8761, 24):
        hourly = []
        for j in range(24):
            if rows[i+j].split(',')[index] != 'No data':
                hourly.append(float(rows[i+j].split(',')[index]))
        if len(hourly) != 0:
            avg.append(sum(hourly) / len(hourly))
        else:
            avg.append('No data')

    return avg

    ## Your code goes here


def daily_median(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    index = 2
    if pollutant == 'pm25':
        index += 1
    elif pollutant == 'pm10':
        index += 2

    meds = []

    rows = data[monitoring_station]

    for i in range(1, 8761, 24):
        hourly = []
        for j in range(24):
            if rows[i + j].split(',')[index] != 'No data':
                hourly.append(float(rows[i + j].split(',')[index]))

        hourly.sort()

        if len(hourly) == 0:
            med = 'No data'
        elif len(hourly) % 2 == 1:
            med = hourly[len(hourly)//2]
        else:
            med = (hourly[len(hourly)//2-1] + hourly[len(hourly)//2])/2
        meds.append(med)

    return meds
    ## Your code goes here


def hourly_average(data, monitoring_station, pollutant):
    """The hourly_average function takes a data set, a monitoring station, and a pollutant as input. It first
    determines the index of the data for the specified pollutant in the rows of data for the specified monitoring
    station. It then creates a dictionary with keys corresponding to each hour of the day, and assigns an empty list
    to each key in the dictionary. It iterates over the rows of data in the data set, appending the pollutant data
    for each row to the list in the dictionary corresponding to the hour of the day indicated in the row. It then
    calculates the average of the pollutant data for each hour of the day, and returns a list of the averages in
    order of the hours of the day. """

    hourly_avgs = []

    index = 2
    if pollutant == 'pm25':
        index += 1
    elif pollutant == 'pm10':
        index += 2

    hours = dict.fromkeys(list(range(1, 25)))
    # Creating a dictionary with 24 keys corresponding to each hour

    for i in range(1, 25):
        hours[i] = []
    # Assigning an empty list to all keys in the dict

    counter = 0

    station_data = data[monitoring_station]

    for i in station_data:
        if i.split(',')[index] != 'No data' and counter != 0:
            hours[int(i.split(',')[1][:2])].append(float(i.split(',')[index]))
        counter += 1

    for i in range(1, 25):
        hourly_avgs.append(sum(hours[i])/len(hours[i]))

    return hourly_avgs

    ## Your code goes here


def monthly_average(data, monitoring_station, pollutant):
    """The function monthly_average calculates the average air quality value for each month in a year. It takes in
    three arguments: data, which is a dictionary with the name of the monitoring station as the key and the
    corresponding data for that station as the value, monitoring_station, which is the name of the monitoring station
    for which the calculation needs to be done, and pollutant, which is the type of air pollutant for which the
    calculation needs to be done.

    First, the function calculates the daily average air quality values for the given monitoring station and pollutant
    using the daily_average function. It then separates the daily averages into months, calculates the average value for
    each month, and returns the result in a list. """

    monthly_avg = []
    yearly_res = daily_average(data, monitoring_station, pollutant)

    monthly_res = yearly_res[:28]
    monthly_res = [x for x in monthly_res if not isinstance(x, str)]
    # Deleting all strings in this list ('No data' values)
    if len(monthly_res) != 0:
        monthly_avg.append(sum(monthly_res) / len(monthly_res))
    else:
        monthly_avg.append('No data')
    yearly_res = yearly_res[28:]

    monthly_res = yearly_res[:31]
    monthly_res = [x for x in monthly_res if not isinstance(x, str)]
    # Deleting all strings in this list ('No data' values)
    if len(monthly_res) != 0:
        monthly_avg.append(sum(monthly_res) / len(monthly_res))
    else:
        monthly_avg.append('No data')
    yearly_res = yearly_res[31:]

    for i in range(5):
        monthly_res = yearly_res[:30]
        monthly_res = [x for x in monthly_res if not isinstance(x, str)]
        # Deleting all strings in this list ('No data' values)
        if len(monthly_res) != 0:
            monthly_avg.append(sum(monthly_res) / len(monthly_res))
        else:
            monthly_avg.append('No data')
        yearly_res = yearly_res[31:]

        monthly_res = yearly_res[:31]
        monthly_res = [x for x in monthly_res if not isinstance(x, str)]
        # Deleting all strings in this list ('No data' values)
        if len(monthly_res) != 0:
            monthly_avg.append(sum(monthly_res) / len(monthly_res))
        else:
            monthly_avg.append('No data')
        yearly_res = yearly_res[30:]

    return monthly_avg

    ## Your code goes here


def peak_hour_date(data, date, monitoring_station, pollutant):
    """This function takes in four inputs: a data set, a date, a monitoring station, and a pollutant type. It first
    determines the index of the pollutant value in the data set. It then initializes the time and maximum pollution
    value to default values. It then iterates through the data for the specified monitoring station and date,
    and updates the time and maximum pollution value if the current pollution value is greater than the current
    maximum. Finally, it returns the time and maximum pollution value. """

    index = 2
    if pollutant == 'pm25':
        index += 1
    elif pollutant == 'pm10':
        index += 2

    time, max_pol = "01:00", 0

    station_data = data[monitoring_station]

    for i in station_data:
        if i.split(',')[0] == str(date):
            if i.split(',')[index] != 'No data' and max_pol < float(i.split(',')[index]):
                time, max_pol = i.split(',')[1][:5], float(i.split(',')[index])

    return time, max_pol

    ## Your code goes here


def count_missing_data(data, monitoring_station, pollutant):
    """Returns the number of missing data values for a given pollutant in a given monitoring station's data"""

    # Determine the index of the correct pollutant in each row of data
    index = 2
    if pollutant == 'pm25':
        index += 1
    elif pollutant == 'pm10':
        index += 2

    # Get the rows of data for the given monitoring station
    pollutant_data = data[monitoring_station]

    # Counter for the number of missing data values
    counter = 0

    # Loop through

    for i in pollutant_data:
        if i.split(',')[index] == 'No data':
            counter += 1

    return counter
    ## Your code goes here


def fill_missing_data(data, new_value, monitoring_station, pollutant):
    """The fill_missing_data function replaces all missing data values for a given pollutant in a given monitoring
    station's data with a specified new value. It does this by first determining the index of the correct pollutant
    in each row of data using an if-else statement. It then loops through the rows of data for the given monitoring
    station, replacing any instances of 'No data' at the determined index with the new value. Finally, the function
    returns the modified data. """

    index = 2
    if pollutant == 'pm25':
        index += 1
    elif pollutant == 'pm10':
        index += 2

    new_data = []

    for i in data[monitoring_station]:
        new_data.append(i.replace('No data', str(new_value)))

    return new_data

    ## Your code goes here


#print(len((daily_average(pol_data, 'Marylebone Road', 'no'))))

