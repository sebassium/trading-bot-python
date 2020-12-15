from config.config import *
from unittest import TestCase
from pyrobot.robot import PyRobot


class PyRobotTest(TestCase):

    def setUp(self) -> None:
        self.robot = PyRobot(
            client_id=CLIENT_ID,
            redirect_uri=REDIRECT_URI,
            credentials_path=CREDENTIALS_PATH
        )

    def test_creates_instance_of_session(self):
        self.assertIsInstance(self.robot, PyRobot)

