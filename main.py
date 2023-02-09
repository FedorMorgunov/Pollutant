# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
from reporting import *
from intelligence import *
from monitoring import *

pol_data = {'Marylebone Road': [], 'N Kensington': [], 'Harlington': []}

for key in pol_data:
    file = open('data/Pollution-London ' + key + '.csv')
    for row in file:
        pol_data[key].append(row.strip())


def choose_pollutant():
    print("Choose the pollutant: no, pm10 or pm25")
    pollutant = input()
    return pollutant


def choose_station():
    print("Choose the monitoring station: Harlington, Marylebone Road or N Kensington")
    station = input()
    return station


def main_menu():
    """Your documentation goes here"""

    print('R - Access the PR module\n'
          'I - Access the MI module\n'
          'M - Access the RM module\n'
          'A - Print the About text\n'
          'Q - Quit the application')

    choice = input()

    if choice == 'R':
        reporting_menu()

    elif choice == 'I':
        intelligence_menu()

    elif choice == 'M':
        monitoring_menu()

    elif choice == 'A':
        about()

    elif choice == 'Q':
        quit()
    # Your code goes here


def reporting_menu():
    """Your documentation goes here"""
    print('1 - Daily averages\n'
          '2 - Daily median\n'
          '3 - Hourly averages\n'
          '4 - Monthly averages\n'
          '5 - Peak hour date\n'
          '6 - Count missing data\n'
          '7 - Fill missing data\n'
          '8 - Go back')

    choice = input()

    if choice == '1':
        pollutant = choose_pollutant()
        station = choose_station()
        print(daily_average(pol_data, station, pollutant))

    elif choice == '2':
        pollutant = choose_pollutant()
        station = choose_station()
        print(daily_median(pol_data, station, pollutant))

    elif choice == '3':
        pollutant = choose_pollutant()
        station = choose_station()
        print(hourly_average(pol_data, station, pollutant))

    elif choice == '4':
        pollutant = choose_pollutant()
        station = choose_station()
        print(monthly_average(pol_data, station, pollutant))

    elif choice == '5':
        pollutant = choose_pollutant()
        station = choose_station()
        print("Choose a date between 2021-01-01 and 2021-12-31: ")
        date = input()
        print(peak_hour_date(pol_data, date, station, pollutant))

    elif choice == '6':
        pollutant = choose_pollutant()
        station = choose_station()
        print(count_missing_data(pol_data, station, pollutant))

    elif choice == '7':
        pollutant = choose_pollutant()
        station = choose_station()
        print("Choose a new value: ")
        new_value = input()
        print(fill_missing_data(pol_data, new_value, station, pollutant))

    elif choice == '8':
        pass

    main_menu()

    # Your code goes here


def monitoring_menu():
    """Your documentation goes here"""
    print('1 - Pollutants species codes\n'
          '2 - Site codes\n'
          '3 - Average pollutant value for today\n'
          '4 - Average pollutant value for a given period\n'
          '5 - Go back')

    choice = input()

    if choice == '1':
        print(get_species())

    elif choice == '2':
        print("Enter a year: ")
        year = input()
        print("Enter the species code: ")
        pollutant = input()
        print(get_sites(year, pollutant))

    elif choice == '3':
        print("Enter the site code: ")
        site = input()
        print("Enter the species code: ")
        species = input()
        average_for_today(site, species)

    elif choice == '4':
        print("Enter the site code: ")
        site = input()
        print("Enter the species code: ")
        species = input()
        print("Enter start date: ")
        start_date = input()
        print("Enter end date: ")
        end_date = input()
        print(average_for_period(site, species, start_date, end_date))

    elif choice == '5':
        pass

    main_menu()

    # Your code goes here


def intelligence_menu():
    """Your documentation goes here"""
    print('1 - Find red pixels\n'
          '2 - Find cyan pixels\n'
          '3 - Detect connected components\n'
          '4 - Detect connected components sorted\n'
          '5 - Go back')

    choice = input()

    if choice == '1':
        print(find_red_pixels('map.png', upper_threshold=100, lower_threshold=50))

    elif choice == '2':
        print(find_cyan_pixels('map.png', upper_threshold=100, lower_threshold=50))

    elif choice == '3':
        print(detect_connected_components(find_red_pixels('map.png', upper_threshold=100, lower_threshold=50)))

    elif choice == '4':
        detect_connected_components_sorted(detect_connected_components(find_red_pixels('map.png', upper_threshold=100, lower_threshold=50)))

    elif choice == '5':
        pass

    main_menu()

    # Your code goes here


def about():
    """Your documentation goes here"""
    print('ECM1400')
    print('248974')
    main_menu()
    # Your code goes here


def quit():
    """Your documentation goes here"""
    import sys
    sys.exit()
    # Your code goes here


if __name__ == '__main__':
    main_menu()
