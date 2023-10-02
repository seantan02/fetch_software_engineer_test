This application is an application that is ready to receive API calls and perform certain actions.

*To run this application in your local machine, please follow steps below:*

1. Pull this entire folder into your machine
2. Install python in your machine if not already installed via https://www.python.org/downloads/
3. Open your terminal and make sure you go to the folder you downloaded by using "cd PATH/TO/FOLDER"
4. Then type "source venv/bin/activate" to enter your virtual environment
5. Then type in "pip3 install -r requirements.txt"
6. Now type in "python3 main.py" to run the server
7. Now open another terminal and follow these steps below to play with the application:
    • To call api action on /add endpoint, type "python3 add_tester.py" and enter.
    • To call api action on /spend endpoint, type "python3 spend_tester.py" and enter.
    • To call api action on /balance endpoint, type "python3 balance_tester.py" and enter.
    • To restart all the points for user, type "python3 restart.py" and enter!

You should see messages printed out on the terminal! Interestingly, if you go to http://localhost:8000/balance, you can see the user's points too!

For real world API application, please DO NOT implement the .json file data storage feature shown here because it is never a good idea! Use a relational database like PostgreSQL instead because it posses crucial feature like making sure 1 query is being execute at a time to prevent complications when modifying data!

Also, please remember to always test your application locally for security before going live!