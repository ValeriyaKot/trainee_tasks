-- Create table News

CREATE TABLE News(
	id SERIAL NOT NULL PRIMARY KEY,
	title TEXT NOT NULL,
	text TEXT,
	is_published BOOLEAN NOT NULL,
	published_date DATE NOT NULL,
	category_id INTEGER NOT NULL,
	FOREIGN KEY (category_id) REFERENCES Categories(id)
);


-- Create table Categories


CREATE TABLE Categories(
	id SERIAL NOT NULL PRIMARY KEY,
	name TEXT NOT NULL
);
