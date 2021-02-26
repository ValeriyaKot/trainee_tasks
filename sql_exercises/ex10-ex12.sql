--Выбрать все записи из таблицы News, у которых IsPublished верно


SELECT *
FROM News
WHERE is_published IS True;


--Выбрать все записи из таблицы News с включением имени соответствующей категории


SELECT *
FROM News
JOIN Categories
	ON News.category_id = Categories.id;


-- Выбрать все записи из таблицы News с включением соответствующей категории, у который IsPublished верно


SELECT *
FROM News
JOIN Categories
	ON News.category_id = Categories.id
WHERE is_published IS True;
