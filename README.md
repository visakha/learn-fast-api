# Notes: learn-fast-api
Notes when learning about fastApi - a Python web framework
Along the way I am building a project : 
    
    ### Customer Data Reconciliation ###

## Functional Goals
Customer Data Reconciliation is about gathering Customer data from contributing sources and then perform 
a reconciliation based on parameters like : same SSN and/or same fullName + Birthdate etc
Once reconciled then publish the information to Kafka and also publish derived events

## representation of  Customer Data
For the sake of simplicity and efficiency, I am modeling the data as flat dictionary
it will consist of

* Name: First Name, Middle Name, Last Name, preferred name, prev name, maiden Name
* Identification: SSN, Birthdate, alt id 1, alt id 2 
* Phone : ph 1, ph 2, ph 3
* eMail:  primary eMail, secondary eMail
* Address : address 1, address 2

## Technical Goals

    - API driven batch data import and export
    - API driven real time sevices
    - Pub-Sub modeling the application logic : Redis and Kafka
    - Derived events publish via KSQL
    




# Credits
There are many resources on the internet that are not listed here - ack and credit to them


## links 

* https://www.starlette.io/routing/
* https://fastapi.tiangolo.com/advanced/sub-applications/
* loading python modules dyncamically https://www.youtube.com/watch?v=cbot48lckOs
* redis on windows 10 https://developer.redis.com/create/windows/
* https://www.w3schools.com/bootstrap5/

# Optional links

fonts mono : https://www.jetbrains.com/lp/mono/#how-to-install

WSL2 : include those fonts in the file
    
    C:\Users\vamsi\AppData\Local\Packages\Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe\LocalState\settings.json
    "defaults": {
        // Put settings here that you want to apply to all profiles.
        "fontFace": "JetBrains Mono",
        "fontSize": 12
      },





# Table of contents

## chapter 01 - Fast API setup
* set up working env and simple helloworld
[setup tools and env](docs/setup-tools-env.md)

## chapter 02 - Web UI
* set up jinja2 and bootsrap 2
[first simple bootstrap home page](docs/add-template-jinja.md)

## chapter 03 - Redis infrastructure
* set up redis on WSl2(Ubuntu)
* ssh into it from windows terminal
* pytest connectivity

[prepare redis on windows](docs/prepare-redis-windows10.md)


## chapter 04 - About the project - Customer Data Reconciliation
* About the goals of this project
* ssh into it from windows terminal
* pytest connectivity

[prepare redis on windows](docs/prepare-redis-windows10.md)









