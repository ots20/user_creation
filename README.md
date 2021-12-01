# user_creation
Script to help user creation in a quick way.<br />
You would be able to create up to 5 users, this can be changed but I consider 5 users is enough. <br />
**Password is set as: test123** <br />

You can change some parameters:
 - Environment: in the `setUp` method you set the environments where users will be created
 - the email manually, in the line 36 of the method `test_create_user`. It contains a random number generator whose digits can be increased. I suggest to change the email and nick before running it. <br />

It prints the user's name(s) if the request was successfully performed, otherwise, it would display the error code. <br />

## Setup
1. open terminal <br />
2. run `git clone https://github.com/ots20/user_creation.git` to clone repository<br />
3. run cd `omar_api_user_tests` to move to local repository folder<br />
4. run `pipenv install` to set up all necessary dependencies from Pipfile.lock<br />
5. run `pipenv shell` to be able to use all pipenv dependencies from terminal<br />
6. rename the file `.env.example` into `.env` and add the URL and password of the staging environment you need

## Execution
to run the script:<br />
`python3 -m unittest tests/api_test.py`
