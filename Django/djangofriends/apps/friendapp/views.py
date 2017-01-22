from django.shortcuts import render
from .models import Users, Friendships # changed from models import models
# Create your views here.
def index(req):
  # default
  # users = Users.objects.all()
  # 1. last_name is Rodriguez
  # users = Users.objects.all().filter(last_name="Rodriguez")
  # 2. last_name not Rodriguez
  # users = Users.objects.all().exclude(last_name="Rodriguez")
  # change methods in order
  # 3. last_name is Rodriguez OR first_name is Daniel
  # users = Users.objects.all().filter(last_name="Rodriguez") | Users.objects.all().filter(first_name="Daniel")
  # 4. last_name is Rodriguez BUT NOT first_name Madison
  # users = Users.objects.all().filter(last_name="Rodriguez").exclude(first_name="Madison")
  # 5. everyone except Daniel and Michael
  # users = Users.objects.all().exclude(first_name="Daniel").exclude(first_name="Michael")
  # 6. print first_name and last_name of of user with id=1
  # user = Users.objects.get(id=1)
  # need [] for iteration
  # users = [user]
  # print users[0].first_name
  # print users[0].last_name
  # 7. models.Users.objects.get(last_name='Rodriguez')
  # ONLY use GET for SINGLE user, otherwise use FILTER
  # 8. Try models.Users.objects.get(id=10000).
  # DOES NOT EXIST user = Users.objects.get(id=10000)
  # 9. Order the users by first_name.
  # users = Users.objects.all().order_by('first_name')
  # 10. Order the users by reverse last_name.
  # users = Users.objects.all().order_by('-last_name')
  # 11. Print all the Friendship objects in your terminal.
  # print Friendships.objects.all()
  # 12. You know how to get a single friend by the id (#6), now retrieve the Friendships where the User at id 4 is the user in the friendships table! (hint: filter(user = ...))
  # users = Friendships.objects.filter(user=Users.objects.get(id=4))
  # 13. Retrieve the Friendships where the User at id 4 is the friend.
  # users = Friendships.objects.filter(user=Users.objects.get(friendsfriend=4))
  # 14. Retrieve the Friendships where the user isn't user 4, 5, or 6. So exclusive...
  # users = Friendships.objects.exclude(user=Users.objects.get(id=4))
  # .exclude(id=5).exclude(id=6)
  # print vars(users[0])
  # print users.query
  # context = {'users':users}

  # part 2: a Friendships.object.user.first_name should be an actual first name.
  # 1. Starting with Friendships, show all of the users and friends' first and last names on your index.html page. 
  # You can loop through and get the user.first_name directly on the index.html page, maybe something like {{friendship.user.first_name}}
  # friendships = Friendships.objects.all()
  # 2. print all friends' first/last associated with user__first_name='Michael'
  # friendships = Friendships.objects.all().filter(user__first_name='Michael')
  # 3. print all friends' first names who Daniel is not friends with
  # friendships = Friendships.objects.all().exclude(friend__first_name='Daniel').exclude(user__first_name='Daniel')
  

  # 4. Print all of the friends who are friends with both User with the id of 1 and with Users with the last name Hernandez.
  # just sophia lopez!

  # solution:
  # creates set of user_ids
  # user_ids = list(set(Friendships.objects.all().filter(friend__id=1).values_list('user_id', flat=True)))
  # print user_ids
  # filter friendship objects with friend last name of hernandez then filter using user_ids compared with primary key
  # friendships = Friendships.objects.filter(friend__last_name='Hernandez').filter(user__pk__in=user_ids)
  # print friendships
  # print friendships.query

  # these didn't work:
  # friendship2 = Friendships.objects.all().filter(friend__last_name='Hernandez').values('').distinct()
  # friendship3 = Friendships.objects.all().filter(friend__id=1) | Friendships.objects.all().filter(friend__last_name='Hernandez')
  # friendships = friendship1 | friendship2
  # first = Friendships.objects.filter(friend__id=1) 
  # second = Friendships.objects.filter(friend__last_name='Hernandez')
  # friendships = set(first) & set(second)
  # friendships = first | second
  # all_friends = Friendships.objects.all()
  # friendships = friendships.annotate(Count('user_id')).filter(user_id__count__gt=1)
  # first.related.all()
  # .distinct()

  # 5. same as 4, but output to html (already complete)

  # 6. try out these lines:
  # from users join friendships and find friend_id 2 
  # users = Users.objects.filter(usersfriend__friend__id=2)
  # print (users.query)
  # output: SELECT `users`.`id`, `users`.`first_name`, `users`.`last_name`, `users`.`created_at`, `users`.`updated_at` 
          # FROM `users` INNER JOIN `friendships` 
          # ON (`users`.`id` = `friendships`.`user_id`) 
          # WHERE `friendships`.`friend_id` = 2
  # context = {'friendships': friendships, 'users':users}

  # 7. use above query to print out first/last of Users id=2 
  # number2 = Users.objects.get(id=2)
  # print "number2:",number2.first_name
  # users = Users.objects.filter(usersfriend__user__id=2).distinct()
  # print (users.query)
  # for user in users:
  #   print user.first_name
  # context = {'friendships': friendships, 'users':users}

  # 8. 4. but start with Users table: Print all of the friends user_id=1 friends__last_name='Hernandez'.
  # just sophia lopez!
  # creates set of user_ids
  users1 = list(set(Users.objects.all().filter(usersfriend__friend_id=1).values_list('id', flat=True)))
  print users1
  # filter friendship objects with friend last name of hernandez then filter using user_ids compared with primary key
  users2 = list(set(Users.objects.filter(usersfriend__friend__last_name='Hernandez').distinct().values_list('id', flat=True)))
  print users2
  # .filter(id__id__in=user_ids)
  friendships = []
  usersSet = set(users1) & set(users2)
  id1 = usersSet.pop()
  users_1 = Users.objects.get(id=id1)
  users = [users_1]
  context = {'friendships': friendships, 'users':users}

  # print friendships
  return render(req, "friendapp/index.html",context)
