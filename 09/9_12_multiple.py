from user2 import User
from admin2 import Admin

user1 = User('denver', 'kong', 35, 'male')
print(user1.describe_user())

a_account = Admin('a-dkong', 'kong', 35, 'male')
print(a_account.show_privileges())