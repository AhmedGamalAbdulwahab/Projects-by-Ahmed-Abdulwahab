import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    month=''
    day=''
    
    while True:
        city = input("Choose one city to analyze between (Chicago, New York or Washington)\n").lower()
        if city not in CITY_DATA:
            print("City not found.")
            continue   
        else:
            break
    month = input('Enter a month name or type (all) for all months\n')

    
    day = input('Enter a day of a week or type (all) for all week days\n')
    
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    freq_month = df['month'].mode()[0]
    print('The most frequent month is: {}\n'.format(freq_month))

    
    freq_day = df['day_of_week'].mode()[0]
    print('The most frequent day is: {}\n'.format(freq_day))

    
    freq_hour = df['hour'].mode()[0]
    print('The most frequent hour is: {}\n'.format(freq_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    common_start = df['Start Station'].mode()[0]
    print('The most common start station is: {}\n'.format(common_start))

    
    common_end = df['End Station'].mode()[0]
    print('The most common end station is: {}\n'.format(common_end))

     
    station_combination = df[['Start Station', 'End Station']].mode()[0]
    print('The most common start station and end station combined are: {}, {}\n'.format(station_combination[0],station_combination[1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    print('Total travel time is: ' + df['Trip Duration'].sum() + '\n')

    
    print('Average travel time is: ' + df['Trip Duration'].mean() + '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    print(df['User Type'].value_counts())
    if 'Gender' in df:
    
        print(df['Gender'].value_counts())
    else:    
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')    
    if 'Birth Year' in df:
        print('Earliest birth year is: ' + df['Birth Year'].min() + '\n')
        print('Most recent birth year is: ' + df['Birth Year'].max() + '\n')
        print('Most common birth year is: ' + df['Birth Year'].mode()[0] + '\n')
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print('Year stats cannot be calculated because Year does not appear in the dataframe')    
        
def display_data(df):
    """Displays data as the user asks."""
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[0:5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display != 'yes':
            break
            


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
