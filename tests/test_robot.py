from config.config import *
from unittest import TestCase
from pyrobot.robot import PyRobot


class PyRobotTest(TestCase):

    def test_creates_instance_of_session(self):
        self.given_a_brokers_auth_data()
        self.when_a_robot_is_created()
        self.the_robot_should_be_a_robot_instance()

    def given_a_brokers_auth_data(self):
        self.client_id = CLIENT_ID
        self.redirect_uri = REDIRECT_URI
        self.credentials_path = CREDENTIALS_PATH

    def when_a_robot_is_created(self):
        self.robot = PyRobot(
            client_id=self.client_id,
            redirect_uri=self.redirect_uri,
            credentials_path=self.credentials_path
        )

    def the_robot_should_be_a_robot_instance(self):
        self.assertIsInstance(self.robot, PyRobot)
