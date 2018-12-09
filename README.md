# cleo

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
  
