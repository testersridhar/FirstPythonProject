def get_full_name(first_name,last_name,formater):
    return formater(first_name,last_name)
full_name=get_full_name(
    'Sridhar',
    'Chittiboina',
    lambda first_name,last_name:f"{first_name},{last_name}"
)