#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models import storage
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        cmd = HBNBCommand()
        self.assertTrue(cmd.onecmd("quit"))
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        cmd = HBNBCommand()
        self.assertTrue(cmd.onecmd("EOF"))
        self.assertEqual(mock_stdout.getvalue(), '')

    def test_emptyline(self):
        cmd = HBNBCommand()
        self.assertIsNone(cmd.onecmd("\n"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        cmd = HBNBCommand()
        cmd.onecmd("create BaseModel")
        self.assertTrue(mock_stdout.getvalue().strip())
