--Вывести количество записей в таблице News, у которых IsPublished верно и нет


SELECT COUNT(is_published) AS quantity_is_published_false
FROM News
GROUP BY is_published
HAVING is_published IS False;


SELECT Count(is_published) AS quantity_is_published_true
FROM News
GROUP BY is_published
HAVING is_published IS True;
