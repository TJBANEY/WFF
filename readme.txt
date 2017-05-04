Cron Setup for cron tasks
30 2 * * * python2.7 $HOME/webapps/djangowebsite/abc-jesus-loves-me/cron_tasks.py 2>&1 >> $HOME/logs/user/cron_tasks.log



Restoring from backup steps
python manage.py flush --no-initial-data
python manage.py loaddata <name of gz file>


This project uses LESS!
- webapp > static > less
- it uses a main file (main.less) that includes multiple individual LESS files
- the main.less file compiles to a single base.css file (you will need to install a compiler for you editor)



Installing LESS compiler on OSX
$ npm install -g less


Relational Database Driven Webapp
