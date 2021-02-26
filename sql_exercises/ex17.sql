-- Вывести количество записей в таблице News, для каждой записи в таблице Categories,
-- у  которых IsPublished верно и нет. Отсортировать записи по имени категории.

SELECT name, is_published, COUNT(*) AS quantity_is_published_false
FROM News
FULL JOIN Categories
	ON News.category_id = Categories.id
GROUP BY name, is_published
HAVING is_published IS False
ORDER BY name ASC;


SELECT name, is_published, COUNT(*) AS quantity_is_published_true
FROM News
FULL JOIN Categories
	ON News.category_id = Categories.id
GROUP BY name, is_published
HAVING is_published IS True
ORDER BY name ASC;