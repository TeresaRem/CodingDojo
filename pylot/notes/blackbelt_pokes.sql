-- select * from pokes

-- DELETE FROM users WHERE id < 1000;

-- SELECT user_id,COUNT(id) FROM pokes
-- WHERE user_id = 1

-- SELECT users.id as id_poked,users.alias as user_poked,u2.id as id_poker,u2.alias as poker, COUNT(users.id) as pokes FROM users
-- JOIN pokes ON users.id=pokes.user_id
-- JOIN users u2 ON pokes.poker_id = u2.id
-- WHERE users.id = 1
-- GROUP BY id_poker
-- ORDER BY COUNT(users.id) DESC

-- data = {}
-- ,count(users.id) 
-- 
-- SELECT users.name,users.alias,users.email, COUNT(pokes.user_id) as pokes FROM users
-- LEFT JOIN pokes ON users.id=pokes.user_id
-- WHERE users.id <> 1
-- GROUP BY users.id

-- INSERT INTO pokes (user_id,poker_id, created_at) VALUES (2,1, NOW())