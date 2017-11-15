# okta-user-export

Export user groups from Okta into various formats using the Okta API.

- `raw_user_list.csv`:  The raw data that is output from the API. 
- `formatted_user_list.csv, formatted_user_list.xls`: The data formatted into human friendly format. (WIP)
- `okta_user_import.csv, okta_user_import.csv`: Exports the data into a format that can be **imported** into another Okta instance. This was the reason for creating this repo.

## Setup

Install [pipenv](https://docs.pipenv.org/index.html) if you don't already have it.

```shell
$ pipenv --python 3.6
$ pipenv install '-e .' --dev
$ pipenv shell
```

You will need to set up a `.env` file with neccesary info from Okta.

```shell
API_TOKEN = ''
OKTA_ROOT_URL = '' # Example: 'https://dev-333222.oktapreview.com'
GROUP_ID = ''
```

## Usage

To create the files.

```shell
pipenv run python main.py
```