# Notes
Following is a collection of notes that would make life less painful when
trying to set up a machine for development.

## Configuration 
Flask provides an instance config file that contains sensitive information,
such as API_KEY etc. It is a good idea to use that instead of the global 
config file so that the sensitive credentials are not exposed through the
version control. At this moment, following lines needs to be added in the
`instance/config.py` file in order for the Flask program to run.

```python
# file: instance/config.py

OPENSTATES_API_KEY = 'xxx---xxx'
MONGO_DBNAME = '[currently_using_mlabs_sandbox]'
MONGO_URI = 'found_in_mlabs_dashboard_contains_username_password_for_db'
```
