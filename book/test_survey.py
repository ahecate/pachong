import unittest
from book.survey import AnnoymousSurvey

class TestAnnoymousSurvey(unittest.TestCase):

    def setUp(self):
        question= "what language did you first learn to speak?"
        self.my_survey = AnnoymousSurvey(question)
        self.responses=['English','Spanish','Mandarin']


    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])

        self.assertEqual(self.responses[0],self.my_survey.responses[0])

    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)


if __name__ == '__main__':

    unittest.main()