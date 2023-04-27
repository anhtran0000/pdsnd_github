import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

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

    while True:
        city = input('Which city do you want to learn and analyze ? \n>')
        if city in  CITIES:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please provide for us a month name (e.g.  january, february, march, april, may, june) or \'all\' to apply no month filter. \n>')
        if month in MONTHS:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Could you type one of the week day you want to? (e.g. monday, tuesday, wednesday, thursday, friday, saturday, sunday) or You can type \'all\' again to apply no day filter. \n>' )
        if day in DAYS:
            break

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
    try:
        df = pd.read_csv(CITY_DATA[city])
        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract hour from the Start Time column to create an hour column
        df['hour'] = df['Start Time'].dt.hour
         # extract month and day of week from Start Time to create new columns
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
    except FileNotFoundError as e:
        print(e)
        raise FileNotFoundError
        
      
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    most_common_month =  df['month'].mode()[0]
    print("The most common month is ", most_common_month)

    # TO DO: display the most common day of week

    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is ", most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour =  df['hour'].mode()[0]
    print("The most common start hour is ", most_common_start_hour)

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        most_common_start_station = df['Start Station'].mode()[0]
        print("The most commonly used start station is ", most_common_start_station)
    except KeyError:
      print("The most commonly used start station: No data available for this month.")
    # TO DO: display most commonly used end station
    try:
        most_common_end_station = df['End Station'].mode()[0]
        print("The most commonly used end station is ", most_common_end_station)
    except KeyError:
      print("The most commonly used end station: No data available for this month.")
    # TO DO: display most frequent combination of start station and end station trip
    try:
        most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
        print("The most commonly used start station and end station are {}, {}".format(most_common_start_end_station[0], most_common_start_end_station[1]))
    except KeyError:
      print("The most commonly used start station and end station: No data available for this month.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        total_travel = df['Trip Duration'].sum()
        print("The total travel time  is ", total_travel)
    except KeyError:
      print("The total travel time: No data available for this month.")
    # TO DO: display mean travel time
    try: 
        mean_travel = df['Trip Duration'].mean()
        print("the mean travel time is ", mean_travel)
    except KeyError:
      print("the mean travel time: No data available for this month.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_counts = df['User Type'].value_counts()
        print("Counts of user types is ",user_counts)
    except KeyError:
      print("Counts of user types: No data available for this month.")
   
def user_stats_gender(df):
    
    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender is ",gender_counts)
    except KeyError:
      print("Counts of gender: No data available for this month.")
   

    # TO DO: Display earliest, most recent, and most common year of birth
def user_stats_birth(df):
    start_time = time.time()
    
    try:
        most_common_year = df['Birth Year'].mode()[0]
        print("The most common birth year is ", most_common_year)
        
        most_recent_year = df['Birth Year'].max()
        print("The most recent birth year:", most_recent_year)
        
        earliest_year = df['Birth Year'].min()
        print("The most earliest birth year:", earliest_year)
    except KeyError:
      print("No data available for this month.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_display(df): 
    view_data  = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data  == "yes":
      print(df.iloc[start_loc:start_loc + 5])
      start_loc += 5
      view_data  = input("Do you wish to continue?: ").lower()

 
def main():
    while True:
        city, month, day = get_filters()
        try:
            df = load_data(city, month, day)
        except FileNotFoundError:
            print ('Please choose another city')
            continue;
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_stats_gender(df)
        user_stats_birth(df)
        view_display(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break  


if __name__ == "__main__":
	main()

#update sth

#update sth 2