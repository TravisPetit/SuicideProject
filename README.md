# SuicideProject

# Reproduction: step by step
On Ubutu-server:

1. Clone the repo.
2. Switch to the root user: `sudo su`.
3. Update package list: `apt-get update`.
4. Install postgres: `apt install postgresql`.
5. Install postGIS: `apt install postgis`.
6. Check your current postgres version: `sudo -i -u postgres` and then `psql --version`. You should get something like:
*psql (PostgreSQL) x.y*
7. Switch back to the root user by pressing control d and install the fitting postgresql developer server package: `postgresql-server-dev-x.y`, where x.y is your postgres version.

8. Install psycopg2: `pip2 install psycopg2`. If you get the error `Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-vkoXyM/psycopg2/ ` then chances are that your setuptools are out of date, running `pip install --upgrade setuptools` should fix this.

9. Switch to the postgres user: `sudo -i -u postgres`. 
10. Set its password to *123* by running: `psql` and then `\password`.

If you get the error message:

`psql: could not connect to server: No such file or directory                                                                    Is the server running locally and accepting                                                                             connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5433"?` 

Then running `psql -h localhost` instead of psql should do the trick.

11. Cd to the gelt folder: `cd /path/to/SuicideProject/gdelt`.

12. Download the GDELT csv files: `python3 download.py`. This will download eighty nine thousand zipped csv files and unzip them. Expect this to take at least a couple of hours.

13. Cd to the src folder: `cd /path/to/SuicideProject/sql_scripts/src`.

14. Alas, you may begin populating the database with: `python2 db.py -all`. Make sure to run this as the postgres user! Expect this to take a couple of days.
