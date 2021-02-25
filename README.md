# employee_management_rest_api_django
## Example
    
    http http://127.0.0.1:8000/api/v1/employees/ "Authorization: Token <YOUR_TOKEN>"
    http GET http://127.0.0.1:8000/api/v1/employees/3 "Authorization: Token <YOUR_TOKEN>"
    http POST http://127.0.0.1:8000/api/v1/employees/ "Authorization: Token <YOUR_TOKEN>" id="" name="" age=00
    http PUT http://127.0.0.1:8000/api/v1/employees/3 "Authorization: Token <YOUR_TOKEN>" id="" name="" age=00
    http DELETE http://127.0.0.1:8000/api/v1/employees/3 "Authorization: Token <YOUR_TOKEN>"


* Login and Tokens

To get a token first we have to login

	http http://127.0.0.1:8000/rest-auth/login/ username="admin" password="root1234"


after that, we get the token

    {
        "key": "2d500db1e51153318e300860064e52c061e72016"
    }


#### ALL request must be authenticated with a valid token, otherwise they will be invalid

We can create new users. (password1 and password2 must be equal)

    http POST http://127.0.0.1:8000/rest-auth/registration/ username="USERNAME" password1="PASSWORD" password2="PASSWORD"


And we can logout, the token must be your actual token

    http POST http://127.0.0.1:8000/rest-auth/logout/ "Authorization: Token <YOUR_TOKEN>" 




