# Engage Legislation
A project to engage citizens with local legislation based on their interests 
through email subscription.

# Technologies Used
We built this web app using Flask, with a MongoDB backend. The database service
is provided by mLab using Amazon AWS Sandbox. We recieve our data from the
`openstates` API. 

# To Do
- [ ] Polish the front end
- [ ] Add more routes
- [ ] unittest the models
- [ ] Set up integration testing
- [ ] Deploy for production

# Set Up
This app is powered by flask on the backend. We will also use `virtualenv` for
development.

0. clone this repository.
```
git clone https://github.com/salekinsirajus/Engage-Legislation.git
```
1. Install `virtualenv`, documentation [here](http://flask.pocoo.org/docs/0.12/installation/)
    1. `sudo pip install virtualenv`
    2. `cd` into `Engage-Legistlation` if you haven't already
    3. Create a new virtual environment for this project
    ```
    virtualenv venv
    ``` 
    4. Activate the virtual environment
    ```
    . venv/bin/activate
    ``` 
    If you are a windows user, do this instead:
    ```
    venv\Scripts\activate.bat
    ```
    5. To deactivate the virtual environment (when you are done working with it)
    ```
    deactivate
    ```
2. cd to `Engage-Legislation` directory
3. Run the `requirements.txt` to install rest of the libraries
```
pip3 install -r requirements.txt
```
Note: if your default python version is >3.0, you don't need to use `pip3`. Use
`pip` instead

4. Let the terminal know where the app is
```
export FLASK_APP=run.py
```

5. Run this app by running the following command
```
flask run
``` 

6. Open a browser window and go to this address
```
http://127.0.0.1:5000/
```

