--Вывести количество записей в таблице News, у которых IsPublished верно,
-- для каждой записи в таблице Categories


SELECT name, is_published, COUNT(*) AS quantity_is_published_true
FROM News
FULL JOIN Categories
	ON News.category_id = Categories.id
GROUP BY name, is_published
HAVING is_published IS True;
