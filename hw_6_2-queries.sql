--Отримати всі завдання певного користувача.
SELECT * FROM tasks WHERE user_id = 15; -- might return 0 tasks; might have to try a few times

--Вибрати завдання за певним статусом.
SELECT * FROM tasks WHERE status_id = 2;

--Оновити статус конкретного завдання.
UPDATE tasks SET status_id = 1 WHERE id = 1;

--Отримати список користувачів, які не мають жодного завдання.
SELECT * FROM users
WHERE id NOT IN (
	SELECT user_id FROM tasks
);

--Додати нове завдання для конкретного користувача. 
INSERT INTO tasks (title, description, status_id, user_id)
VALUES (
	'Duck got shot',
	'This is a test task. Some more description here',
	1,
	7
);

--Отримати всі завдання, які ще не завершено.
SELECT * FROM tasks WHERE status_id != 3;

--Видалити конкретне завдання.
DELETE FROM tasks WHERE id = 101; -- delete the newly added task

--Знайти користувачів з певною електронною поштою.
SELECT * FROM users WHERE email LIKE '%ll%';

--Оновити ім'я користувача.
UPDATE users SET fullname = 'Ryan Hill' WHERE id = 2;

--Отримати кількість завдань для кожного статусу.
SELECT COUNT(status_id) as statuses
FROM tasks
GROUP BY status_id ORDER BY status_id;

--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
SELECT t.user_id, t.title, t.description, u.email, u.fullname as users
FROM tasks AS t
JOIN users AS u ON u.id = t.user_id
WHERE u.email LIKE '%example.net'
ORDER BY user_id;

--Отримати список завдань, що не мають опису.
SELECT * FROM tasks WHERE description = '' OR description IS NULL;

--Вибрати користувачів та їхні завдання, які є у статусі in progress
SELECT t.user_id, u.fullname, t.title, t.description, t.status_id as status
FROM tasks AS t
INNER JOIN users AS u ON u.id = t.user_id 
WHERE t.status_id = 2
ORDER BY user_id;

--Отримати користувачів та кількість їхніх завдань.
SELECT t.user_id, u.fullname, COUNT(u.fullname) as num_tasks
FROM tasks AS t
JOIN users AS u ON u.id = t.user_id 
WHERE t.status_id = 2
GROUP BY t.user_id, u.fullname
ORDER BY t.user_id;