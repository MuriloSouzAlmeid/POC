CREATE DATABASE POC_Database;

USE POC_Database;

CREATE TABLE ncm_entries(
	id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
	[user] VARCHAR(MAX) NOT NULL,
	ipi VARCHAR(MAX),
	ncm VARCHAR(MAX) NOT NULL,
	[description] TEXT NOT NULL,
	created_at DATETIME2(3) NOT NULL
);

INSERT INTO ncm_entries (id, [user], ipi, ncm, description, created_at) VALUES (NEWID(), 'student', ' ', '1', 'ANIMAIS VIVOS', 1747702650.851647)

SELECT * FROM ncm_entries;
DELETE FROM ncm_entries