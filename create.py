import tablib

RAW_HEADER_ORDER = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
FORMATTED_HEADERS = [
    'Id',
    'Status',
    'First Name',
    'Last Name',
    'Primary Phone',
    'Email',
    'Profile',
    'Password Last Changed',
    'Created',
    'Activated',
    'Last Updated',
    'Link',
    'Last Login',
    'Credentials',
    'Status Changed'
]


def create(response_data):
    count = 0
    headers = []
    tabbed_data = []
    formatted_data = []

    for data in response_data:
        if count == 0:
            headers = data.keys()
            ordered_headers = [headers[i] for i in RAW_HEADER_ORDER]
            count += 1

        values = data.values()
        ordered_values = [values[i] for i in RAW_HEADER_ORDER]

        tabbed_data.append(ordered_values)
        formatted_row = _format_row(ordered_values, ordered_headers)
        formatted_data.append(formatted_row)

    unformatted_dataset = tablib.Dataset(*tabbed_data, headers=ordered_headers)

    formatted_dataset = tablib.Dataset(
        *formatted_data, headers=FORMATTED_HEADERS)

    open('raw_user_list.csv', 'w').write(unformatted_dataset.csv)
    print('raw_user_list.csv created...')
    open('formatted_user_list.csv', 'w').write(formatted_dataset.csv)
    print('formatted_user_list.csv created...')
    open('formatted_user_list.xls', 'wb').write(formatted_dataset.xls)
    print('formatted_user_list.xls created...')


def _format_row(ordered_values, headers):
    count = 0
    formatted_row = []

    for value in ordered_values:
        current_column = headers[count]
        if current_column == 'profile':
            formatted_profile_values = [
                value.get('firstName', ''),
                value.get('lastName', ''),
                value.get('primaryPhone', ''),
                value.get('email')
            ]
            formatted_row.extend(formatted_profile_values)

        formatted_row.append(str(value))
        count += 1

    return formatted_row
