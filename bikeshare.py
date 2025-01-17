import time
import pandas as pd
import numpy as np

#Dicitionary with data files used for the project
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#list to validate user entry for month
month_data =['january','february','march''april','may','june','all']

#list of validate user entry for day of week
weekday_data =['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

#Code to filter dataset based on city, month, and day
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    #variable for while loop to run until a valid city is entered
    invalid_city = 1

    #while loop for handling invalid city entries
    while invalid_city:
        input_city = input('Enter City Name: chicago, new york city, washington\n').lower()
        #to validate if the user entered city is in the dictionary
        if input_city in CITY_DATA:
            city = input_city
            #invalid city is set to 0 when valid city from dictionary is entered
            invalid_city = 0

        else:
            print("Invalid city entered. Please enter a valid city")
            #to return control back to while loop until user enters a valid city
            continue



    #variable for while loop to run until a valid month is entered
    invalid_month = 1

    while invalid_month:
          # TO DO: get user input for month (all, january, february, ... , june)
        input_month = input('Enter month as all, january, february,..,june,all\n').lower()
        #to validate if the user entered month is in the list
        if input_month in month_data:
            month = input_month
            #invalid month is set to 0 when valid month from list is entered
            invalid_month = 0

        else:
            print('Invalid month entered. Please enter a valid month')
            #to return control back to while loop until user enters a valid month
            continue


    #variable for while loop to run until a valid weekday is entered
    invalid_weekday = 1


    while invalid_weekday:
          # TO DO: get user input for month (all, january, february, ... , june)
        input_day_of_week = input('Enter day of week as all, monday,..sunday\n').lower()
        #to validate if the user enterd weekday is in the list
        if input_day_of_week in weekday_data:
            day =  input_day_of_week
            #invalid weekday is set to 0 when valid weekday from the list is entered
            invalid_weekday = 0

        else:
            print('Invalid weekday entered. Please enter a valid weekday')
            #to return control back to while loop until user enters a valid weekday
            continue



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    row_start=0
    #Display 5 lines of raw data upon request
    while True:

        display_raw_data = input('\nWould you like to display 5 lines of raw data? Enter yes or no.\n')
        if display_raw_data.lower() != 'yes':
            break
        else:
            print(df.iloc[row_start:row_start+5])
            row_start+=5




     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extract month and day of week from Start time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]



    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    #print('Most Common Day:', common_day)
    print('Most Common Day:',common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip']=df['Start Station']+'|'+df['End Station']
    common_trip = df['Trip'].mode()[0].split("|")
    print('Most Commmon Trip starts at {} and ends at {}:'. format(common_trip[0], common_trip[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time:',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('counts of user types:', count_user_types)

    # TO DO: Display counts of gender
    #Check if a column exists in DataFrame
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('counts of gender:', count_gender)

    else:
        print('Gender data not available in source file')

    # TO DO: Display earliest, most recent, and most common year of birth
    #check if column exists in DataFrame
    if 'Birth Year' in df.columns:
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('most common year of birth:',most_common_year_of_birth)

    else:
        print('Birth Year data available in source file')
    earliest_trip_start = df['Start Time'].min()
    print('earliest trip is:',earliest_trip_start)
    most_recent_trip = df['Start Time'].max()
    print('recent trip is:',most_recent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
