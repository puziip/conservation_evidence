# Conservation Evidence

Task: 
- In this task we would like you to take some biodiversity conservation data, model it effectively in Django and provide some guidance on how this might be deployed. Use any resources you would normally use to complete this task, that includes StackOverflow and AI-tooling such as Github Copilot.
Please spend no more than an hour and a half on this task.

## Initial Commit note:
Initial commit for this project is a bare bones Django setup using the 
inbuilt ORM and MVC to set up a data service for conservation evidence data.

## Local Installation
This would require a standard Python package set up. Locally it would be set up
along these lines:

- Create a virtual environment on the production server (if no already there)
- git pull (clone the repo)
- Use the command below in stall the package requirements 
  - ```pip install -r requirements.txt```
- Run the migrations:
  - ```python manage.py makemigrations```
  - ```python manage.py migrate```
- Import the data:
  - ```python manage.py import_data [path_to_file]```
- Run the local server:
  - ```python manage.py runserver```

See these links for data as per the exercise in JSON format:
- http://127.0.0.1:8000/high_score_interventions/
- http://127.0.0.1:8000/average_score/

## Specific Considerations for Production Set Up
- A complete README for production installation
- For the production server use something like e.g. nginx
- Use a proper relational database such as PostgreSQL
- Add more checks in for malformed data
- Use a container virtual environment model such as docker
- Make sure tests (unit) written
- Create a proper HTML template structure to display the data e.g. sortable table
- Security: This might include only those with access to access the data. API
would use a token of some kind.
