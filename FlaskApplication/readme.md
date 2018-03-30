1. Clone the application `git clone git@github.com:pyVarad/cautious-octo-journey.git`.
2. cd cautious-octo-journey
3. cd FlaskApplication
4. Install the dependent modules using the command `pip install -r requirements.txt`
5. export FLASK_APP="run.py"
6. Create the database migration files `flask db init`.
7. Perform database migration `flask migrate`.
8. Run the command `flask shell`.
    ``` Python
        Python 2.7.10 (default, Jul 15 2017, 17:16:57)
        [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
        App: app
        Instance: /Users/shriya/Desktop/Github/Testing/cautious-octo-journey/FlaskApplication/instance
        >>> from app import db
        >>> db.create_all()
        >>> exit()
    ```
9. Perform `flask run --reload`.
10. Open the web browser "http://localhost:5000"