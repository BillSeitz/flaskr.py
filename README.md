Flaskr.py - fork of Flask tutorial to use SqlAlchemy
====================================================

Background pages
 * http://flask.pocoo.org/docs/0.10/tutorial
 * http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/
 * http://postgresapp.com/documentation/configuration-python.html
 * http://webseitz.fluxent.com/wiki/FlaskForWikiEngine
 
Process here
 * I started with the standard Flask tutorial, which uses SQLite without SqlAlchemy
 * Then changed it to use SqlAlchemy talking to SQLite
  * That's when I made the first git commit here
 * Then tweak to have SqlAlchemy talk to postgresql.app on MacOsX
  * only 1 line in database.py to change
  * lots of hassles getting PostgreSQL set up - see last link above for Nov13'2014 notes.

