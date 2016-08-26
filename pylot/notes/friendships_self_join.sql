-- SELECT users.first_name,users.last_name,u2.first_name,u2.last_name FROM users
-- LEFT JOIN friendships ON users.id=friendships.user_id
-- LEFT JOIN users u2 ON friendships.friend_id = u2.id

/* 

for users, get their friendships
from their friendships, get their friends' names

for employees, get their managers
from their managers, get their manager's names

*/

-- SELECT users.first_name,users.last_name,u2.first_name,u2.last_name FROM users
-- JOIN friendships ON users.id=friendships.user_id
-- JOIN users u2 ON friendships.friend_id = u2.id

SELECT users.first_name, users.last_name, f.first_name, f.last_name

FROM
users JOIN friendships JOIN
	(SELECT first_name, last_name, users.id 
    FROM users JOIN 
         friendships ON (users.id = friendships.friend_id)
	) f ON (friendships.id = f.id)
WHERE 
users.first_name != f.first_name
    