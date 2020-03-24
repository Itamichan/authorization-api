import os
from collections import namedtuple

import pymysql

User = namedtuple('User', 'id username email password secret')

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'cristina')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'login_test')

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_NAME
        )

    def close_connection(self):
        self.connection.close()

    def get_user_by_id(self, user_id):
        with self.connection.cursor() as cursor:
            sql = 'SELECT username, email, password, secret FROM users WHERE id=%s;'
            cursor.execute(sql, user_id)
            result = cursor.fetchone()
            return User(id=user_id, username=result[0], email=result[1], password=result[2], secret=result[3])

    def get_user_by_name(self, username):
        with self.connection.cursor() as cursor:
            sql = 'SELECT id, email, password, secret FROM users WHERE username=%s;'
            cursor.execute(sql, username)
            result = cursor.fetchone()
            if result is not None:
                return User(id=result[0], username=username, email=result[1], password=result[2], secret=result[3])

    def change_user_secret(self, pk, new_secret):
        with self.connection.cursor() as cursor:
            cursor.execute('UPDATE users set secret=%s WHERE id=%s;', (new_secret, pk))
            self.connection.commit()

    def create_user(self, username, email, password):
        with self.connection.cursor() as cursor:
            cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s);',
                           (username, email, password))
            self.connection.commit()

    def remove_user(self, pk):
        with self.connection.cursor() as cursor:
            cursor.execute('DELETE FROM users WHERE id=%s;', pk)
            self.connection.commit()


if __name__ == '__main__':
    database_instance = Database()

    u1 = database_instance.get_user_by_id(1)
    u2 = database_instance.get_user_by_name('cristina23')
    assert u1 == u2, 'not the same user'

    database_instance.change_user_secret(1, 'boo boo')
    database_instance.create_user('andrew', 'andrew@gmail.com', 'ddggg5884&')
    print(database_instance.get_user_by_name('andrew'))
    database_instance.remove_user(4)
    print(database_instance.get_user_by_name('andrew'))
    database_instance.close_connection()
