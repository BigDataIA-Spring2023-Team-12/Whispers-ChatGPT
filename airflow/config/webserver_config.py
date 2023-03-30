from airflow import configuration as conf

# Disable authentication
conf.set('webserver', 'authenticate', 'False')
