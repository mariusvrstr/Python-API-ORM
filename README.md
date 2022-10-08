# Python-API-ORM
Python based FastAPI and SQLAlchemy example

## Design Patterns
- [X] Repository Pattern - Abstract database access
- [X] Builder Pattern - Generate sample test with fluent objects
- [X] Unit of Work - Ensure there are no partial database changes all in or all out

## Setup
1. Run setup.ps1 powershell script
2. Install [TablePlus](https://tableplus.com/) for SQL Lite -OR- [SSMS](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms) for SQL Server

## Known Limitations
- Even though you share the Session object between repositories only RAW SQL return uncomitted data in your current session. Severe limitation when you need to do multiple dependant steps in a single action [Read More](https://stackoverflow.com/questions/56640429/using-session-query-to-read-uncommitted-data-in-sqlalchemy)

## ORM Backlog (SQLAlchemy)
- [X] Code first db generation
- [X] SQL Lite Database Example
- [ ] SQL Server Database Example
- [ ] GUID Id's
- [X] Unit of Work (Transactions + Repository Session sharing)
- [X] Foreign Keys
- [X] Crud interactions
- [X] Get access to new DB ID's before transaction is committed
- [ ] Code Migrations ([Alembic Offline Migrations](https://alembic.sqlalchemy.org/en/latest/))

## API Backlog (FastAPI)
- [ ] Multiple routers
- [ ] Validation
- [ ] Authentication (API Key)
- [ ] Parameters (Query, path & body)
- [ ] Error handling
- [ ] Async Await
- [ ] Swagger documentation
- [ ] Config / Variable Replacement
