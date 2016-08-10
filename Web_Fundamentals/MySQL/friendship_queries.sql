
SELECT users.first_name,users.last_name,
user2.first_name as friend_first_name,user2.last_name as friend_last_name
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id 
LEFT JOIN users as user2 ON user2.id = friendships.friend_id 
ORDER BY friend_last_name DESC

/* use this to append friendships table
SELECT id,user_id,friend_id FROM friendships
*/

