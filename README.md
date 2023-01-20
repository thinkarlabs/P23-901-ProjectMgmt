# P23-901-ProjectMgmt Development Instructions.

The below are instructions to get started with the development of this project.

1. Download and install Python 3.9/3.10/3.11+ from https://www.python.org/downloads/
2. Download an install git from https://github.com/git-for-windows/git/releases/download/v2.39.1.windows.1/Git-2.39.1-64-bit.exe
3. Create an account at MongoDB Atlas at https://www.mongodb.com/atlas
4. Run the following commands from command prompt in a local folder
    1. Clone this repo by running    
        ```
        git clone https://github.com/thinkarlabs/P23-901-ProjectMgmt.git
        ```
    2. Naviate to the folder
        ```
        cd P23-901-ProjectMgmt
        ```
    3. Create an environment by running
        ```
        py -m venv penv
        ```
    4. Activate the environment by running
        ``` 
        .\penv\Scripts\activate
    5. Install the required packages by running
        ``` 
        pip install -r requirements.txt
        ```
    6. Run the project using the following command
        ``` 
        uvicorn main:app --reload --port 8000
        ```
You should now be able to browse to the application from your browser using http://localhost:8000




