import tablib
from constants import RAW_HEADER_ORDER, FORMATTED_HEADERS, OKTA_IMPORT_FIELDS


def create(response_data):
    count = 0
    headers = []
    tabbed_data = []
    formatted_data = []
    okta_import_data = []

    for data in response_data:
        if count == 0:
            headers = list(data.keys())
            ordered_headers = [headers[i] for i in RAW_HEADER_ORDER]
            count += 1

        values = list(data.values())
        ordered_values = [values[i] for i in RAW_HEADER_ORDER]
        formatted_row = _format_row(ordered_values, ordered_headers)
        okta_import_row = _format_row_for_okta_import(
            ordered_values, ordered_headers)
        tabbed_data.append(ordered_values)
        formatted_data.append(formatted_row)
        okta_import_data.append(okta_import_row)

    unformatted_dataset = tablib.Dataset(*tabbed_data, headers=ordered_headers)
    formatted_dataset = tablib.Dataset(
        *formatted_data, headers=FORMATTED_HEADERS)
    okta_import_dataset = tablib.Dataset(
        *okta_import_data, headers=OKTA_IMPORT_FIELDS
    )

    open('raw_user_list.csv', 'w').write(unformatted_dataset.csv)
    open('formatted_user_list.csv', 'w').write(formatted_dataset.csv)
    open('formatted_user_list.xls', 'wb').write(formatted_dataset.xls)
    open('okta_user_import.csv', 'w').write(okta_import_dataset.csv)
    open('okta_user_import.xls', 'wb').write(okta_import_dataset.xls)

    print('raw_user_list.csv created...')
    print('formatted_user_list.csv created...')
    print('formatted_user_list.xls created...')
    print('okta_user_import.csv created...')
    print('okta_user_import.xls created...')


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


def _format_row_for_okta_import(values, headers):
    count = 0
    formatted_row = []

    for value in values:
        current_column = headers[count]
        if current_column == 'profile':
            formatted_row = _map_profile(value)
        count += 1

    return formatted_row


def _map_profile(profile_data):
    def get_field(field):
        return profile_data.get(field, '')

    return list(map(get_field, OKTA_IMPORT_FIELDS))
