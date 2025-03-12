# azure_sql_django

Template for Auzre SQL and restAPI in Django Python

## Set Python environment

For Mac/ Linux
```
python3 -m venv .venv  
source .venv/bin/activate 
```

For Windows
```
python3 -m venv .venv  
.venv\Scripts\activate
```

## Check current Python path

```
where python
```

## Install required dependencies from requirements.txt

```
pip install -r requirements.txt
```

## Generate database migration files
In Django, migrations are a way to propagate changes made to your models (database schema) into the actual database.

When you run:
```
python3 manage.py makemigrations
```

Django will:
1. Scans the models.py file in your Django app.
2. Detects changes (like adding a new model, modifying a field, etc.).
3. Generates a migration file inside the migrations/ directory of your app.
4. The migration file contains instructions (SQL-like operations) that Django will use to update the database.
   
## Apply migrations to the database

```
python3 manage.py migrate
```
## Start Server

```
python3 manage.py runserver
```

## Install Mac odbc driver

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
HOMEBREW_ACCEPT_EULA=Y brew install msodbcsql18 mssql-tools18
```

## Install Window odbc driver
[Download ODBC Driver for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)  

or

```
msiexec /i msodbcsql.msi ADDLOCAL=ALL
```
