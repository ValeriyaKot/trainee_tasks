-- Обновить значение IsPublished в первых 10 записях таблицы News


UPDATE News
SET is_published = True
WHERE id IN (SELECT id FROM News ORDER BY id ASC LIMIT 10);


-- Обновить название одной из записей в таблице Categories


UPDATE Categories
SET name = 'Romance'
WHERE id = 2;
