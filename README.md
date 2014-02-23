Quotes
=========

This is a [django](http://www.djangoproject.com) powered quote sharing app.

So far, it lets you post, edit, and delete quotes.


Dependencies
--------------

* [PostgreSQL](http://www.postgresql.org/) (Might work with other databases, but I only work with postgres).

* [ElasticSearch](http://www.elasticsearch.org/)

* Other python libraries listed in the [requirements file](requirements.txt), use [pip](http://www.pip-installer.org) to install those.


Usage
-------

For the application to work, you'll need to set some environment variables first.

These variables are:

1. DATABASE_URL
2. SECRET_KEY
3. POSTMARK_API_KEY
4. SEARCHBOX_URL
5. PROJECT_DIR (Optional)
