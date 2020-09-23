## PROJECT  NAME 
 - PITCH-eat

 ## project by Jackson kitsao see live link [view it live](https://pitch-eat.herokuapp.com/)

### Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* PostgresSQL was used in this project as the database client, however fell free to use whichever cliet you prefer (this documentaion is based on Postgres)
    * To download postgres, follow this [link](https://www.postgresql.org/download/)

### Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/jkitsao/flask-user-story.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv virtual`**
    * **`source virtual/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**

* **Step 5** : If you are using postgresql, run the server on a separate terminal tab/window using **postgres**
    * Then on another terminal tab/window, run the command **psql** to enter the postgresql shell
    * Create a database called **'test'** by typing the command  **`CREATE DATABASE test;`**
    * Set a password for your database by running this command **`ALTER USER <username> WITH PASSWORD "<new_password>";`**
    * Now go back to the project directory, in the **config.py** file, set your **SQLALCHEMY_DATABASE_URI** in the Config class following the following format:
    **`SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://<username>:<password>@localhost/test"`**
    * Side note: you will notice that on the TestConfig class, the database uri is linked to a test database, you can create one for testing purposes, otherwise, ignore.
* **Step 6** : Run the following command to upgrade your database to current schema:
```
python manage.py db upgrade
```
* **Step 7** : On your terminal, run the following command, **`chmod +x start.sh`** to make the shell file from **step 5** executable
    * You can now launch the application locally by running the command **`./start.sh`** 
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:5000/**.
