-- Выбрать все записи из таблицы Categories, у которых нет соответствия в таблице News


SELECT *
FROM Categories
LEFT JOIN News
	ON Categories.id = News.category_id 
WHERE News.category_id IS NULL;
