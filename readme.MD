## Inventory Management System Application For LTU Senior Project
### Mitchell Rusinek



#### "I have neither given nor received unauthorized aid in completing this work, nor have I presented someone else's work as my own."



## How To Setup and Run Application
**Step 1: Download Project**
- You can create a new folder or use the folder called senior_project-main
- Make sure your folder contains the folder with the project itself (inventory_management)
- The project itself is located in the folder called inventory_management
- I used Visual Studio Code to create this application
- Open the folder containing the recipe_book folder in VSCODE

**Step 2: Create Virtual Environment**
- In the terminal of VSCODE, create a virtual enviornemnt
- python -m venv env 

**Step 3: Activate Virtual Environment**
- env/Scripts/activate

**Step 4: Move to Project Folder**
- cd inventory_management

**Step 5: Install Required Package**
- pip install -r requirements.txt

**Step 6: Migrate Database**
- The Database should already be setup and working, but just in case it is not
- python manage.py makemigra
- python manage.py migrate

**Step 7: Run Server**
- python manage.py runserver

**Step 8: Login Credentials**
- The application already has two admin users and some non-admin users created
- You can create as many non-admin users as you would like by registering
- You cannot create anymore admin users, you must use the one below to access the admin panel at /admin
- Admin User:
	- username: admin
	- password: password1

    - username: mrusinek
    - password: Goblue323
- Non-Admin User:
	- username: TestUser1
	- password: Goblue323
