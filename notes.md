1. Video
    - Host -> YouTube - Private Video -> Udacity
      -> Vimeo, Wistia
      -> Self Hosted - nginx
    - Analytics
        - Lot of data
        - 1 user watches for 10 seconds on 100 videos * 10_000
        - Lot of writes
        - Frame by Frame analysis -> 30 FPS -> 120 second -> 3600

2. Members
    - Sign up
    - Login
    - Remember things
    - Email Validation / Confirmation
    - Payments

## AstraDB - Managed NoSQL Cassandra

- Database name
    - Keyspace name
        - Tables
    - Keyspace name A
        - Table A
        - Table b
        - Table c


- Database for Testing
    - keyspace -> Project 1
        - tables (correspond to prod)

## Create user via shell

```python
from app import db
from app.users.models import User

db.get_session()
user.objects.create(email='santosh33@gmail.com', password='abc123')
user.objects.create(email='santosh33@gmail.com', password='abc123s')

```python

q = User.objects.all()

for user in q:
    print(user.email, user.user_id, user.password)
```

## Create user via jupyter notebook

```python
!pwd
# output /home/ssntosh/projects/Python/FastApi/videomembership/fastApiProject

from app import db
from app.users.models import User
from cassandra.cqlengine.management import sync_table

user_a = User.create_user("hello@teamcfc.com", password='abc123')

user_a.password
# Output= '$argon2id$v=19$m=65536,t=3,p=4$fE32NWGmkJt4jY0Wlas3Fg$qaY3fdBdlvX8Af9so1N/6h4QXkKfEnUM1wJtXBLbYn4'

user_a.verify_password('abc123')
# Output = (True, '')

user_a.verify_password('abc123d')
# Output = (False, 'Invalid password')

```