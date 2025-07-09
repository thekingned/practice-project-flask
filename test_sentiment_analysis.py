from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Test with a positive sentiment text
        result_1 = sentiment_analyzer("I love programming!")
        self.assertIn('label', result_1)
        self.assertIn('score', result_1)
        self.assertEqual(result_1['label'], 'POSITIVE')
        self.assertGreater(result_1['score'], 0.5)

        # Test with a negative sentiment text
        result_2 = sentiment_analyzer("I hate bugs in my code.")
        self.assertIn('label', result_2)
        self.assertIn('score', result_2)
        self.assertEqual(result_2['label'], 'NEGATIVE')
        self.assertGreater(result_2['score'], 0.5)

if __name__ == '__main__':
    unittest.main()