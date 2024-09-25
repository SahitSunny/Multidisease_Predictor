number_to_blood_group = {
        'A+': 11,
        'A-': 12,
        'B+': 13,
        'B-': 14,
        'AB+': 15,
        'AB-': 16,
        'O+': 17,
        'O-': 18
    }

def blood_group_mapper(bg):
    bg = bg.upper()
    if bg in number_to_blood_group:
        return number_to_blood_group[bg]
    else:
        return None
    
def yes_no_mapper(choice):
    choice = choice.lower()
    return 1 if choice == 'yes' else 0


def add_days_to_date(user_input_date, model_output_days):
    model_output_days_int = int(model_output_days)
    new_date = user_input_date + timedelta(days=model_output_days_int)

    return new_date.strftime('%Y-%m-%d')