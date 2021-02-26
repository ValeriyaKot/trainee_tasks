-- Отсортировать записи по имени категории в порядке возрастания и по PublishedDate в порядке убывания


SELECT *
FROM News
FULL JOIN Categories
	ON News.category_id = Categories.id 
ORDER BY name ASC, published_date DESC;


-- Вывести количество записей в таблице News для каждой записи в таблице Categories


SELECT name, COUNT(*) AS quantity_topics
FROM News
FULL JOIN Categories
	ON News.category_id = Categories.id
GROUP BY name;