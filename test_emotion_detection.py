import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        res_1 = emotion_detector("I am glad this happened")
        res_2 = emotion_detector("I am really mad about this")
        res_3 = emotion_detector("I feel disgusted just hearing about this")
        res_4 = emotion_detector("I am so sad about this")
        res_5 = emotion_detector("I am really afraid that this will happen")
        
        self.assertEqual(res_1['dominant_emotion'], "joy")
        self.assertEqual(res_2['dominant_emotion'], "anger")
        self.assertEqual(res_3['dominant_emotion'], "disgust")
        self.assertEqual(res_4['dominant_emotion'], "sadness")
        self.assertEqual(res_5['dominant_emotion'], "fear")

unittest.main()