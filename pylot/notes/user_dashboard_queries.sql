-- select * from users
-- select * from messages
-- select * from comments

-- select first_name,last_name,messages.id as message_id,messages.user_id,comments.comment,comments.created_at,comments.user_id,messages.wall_id from users
-- JOIN messages ON users.id=messages.user_id
-- JOIN comments ON messages.id=comments.message_id

-- ALTER TABLE comments CHANGE author_id wall_id INT;
-- select * from users

-- INSERT INTO users (first_name,last_name,email,password,user_level,created_at)
-- VALUES (:first_name,:last_name,:email,:password,:user_level,NOW())

-- INSERT INTO comments (comment, created_at, user_id,wall_id, message_id) values('so great', NOW(), 9, 5, 11)


-- ALTER TABLE comments
-- ADD author_id INT

-- ALTER TABLE table_name
-- DROP COLUMN column_name

-- INSERT INTO messages (message, created_at, user_id, author_id) values('bye', NOW(), 9, 5)

-- SELECT user_id,wall_id,first_name,last_name,messages.created_at,message from messages JOIN users ON users.id = messages.user_id WHERE user_id =5

-- SELECT * FROM users users1
-- LEFT JOIN users users2 on users2.user_level = users.user_level
-- WHERE users.id=1

-- sqlalchemy.exc.IntegrityError
-- IntegrityError: (_mysql_exceptions.IntegrityError) (1452, 'Cannot add or update a child row: a foreign key constraint fails (`dashboard`.`messages`, CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION)') [SQL: u'INSERT INTO messages (message, created_at, user_id, author_id) values(%s, NOW(), %s, %s)'] [parameters: (u'my first message', u'user.id', u'5')]

-- SELECT comments.user_id,messages.wall_id,first_name,last_name,messages.created_at,message from comments 
-- JOIN messages ON messages.id = comments.message_id
-- JOIN users ON users.id = messages.user_id WHERE messages.wall_id =5

-- SELECT first_name,last_name,messages.id as message_id,messages.user_id,comments.comment,comments.created_at,comments.user_id,messages.wall_id,comments.id FROM users
-- JOIN messages ON users.id=messages.user_id
-- JOIN comments ON messages.id=comments.message_id

SELECT first_name,last_name, comments.comment, comments.user_id,comments.created_at,comments.wall_id,comments.message_id FROM users
JOIN comments ON users.id = comments.user_id 
JOIN messages ON messages.id = comments.message_id