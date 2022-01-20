# how-to :: DEPLOY A FLASK APP WITH APACHE
---
## Overview
Guide to creating an flask app using an Apache2 webserver.

### Estimated Time Cost: 15 min

### Prerequisites:
Apache installed.

### How To Deploy a Flask Application on an Ubuntu VPS

1. Install and Enable mod_wsgi
  ```
  sudo apt-get install libapache2-mod-wsgi python-dev
  sudo a2enmod wsgi
  ```

2. Creating a Flask App
  ```
  cd /var/www
  sudo mkdir <FlaskApp>
  cd <FlaskApp>
  sudo mkdir <FlaskApp>
  cd <FlaskApp>
  sudo mkdir static templates
  sudo nano __init__.py
  ```

  Once you create your python file, create a flask app. Here is a basic code snippet:
  ```
  from flask import Flask
  app = Flask(__name__)
  @app.route("/")
  def hello():
      return "Hello world!"
  if __name__ == "__main__":
      app.run()
  ```
  Save and close the file.

3. Install Flask
  ```
  sudo apt-get install python3-pip
  sudo pip install virtualenv
  sudo virtualenv <venv>
  source <venv>/bin/activate
  sudo pip3 install Flask
  sudo python3 __init__.py
  ```

4. Configure and Enable a New Virtual Host
  ```
  sudo nano /etc/apache2/sites-available/<FlaskApp>
  sudo nano /etc/apache2/sites-available/<FlaskApp>.conf
  ```

  Add this into your config file. Be sure to change the ServerName to your domain or cloud server's IP address:
  ```
  <VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
  ```

  Enable the virtual host:
  ```
  sudo a2ensite FlaskApp
  ```

5. Create the .wsgi File
  ```
  cd /var/www/<FlaskApp>
  sudo nano <flaskapp>.wsgi
  ```

  Add this into your wsgi file:
  ```
  #!/usr/bin/python
  import sys
  import logging
  logging.basicConfig(stream=sys.stderr)
  sys.path.insert(0,"/var/www/FlaskApp/")

  from FlaskApp import app as application
  application.secret_key = 'Add your secret key'
  ```

6. Install python3
  ```
  sudo apt-get install libapache2-mod-wsgi-py3 python-dev
  ```

6. Restart Apache
  ```
  sudo service apache2 restart
  ```

Now you can add your ServerName into your browser and run it!

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
---

Accurate as of (last update): 2022-01-19

#### Contributors:  
Ella Krechmer, pd1  
Ivan Lam, pd1  
