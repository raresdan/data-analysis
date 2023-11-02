from numpy import number
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts(df.race).round(1)

    # What is the average age of men?
    all_men = df['sex'] == 'Male'
    average_age_men = df.loc[all_men]['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    educations = df['education'].value_counts()
    total_educations = educations.sum()
    bachelors = educations['Bachelors']

    percentage_bachelors = bachelors / total_educations * 100
    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    masters = educations['Masters']
    doctorates = educations['Doctorate']
    higher_education = bachelors + masters + doctorates
    lower_education = educations.sum() - higher_education

    # percentage with salary >50K
    all_higher_education_rich = df.loc[
        df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
        & (df['salary'] == '>50K')].value_counts()
    total_higher_education_rich = len(all_higher_education_rich.index)
    higher_education_rich = total_higher_education_rich / higher_education * 100
    higher_education_rich = round(higher_education_rich, 1)

    all_lower_education_rich = df.loc[
        ~(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))
        & (df['salary'] == '>50K')].value_counts()
    total_lower_education_rich = len(all_lower_education_rich.index)
    lower_education_rich = total_lower_education_rich / lower_education * 100
    lower_education_rich = round(lower_education_rich, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    working_hours = df['hours-per-week']
    min_work_hours = working_hours.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    all_min_workers_rich = df.loc[(working_hours == min_work_hours)
                                  & (df['salary'] == '>50K')].value_counts()
    num_min_workers_rich = len(all_min_workers_rich.index)

    all_min_workers = df.loc[(working_hours == min_work_hours)].value_counts()
    num_min_workers = len(all_min_workers.index)

    rich_percentage = num_min_workers_rich / num_min_workers * 100
    rich_percentage = round(rich_percentage, 1)

    # What country has the highest percentage of people that earn >50K?
    rich_workers = df.loc[df['salary'] == '>50K']
    rich_workers_by_country = rich_workers.groupby(
        'native-country')['native-country'].count()

    total_workers_by_country = df.groupby(
        'native-country')['native-country'].count()

    df_with_rich_and_total_workers_by_country = pd.DataFrame(
        dict(rich_workers_by_country=rich_workers_by_country,
             total_workers_by_country=total_workers_by_country)).reset_index()

    df_with_rich_and_total_workers_by_country["percentage"] = df_with_rich_and_total_workers_by_country[
                                                                  'rich_workers_by_country'] \
                                                              / df_with_rich_and_total_workers_by_country[
                                                                  'total_workers_by_country'] * 100

    df_ordered = df_with_rich_and_total_workers_by_country.sort_values(by=['percentage'], ascending=False)

    highest_earning_country = df_ordered['native-country'].iloc[0]
    highest_earning_country_percentage = round(df_ordered['percentage'].iloc[0],
                                               1)

    # Identify the most popular occupation for those who earn >50K in India.
    ordered_for_india = df.loc[(df['native-country'] == 'India')
                               & (df['salary'] == '>50K')]
    occupations_numbers = ordered_for_india['occupation'].value_counts()
    top_IN_occupation = occupations_numbers.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
