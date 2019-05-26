# CollabMates-Python-Assignment
Assignment For Collabmates

STEPS -
Install the requirements in requirements.py
1. specify the database in PythonAssignment/assignment/assignment/settings.py
2. go to PythonAssignment/assignment
3. run following commands -
    1. python manage.py makemigrations
    2. python manage.py migrate

4. api get url = /api/get

5. dashboard url = /videos

The get response of the api endpoint is paginated by 10 videos per page.
The background api call is made every 10 seconds.
