-- a script that creates the table unique_id on your MySQL server.
-- table unique_id.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT default 1 UNIQUE,
    name VARCHAR(256)
);
