#import datetime
#
#from django.utils import timezone
#
#from django.test import TestCase
##from django.test import Client
##from django.test.utils import setup_test_environment
#from django.core.urlresolvers import reverse
#
#from polls.models import Poll
#
#
## Utility functions
#
#def create_poll(question, days):
#    time = timezone.now() + datetime.timedelta(days=days)
#    return Poll.objects.create(question=question, pub_date=time)
#
#
#
## Create your tests here.
#
#class PollMethodTests(TestCase):
#
#    def test_was_published_recently_with_future_question(self):
#        """
#        was_published_recently() should return False for questions whos
#        pub_date is in the future.
#        """
#        time = timezone.now() + datetime.timedelta(days=30)
#        future_question = Poll(pub_date=time, question="Test Question?")
#        self.assertEqual(future_question.was_published_recently(), False)
#
#    def test_was_published_recently_with_old_question(self):
#        """
#        was_published_recently() should return False for questions whose
#        pub_date is older than one day.
#        """
#        time = timezone.now() - datetime.timedelta(days=30)
#        recent_question = Poll(pub_date=time, question="Test Question?")
#        self.assertEqual(recent_question.was_published_recently(), False)
#
#    def test_was_published_recently_with_recent_question(self):
#        """
#        was_published_recently() should return True for quesions whose
#        pub_date is within the last day
#        """
#        time = timezone.now() - datetime.timedelta(hours=1)
#        recent_question = Poll(pub_date=time, question="Test Question?")
#        self.assertEqual(recent_question.was_published_recently(), True)
#
#class PollViewTests(TestCase):
#
#    def test_index_view_with_no_questions(self):
#        """
#        If no questions exist, an appropriate message should be displayed.
#        """
#        response = self.client.get(reverse('polls:index'))
#        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, "No polls are available.", status_code=200)
#        self.assertQuerysetEqual(response.context['latest_question_list'], [])
#
#    def test_index_view_with_a_past_question(self):
#        """
#        Questions with a pub_date in the past should be displayed on the index page.
#        """
#        create_poll(question="Past question.", days=-30)
#        response = self.client.get(reverse('polls:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_question_list'],
#            ['<Poll: Past question.>']
#        )
#
#    def test_index_view_with_a_future_question(self):
#        """
#        Questions with a pub_datein the future should not be displayed on the index page.
#        """
#        create_poll(question="Future question.", days=30)
#        response = self.client.get(reverse('polls:index'))
#        self.assertContains(response, "No polls are available.", status_code=200)
#        self.assertQuerysetEqual(response.context['latest_question_list'],[])
#
#    def test_index_view_with_future_question_and_past_question(self):
#        """
#        Even if both past and future questions exist, only past questions should
#        be displayed.
#        """
#        create_poll(question="Past question.", days=-30)
#        create_poll(question="Future question.", days=30)
#        response = self.client.get(reverse('polls:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_question_list'],
#            ['<Poll: Past question.>']
#        )
#
#    def test_index_view_with_two_past_questions(self):
#        """
#        The questions index page may display multiple questions.
#        """
#        create_poll(question="Past question 1.", days=-30)
#        create_poll(question="Past question 2.", days=-5)
#        response = self.client.get(reverse('polls:index'))
#        self.assertQuerysetEqual(
#            response.context['latest_question_list'],
#            ['<Poll: Past question 2.>', '<Poll: Past question 1.>']
#        )
#
#
#class QuestionIndexDetailTests(TestCase):
#
#    def test_detail_view_with_a_future_question(self):
#        """
#        The detail view of a question with a pub_date in the future should return
#        a 404 non found page.
#        """
#        future_question = create_poll(question = "Future question.", days=5)
#        response = self.client.get(reverse('polls:detail', args=(future_question.id, )))
#        self.assertEqual(response.status_code, 404)
#
#    def test_detail_view_with_a_past_question(self):
#        """
#        The detail view of a question with a pub_date in the future should return
#        display the question's text.
#        """
#        past_question = create_poll(question = "Past question.", days=-5)
#        response = self.client.get(reverse('polls:detail', args=(past_question.id, )))
#        self.assertContains(response, past_question.question, status_code=200)




