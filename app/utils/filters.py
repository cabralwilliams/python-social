# format the date in January 1, 2022 form
def format_date(date):
    return date.strftime('%B %d, %Y')

# format plural word
def format_plural(total, word):
    if total != 1:
        return word + 's'
    return word
