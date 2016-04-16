# ORL Connection

*This software is still under developpement...*

## Table of contents

1. [Installation](#installation)
2. [About Compass watch](#about-compass-watch)
3. [License](#license)

### Installation

**NOTE**: Requires 
[Python 3.5](https://www.python.org/downloads/release/python-350/ "Python 3.5 download"),
[virtualenv 15.0.0](http://virtualenv.readthedocs.org/en/latest/ "virtualenv installation"),
[Node.js 5.0.0](https://nodejs.org/en/ "Node.js installation"),
[Ruby 2.2.3](https://www.ruby-lang.org/en/documentation/installation/ "Ruby installation")

Fork this repository:

* `$ git clone https://github.com/VincentMardon/orl-connection.git [repository name]`
* `$ virtualenv path/to/project/<env_project_name>`
* `$ source <env_project_name>/bin/activate`
* `$ cd orl-connection`
* `$ pip install -r requirements.txt`
* `$ npm install -g bower`
* `$ npm install`
* `$ bower install`
* `$ bundle install`
* `$ gulp`
* `$ python manage.py livereload`
* `$ python manage.py runserver`
* `$ compass watch --config static/config.rb` 

### About Compass watch

It is possible that you encouter a bug with the command line `compass watch`.
To fix that, try this:

* `$ compass watch --config static/config.rb --poll`

If the watcher crashes, try this:

* `$ gem update --system`

Normally, this command line resolves this possible issue.

### License

This software is under the *GPL-3.0* license.
See LICENSE file for more information.