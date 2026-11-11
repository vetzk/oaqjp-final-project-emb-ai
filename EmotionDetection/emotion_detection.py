import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze or not text_to_analyze.strip():
        return {"anger": None, "joy": None, "sadness": None, "fear": None, "disgust": None}

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    formatted_result = formatted_response['emotionPredictions'][0]['emotion']

    anger = formatted_result['anger'] 
    disgust = formatted_result['disgust'] 
    fear = formatted_result['fear'] 
    joy = formatted_result['joy'] 
    sadness = formatted_result['sadness'] 
    
    dominant_emotion = max(formatted_result, key=formatted_result.get)
    formatted_result['dominant_emotion'] = dominant_emotion
    return formatted_result
