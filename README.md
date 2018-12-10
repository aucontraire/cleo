# cleo


### To run the server:

```$ DB_NAME=cleo_db DB_USER=user_00 DB_PASSWORD=user_00_pwd HOST=localhost PORT=3306 SECRET_KEY='somearbitrarykey' python3 manage.py runserver 0:5000```

### To run the main tests:

```$ DB_NAME=cleo_db DB_USER=user_00 DB_PASSWORD=user_00_pwd HOST=localhost PORT=3306 SECRET_KEY='somearbitrarykey' python3 manage.py test service```


### To run the API tests:

```$ DB_NAME=cleo_db DB_USER=user_00 DB_PASSWORD=user_00_pwd HOST=localhost PORT=3306 SECRET_KEY='somearbitrarykey' python3 manage.py test api```



## Models

- Family (references up to two users representing the parents)
  - id
  - created_at
  - updated_at
  - due_date (optional)
  - birth_date (optional)
  - baby_gender (optional)
  - main_address
  - company (foreign key)
  - guide (foreign key)
    
- User  
  - id
  - created_at
  - updated_at
  - first_name
  - last_name
  - phone_number
  - email
  - address
  - activation_code (used when setting the password the first time, randomly generated when the user is first created)
  - password (encrypted)
  - family (foreign key)  
  
- Guide  
  - id
  - created_at
  - updated_at
  - first_name
  - last_name
  - phone_number
  - email
 
- Company
  - id
  - created_at
  - updated_at
  - name
  - address
  
# API Endpoints

## User
- Get a list of all users [GET]  
  - http://127.0.0.1:5000/api/v1/users/  
- Get a specific user [GET]  
  - http://127.0.0.1:5000/api/v1/users/id/  
- Create a new user [POST]  
  - http://127.0.0.1:5000/api/v1/users/
  - User emails must be unique and return an error if user email is already in use.
- Delete a user [DELETE]
  - http://127.0.0.1:5000/api/v1/users/id/
- Update a user [PUT]  
  - http://127.0.0.1:5000/api/v1/users/id/  
- Activate a user [PUT]  
  - http://127.0.0.1:5000/api/v1/users/id/activate
  - Takes an activation code and new password.
  - Must check activation code before setting password.  Returns error if activation code is invalid.
  - Returns error if user is already activated.

## Company
- Get a list of all companies [GET]  
  - http://127.0.0.1:5000/api/v1/companies/  
- Get a specific company [GET]  
  - http://127.0.0.1:5000/api/v1/companies/id/  
- Create a new company [POST]  
  - http://127.0.0.1:5000/api/v1/companies/
- Delete a company [DELETE]
  - http://127.0.0.1:5000/api/v1/companies/id/
- Update a company [PUT]  
  - http://127.0.0.1:5000/api/v1/companies/id/  

## Family
- Get a list of all families [GET]  
  - http://127.0.0.1:5000/api/v1/families/  
- Get a specific family [GET]  
  - http://127.0.0.1:5000/api/v1/families/id/
- Create a new family [POST]  
  - http://127.0.0.1:5000/api/v1/families/
- Delete a family [DELETE]
  - http://127.0.0.1:5000/api/v1/families/id/
- Update a family [PUT]  
  - http://127.0.0.1:5000/api/v1/families/id/ 

## Guide
- Get a list of all guides [GET]  
  - http://127.0.0.1:5000/api/v1/guides/  
- Get a specific guide [GET]  
  - http://127.0.0.1:5000/api/v1/guides/id/
- Create a new guide [POST]  
  - http://127.0.0.1:5000/api/v1/guides/
- Delete a guide [DELETE]
  - http://127.0.0.1:5000/api/v1/guides/id/
- Update a guide [PUT]  
  - http://127.0.0.1:5000/api/v1/guides/id/ 
