-- Create test database
CREATE DATABASE test_db;

-- Create test user
CREATE USER testuser WITH ENCRYPTED PASSWORD 'testpass';

-- Grant privileges to testuser on test_db
GRANT ALL PRIVILEGES ON DATABASE test_db TO testuser;
