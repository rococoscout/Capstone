# Chadbot

The Chatbot system is a chatbot interface that responds to inquiries on the Computer Science department, the Naval Academy, and basic dialogue.

## Usage

The Chadbot is very easy to begin interacting with. The interface is a simple webpage, so when deployed simply visit http://midn.cs.usna.edu/~m213990/cap/Capstone/ in order to begin asking Chadbot questions. 

To access the administrative sight visit http://midn.cs.usna.edu/~m213990/cap/Capstone/Admin.php and sign in with your normal USNA credentials. 

## Installation

The following outlines the prerequisites and steps in order to deploy Chadbot yourself on the midn.cs.usna.edu server. 

The package manager [pip](https://pip.pypa.io/en/stable/) will be required to install all the dependent python packages required to run Chadbot. 

## Database

Files:
- [PYTHON/dbhelper.py][dbhelper]

Python package [pymysql](https://pypi.org/project/PyMySQL/) is used to manage access to the MySQL database. Install:

```bash
$ python3 -m pip install PyMySQL
```

The class **DBHelper** from [dbhelper.py][dbhelper] allows for easy access to the database. The **DBHelper** object specifies the following that facilate access. 

```python
def __init__(self):
        self.host = "midn.cs.usna.edu"
        self.user = "m215394"
        self.password = "greg1018"
        self.db = "capstone_chatbot"
```

To utilize your own MySQL account simply email the USNA MySQL manager, currently [Mr. Jeff Kenney](kenney@usna.edu), requesting access to the schema labeled __capstone_chatbot__. Then replace **self.user** and **self.password** with your own credentials. 

Accessing and editing the database itself can be done either using a bash shell or **MySQL Workbench**. Please see [MySQL Documentation](https://dev.mysql.com/doc/) for more information. 

[dbhelper]: PYTHON/dbhelper.py

## API Setup and Deployment

Files:
- [PYTHON/api.py][api]
- [PYTHON/wsgi.py][wsgi]
- [PYTHON/rule.py][rule]

Chadbot API facilitates connection between the website, the database, and the machine learning required to get answers. Chadbot utilizes the web framework [Flask](https://flask.palletsprojects.com/en/1.1.x/) and the WSGI HTTP Server for UNIX [gunicorn](https://gunicorn.org/) to host the webstie on the **midn.cs.usna.edu** server. Install:
 
```bash
pip install flask gunicorn
```

Also, Flask-CORS is requied. Flask-CORS is a Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.

```bash
pip install -U flask-cors
```

In order to deploy the server, you must run the [wsgi file][wsgi] with gunicorn:
```bash
gunicorn --bind=10.1.83.57:5000 wsgi:app
```

This bash command runs the flask application on the IP address **10.1.83.57** (midn.cs.usna.edu) on port **5000**. These values are important because the webpages that request information will need to use these values specifically to return information. 

To better facilitate managing and controlling rules the helper class **Rule** in [rule.py][rule] was created. This allows for easy calls to retrieve and alter entries in the databse. 

[api]: PYTHON/api.py
[wsgi]: PYTHON/wsgi.py
[rule]: PYTHON.rule.py

## Responses and Language Filtering 

Files:
- [PYTHON/response.py][response]
- [PYTHON/vecResponse.py][vec]
- [PYTHON/regex.py][regex]
- [PYTHON/genericResponse.py][generic]
- [PYTHON/rule.py][rule]

The **getAnswer()** method from [response.py][response] outputs the answer the Chadbot will respond to given a user question. The other classes and functions are helpers that assist in the decoding, vector mapping, and storing of information in order for the system to properly learn. 

To perform the word to vector operations an api must be downloaded using the package called [gensim](https://pypi.org/project/gensim/). Install:

```bash
pip install --upgrade gensim
```


[regex]: PYTHON/regex.py
[generic]: PYTHON/genericResponse.py
[response]: PYTHON/response.py
[vec]: PYTHON/vecResponse.py

## Webpages 

Files:
- 

