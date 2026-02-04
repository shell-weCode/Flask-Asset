This is my Asset
This asset is build with Flask framework and Python 3.13.5

It's a simple REST API with 4 Endpoints using 4 HTTP methods: GET, POST, PUT, DELETE
Each endpoint has it own test that will run using pytest, each test validates that every
endpoint response has a succesful response returning a status code == 200

In order to being able to install and run the project, Python 3.13+ must be installed

First Step:
- Give execute permissions to run_asset file:
  ´´´chmod +x run_asset.sh´´´

Second Step:
- Run the script:
        ./run_asset.sh
    
This script will execute the whole dependencies installation process. (Process explained below)
  - Verify if python 3.13+ is installed
  - Creates a virtual environment
  - Installs dependencies to create a .whl file and then creates the file
  - Intalls the wheel
  - Runs the tests
