## Python Folder README 

### Running API server
To start server ssh into midn.cs.usna.edu then run the command
```
gunicorn --reload --bind=10.1.83.57:5000 wsgi:app
```
Reload means updating the python files will reboot the server (good for during development)

To kill application run 
```
pkill gunicorn
```
