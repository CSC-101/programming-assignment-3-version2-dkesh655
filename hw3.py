import data

# Task 1
# The purpose of this function is must take a list (list[CountyDemographics]) and return the total 2014 population (int) based on the counties' populations.
def population_total(counties:(list[data.CountyDemographics])) -> int:
    count = 0
    for i in counties:
        count += i.population['2014 Population']
    return count

# Task 2
# The purpose of this function is to take a list (list[CountyDemographics]) and a state abbreviation (str) and return a list of county demographic objects from specified state.
def filter_by_state(counties:list[data.CountyDemographics], state_abb:str) -> list[data.CountyDemographics]:
    new_list = []
    for i in counties:
        if state_abb == i.state:
            new_list.append(i)
    return new_list

# Task 3
# The purpose of this function is to take a list (list[CountyDemographics]) and an education key of interest (str) and return the total 2014 subpopulation of that education key.
def population_by_education(counties:list[data.CountyDemographics], education_status:str) -> float:
    count = 0
    for i in counties:
        if education_status in i.education:
            count += i.education[education_status] * i.population['2014 Population'] / 100
        else:
            count = 0
    return count

# The purpose of this function is to take a list (list[CountyDemographics]) and an ethnicity key of interest (str) and return the total 2014 subpopulation of that ethnicity key.
def population_by_ethnicity(counties:list[data.CountyDemographics], ethnicity_status:str) -> float:
    count = 0
    for i in counties:
        if ethnicity_status in i.ethnicities:
            count += i.ethnicities[ethnicity_status] * i.population['2014 Population'] / 100
        else:
            count = 0
    return count

# The purpose of this function is to take a list (list[CountyDemographics]) and return the total 2014 subpopulation of the income key 'Persons Below Poverty Level'.
def population_below_poverty_level(counties:list[data.CountyDemographics]) -> float:
    count = 0
    for i in counties:
        count += i.income['Persons Below Poverty Level'] * i.population['2014 Population'] /100
    return count

# Task 4
# The purpose of this function is to take a list (list[CountyDemographics]) and an education key of interest (str) and return the percentage of the 2014 subpopulation
def percent_by_education(counties:list[data.CountyDemographics], education_status:str) -> float:
    if population_total(counties) == 0:
        return 0
    educated_percentage = population_by_education(counties,education_status)/population_total(counties)*100
    return educated_percentage

# The purpose of this function is to take a list (list[CountyDemographics]) and an ethnicity key of interest (str) and return the percentage of the 2014 subpopulation
def percent_by_ethnicity(counties:list[data.CountyDemographics], ethnicity_status:str) -> float:
    if population_total(counties) == 0:
        return 0
    ethnicity_percentage = population_by_ethnicity(counties,ethnicity_status)/population_total(counties)*100
    return ethnicity_percentage

# The purpose of this function is to take a list (list[CountyDemographics]) and return the percentage 2014 subpopulation of the income key 'Persons Below Poverty Level'.
def percent_below_poverty_level(counties:list[data.CountyDemographics]) -> float:
    below_poverty_level_percentage = population_below_poverty_level(counties)/population_total(counties)*100
    return below_poverty_level_percentage

# Task 5
# The purpose of this function is to take a list (list[CountyDemographics]), the ethnicity key of interest (str), a numeric threshold value (value), and return all county objects for which the education key is greater than the value (list).
def education_greater_than(counties:list[data.CountyDemographics], education_level:str, percentage:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in counties:
        if education_level in i.education:
            if i.education[education_level]>percentage:
                new_list.append(i)
    return new_list

# The purpose of this function is to take a list (list[CountyDemographics]), the ethnicity key of interest (str), a numeric threshold value (value), and return all county objects for which the education key is less than the value (list).
def education_less_than(counties:list[data.CountyDemographics], education_level:str, percentage:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in counties:
        if education_level in i.education:
            if i.education[education_level]<percentage:
                new_list.append(i)
    return new_list

# The purpose of this function is to take a list (list[CountyDemographics]), the ethnicity key of interest (str), a numeric threshold value (value), and return all county objects for which the education key is greater than the value (list).
def ethnicity_greater_than(counties:list[data.CountyDemographics], ethnicity:str, percentage:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in counties:
        if ethnicity in i.ethnicities:
            if i.ethnicities[ethnicity]>percentage:
                new_list.append(i)
    return new_list

# The purpose of this function is to take a list (list[CountyDemographics]), the ethnicity key of interest (str), a numeric threshold value (value), and return all county objects for which the education key is less than the value (list).
def ethnicity_less_than(counties:list[data.CountyDemographics], ethnicity:str, percentage:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in counties:
        if ethnicity in i.ethnicities:
            if i.ethnicities[ethnicity]<percentage:
                new_list.append(i)
    return new_list

# The purpose of this function is to take a list (list[CountyDemographics]) and a value (str) and return a list of county objects for which the value for key 'Persons Below Poverty Level' is greater than the value parameter.
def below_poverty_level_greater_than(counties: list[data.CountyDemographics], percentage:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in counties:
        if i.income['Persons Below Poverty Level']>percentage:
            new_list.append(i)
    return new_list

# The purpose of this function is to take a list (list[CountyDemographics]) and a value (str) and return a list of county objects for which the value for key 'Persons Below Poverty Level' is less than the value parameter.
def below_poverty_level_less_than(counties: list[data.CountyDemographics], percentage:float) -> list[data.CountyDemographics]:
    new_list = []
    for i in counties:
        if i.income['Persons Below Poverty Level']<percentage:
            new_list.append(i)
    return new_list

