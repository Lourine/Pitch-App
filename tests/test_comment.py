import unittest
from app.models import Comment,User, Pitch
from flask_login import current_user
from app import db

class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_Milly = User(username = 'Milly',password = 'potato')
        self.new_comment = Comment(comment = 'Great Pitch',user = self.user_Milly, pitch = self.pitch_Job )


    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
 
    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'Great Pitch')
        self.assertEquals(self.new_comment.user, user_Milly)


    def test_save_c(self):
        self.new_comment.test_save_c()
        self.assertTrue(len(Comment.query.all())>0)


    def test_get_comments(self):

        self.new_comment.save_c()
        got_comments = Comment.get_comments("")
        self.assertTrue(len(got_comments) == 1)
