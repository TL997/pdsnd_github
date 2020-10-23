"""
Start of the Code provided by Udacity
"""

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
<<<<<<< HEAD
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(" Would you like to see data for Chicago, New York City, or Washington? ")
        print(city)
        city = city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Please provide the name of the city again as either Chicago, New York City or Washington. ')
            continue
        else:
            break
||||||| merged common ancestors
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)
=======
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(" Would you like to see data for Chicago, New York City, or Washington? ")
        print(city)
        city = city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Please provide the name of the city again as either Chicago, New York City or Washington. ')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Do you like to look at all months or either: January, February, March, April, May, or June? ")
        print(month)
        month = month.lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('Please use either all, January, February, March, April, May or June. ')
            continue
        else:
            break
>>>>>>> refactoring

<<<<<<< HEAD
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Do you like to look at all months or either: January, February, March, April, May, or June? ")
        print(month)
        month = month.lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('Please use either all, January, February, March, April, May or June. ')
            continue
        else:
            break
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day = input("Do you like to look at Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all days? ")
        print(day)
        day = day.lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('Please use either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all if you like to see all the days. ')
            continue
        else:
            break
||||||| merged common ancestors
=======
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you like to look at Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all days? ")
        print(day)
        day = day.lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('Please use either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all if you like to see all the days. ')
            continue
        else:
            break
>>>>>>> refactoring

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
<<<<<<< HEAD
    
||||||| merged common ancestors
=======

>>>>>>> refactoring
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

<<<<<<< HEAD
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
||||||| merged common ancestors
=======
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

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
>>>>>>> refactoring

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

<<<<<<< HEAD
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
||||||| merged common ancestors
=======
"""
end of code provided by Udacity
start of own code
"""

"""improving READABILITY by using p instead of popular"""
>>>>>>> refactoring

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month

<<<<<<< HEAD
    popular_month = df['month'].mode() [0]
    
    print('Most Frequent Start Month:', popular_month)
||||||| merged common ancestors
    # display the most common month
=======
# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month

    p_month = df['month'].mode() [0]
>>>>>>> refactoring

<<<<<<< HEAD
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
||||||| merged common ancestors
=======
    print('Most Frequent Start Month:', p_month)
>>>>>>> refactoring

<<<<<<< HEAD
    popular_day = df['day'].mode() [0]
    
    print('Most Frequent Start Day:', popular_day)
||||||| merged common ancestors
    # display the most common day of week
=======
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
>>>>>>> refactoring

<<<<<<< HEAD
    # TO DO: display the most common start hour
||||||| merged common ancestors
=======
    p_day = df['day'].mode() [0]
    print('Most Frequent Start Day:', p_day)
>>>>>>> refactoring

<<<<<<< HEAD
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
||||||| merged common ancestors
    # display the most common start hour
=======
    # TO DO: display the most common start hour
>>>>>>> refactoring

<<<<<<< HEAD
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode() [0]
    
    print('Most Frequent Start Hour:', popular_hour)
||||||| merged common ancestors
=======
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    p_hour = df['hour'].mode() [0]
    print('Most Frequent Start Hour:', p_hour)
>>>>>>> refactoring

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

<<<<<<< HEAD
    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode() [0]
    
    print('Most Frequent Start Station:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode() [0]
    
    print('Most Frequent End Station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    popular_route = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent combination of start and end station is ', popular_route) 
||||||| merged common ancestors
    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip

=======
    # TO DO: display most commonly used start station
    p_start = df['Start Station'].mode() [0]
    print('Most Frequent Start Station:', p_start)

    # TO DO: display most commonly used end station
    p_end = df['End Station'].mode() [0]
    print('Most Frequent End Station:', p_end)

    # TO DO: display most frequent combination of start station and end station trip
    p_route = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent combination of start and end station is ', p_route)
>>>>>>> refactoring

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totaltravel = df['Trip Duration'].sum()
    print ('The total travel time was ', totaltravel, 'seconds')

    # TO DO: display mean travel time
    totaltravel = df['Trip Duration'].mean()
    print ('The average travel time was ', totaltravel, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

<<<<<<< HEAD
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    except KeyError:
        print('The data you are looking for is not available for this city.')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        recentbirthday = df['Birth Year'].max()
        print ('The youngest user was born ', recentbirthday)
        earliestbirthday = df['Birth Year'].min()
        print ('The oldest user was born ', earliestbirthday)
        commonbirthday = df['Birth Year'].value_counts().idxmax()
        print('The most common year of birth is ', commonbirthday)
    except KeyError:
        print('The requested date is not available for the selection you have choosen')
||||||| merged common ancestors
    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth

=======
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    except KeyError:
        print('The data you are looking for is not available for this city.')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        recentbirthday = df['Birth Year'].max()
        print ('The youngest user was born ', recentbirthday)
        earliestbirthday = df['Birth Year'].min()
        print ('The oldest user was born ', earliestbirthday)
        commonbirthday = df['Birth Year'].value_counts().idxmax()
        print('The most common year of birth is ', commonbirthday)
    except KeyError:
        print('The requested date is not available for the selection you have choosen')
>>>>>>> refactoring

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""
end of own Code
start of mixed code (provided by Udacity but modified myself)
"""


def main():
<<<<<<< HEAD
    
||||||| merged common ancestors
=======

>>>>>>> refactoring
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
<<<<<<< HEAD
        break
            
    i = 0
    raw = input('Would you like to see five rows of the raw data? Please answer with yes or no. ').lower()
    
    while True:
        if raw == 'yes': 
            print(df[i:i+5])
            raw = input('Would you like to see five rows of the raw data? Please answer with yes or no. ').lower()
            i += 5
        elif raw != 'yes':
            break    
            
    restart = input('\nWould you like to restart? Enter yes or no.\n').lower() 
    
    while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
            
            if restart.lower() != 'yes':
                break
||||||| merged common ancestors

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
=======
        break

    i = 0
    raw = input('Would you like to see five rows of the raw data? Please answer with yes or no. ').lower()

    while True:
        if raw == 'yes':
            print(df[i:i+5])
            raw = input('Would you like to see five rows of the raw data? Please answer with yes or no. ').lower()
            i += 5
        elif raw != 'yes':
            break
>>>>>>> refactoring

    restart = input('\nWould you like to restart? Enter yes or no.\n').lower()

    while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()

            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
