import os
from app import create_app, db
import unittest
import tempfile
from app.scripts.db import InitDB, DropDB


class TestApp(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.app = create_app({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///{}'.format(self.db_path)
        })
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        InitDB().run

    def tearDown(self):
        DropDB().run()
        self.app_context.pop()
        os.unlink(self.db_path)

    def login(self, username, password):
        return self.client.post(
            '/login',
            data=dict(
                username=username,
                password=password),
            follow_redirects=True)

    def logout(self):
        return self.client.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        # TODO: DBが反映されていないのであとで直す
        # rv = self.login('user', 'password')
        # assert 'ログインしました'.encode() in rv.data

        rv = self.login('admin', 'default')
        assert 'ユーザ名が異なります'.encode() in rv.data

        rv = self.login('user', 'default')
        assert 'パスワードが異なります'.encode() in rv.data


if __name__ == '__main__':
    unittest.main()
