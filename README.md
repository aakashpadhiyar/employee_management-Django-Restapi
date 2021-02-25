# employee_management_rest_api_django
## Example
    
    http http://127.0.0.1:8000/api/v1/employees/ "Authorization: Token <YOUR_TOKEN>"
    http GET http://127.0.0.1:8000/api/v1/employees/3 "Authorization: Token <YOUR_TOKEN>"
    http POST http://127.0.0.1:8000/api/v1/employees/ "Authorization: Token <YOUR_TOKEN>" id="" name="" age=00
    http PUT http://127.0.0.1:8000/api/v1/employees/3 "Authorization: Token <YOUR_TOKEN>" id="" name="" age=00
    http DELETE http://127.0.0.1:8000/api/v1/employees/3 "Authorization: Token <YOUR_TOKEN>"