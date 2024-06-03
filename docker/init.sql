IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'local_db')
BEGIN
    CREATE DATABASE local_db;
END;
GO