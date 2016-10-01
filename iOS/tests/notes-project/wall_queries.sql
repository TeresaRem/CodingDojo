-- SELECT * FROM users
-- SELECT * FROM messages
-- SELECT * FROM comments

-- SELECT first_name, last_name, messages.created_at, messages.message 
-- FROM users
-- JOIN messages ON users.id = messages.user_id
-- ORDER BY messages.created_at DESC;


--  SELECT first_name, last_name, comments.created_at, comments.comment, message_id
--  FROM users
--  JOIN messages ON users.id = messages.user_id
--  JOIN comments ON messages.id = comments.message_id;

-- how to delete comments
-- DELETE FROM comments WHERE id = :comment_id

-- how to delete comments from message
-- DELETE FROM messages
 -- SELECT comments.id FROM messages
--  JOIN comments ON messages.id = comments.message_id
--  WHERE messages.id = 7;
 -- :message_id;
 -- how to delte the message
 -- DELETE FROM messages
 -- SELECT * FROM messages
--  WHERE messages.id = 7;
 -- :message_id;
 -- 

-- SELECT first_name, last_name, comments.user_id, comments.id, comments.created_at, comments.comment, message_id
-- FROM users
-- JOIN comments ON users.id = comments.user_id
-- JOIN messages ON messages.id = comments.message_id
-- 
-- how to use time to decide if comment or post is deletable
-- SELECT comments.message_id, comments.user_id, comments.created_at, CONCAT_WS(' ', first_name, last_name) AS name, (comments.created_at <= DATE_SUB(NOW(), INTERVAL 30 MINUTE)) AS deletable FROM wall.comments
-- JOIN users ON comments.user_id = users.id
-- JOIN messages ON message_id = messages.id
                                         