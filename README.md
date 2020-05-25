# HMS_Django
Hospital Management System using Django 

### Basic Requirements
Python version 3.8

### Steps to run this project
1. Clone the repository using ``` git clone https://github.com/charithesh16/HMS_Django.git ```
2. Open the folder and create a python virtual enviornment using 
``` python3 -m venv venv```
3. Activate the virtual environment
   - In windows ``` venv\Scripts\activate```
   - In Ubuntu ```source venv/bin/activate```
4. Install the required modules using ``` pip install -r requirements.txt ```
5. Run the following commands 
   - ```python3 manage.py makemigrations```
   - ```python3 manage.py migrate```
   - To create superuser ```python3 manage.py createsuperuser``` and follow the steps to register.
   - to start the server run ```python3 manage.py runserver```
6. Follow the below urls for corresponding functionalities. Append these urls after ```127.0.0.1:8000```
   - For registration ``` accounts/register```
   - For login ```accounts/login```
   - For admin panel ```admin/```
7. to login as receptionist create receptionist profile in the admin panel and login with the receptionist credentials.
   - Note : enter 3 in the type field when u create the receptionist user
