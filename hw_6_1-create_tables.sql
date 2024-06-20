CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	fullname VARCHAR(100),
	email VARCHAR(100) UNIQUE
);

CREATE TABLE status (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE
);

INSERT INTO status (name)
VALUES ('new'),
('in progress'),
('completed');

CREATE TABLE tasks (
	id SERIAL PRIMARY KEY,
	title VARCHAR(100),
	description TEXT,
	status_id INT,
	user_id INT,
	FOREIGN KEY (status_id) REFERENCES status (id)
		ON DELETE SET NULL,
	FOREIGN KEY (user_id) REFERENCES users (id)
		ON DELETE CASCADE
);