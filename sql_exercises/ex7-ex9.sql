-- Удалить запись из таблицы News


DELETE FROM News
WHERE id = 1;

-- Удалить 100 последних записей из таблицы news

DELETE FROM News
WHERE id IN (SELECT id FROM News ORDER BY id DESC LIMIT 100);


-- Удалить 1 запись из таблицы Categories


DELETE FROM Categories
WHERE id = 1;
