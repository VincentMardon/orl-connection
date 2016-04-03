# ORL Connection

This software is on developpement for now...

## Installation

*NOTE: Requires 
[Python 3.5](https://www.python.org/downloads/release/python-350/),
[virtualenv](http://virtualenv.readthedocs.org/en/latest/),
[Node.js 5](https://nodejs.org/en/download/),
[Ruby 2.2.3](https://www.ruby-lang.org/en/documentation/installation/)

* For this repository
* `$ git clone git@github.com:<your username>/orl-connection.git`
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

## About Compass watch

It is possible you encoutered an issue with le command line `compass watch`.
To fix this try this:

* `$ compass watch --config static/config.rb --poll`

If the watcher crash, try this:

* `$ gem update --system`

Normally, this command line resolve this possible issue

## License

This software is under the GPL-3.0 license.
See LICENSE file for more information.