-- Добавить 4 записи в таблицу Categories


INSERT INTO Categories(name)
VALUES ('Adventure'),
		('Science'),
		('News'),
		('Jokes');


-- Добавить записи в таблицу News


INSERT INTO News(title, text, is_published, published_date, category_id)
VALUES ('Flowers', 'Lectus leo dui tempus in mollis lectu', True, '2018-02-03', 1),
        ('Birds', 'Lectus leo dui tempus in mollis lectu', True, '2018-05-03', 2),
		('Blue glass', 'Morbi vitae interdum morbi mauris accumsan ', True, '2014-05-03', 3),
		('Sky', 'Nisi sed efficitur in habitasse nisi dictumst', True, '2014-03-03', 4),
		('18.09', 'Augue hac arcu ultricies', False, '2014-03-03', 5);


--Добавить 500 записей в таблицу News


INSERT INTO News(title, text, is_published, published_date, category_id)
SELECT title, text, is_published, published_date, category_id
FROM News;
