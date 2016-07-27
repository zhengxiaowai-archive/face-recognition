#!/usr/bin/env python # -*- coding: utf-8 -*- 
import requests
import time

API_KEY = '7f8470a6a0bbbe77e34a41a4ae860e4c'
API_SECRET = 'FpzsUigs2Lmu-_PFaimlTDPmIrSXPGkY'
FACESET_NAME = 'all_faceset'
FACESET_ID = 'd0124766aa3fb868660d02bd137c4a14'

CREATE_PERSON_URL = 'https://apicn.faceplusplus.com/v2/person/create'
FACE_DETECT_URL = 'http://apicn.faceplusplus.com/v2/detection/detect'
ADD_FACE_URL = 'https://apicn.faceplusplus.com/v2/person/add_face'
TRAIN_VERIFY_URL = 'https://apicn.faceplusplus.com/v2/train/verify'
GET_SESSION_INFO_URL = 'https://apicn.faceplusplus.com/v2/info/get_session'

RECOGNITION_VERIFY_URL = 'https://apicn.faceplusplus.com/v2/recognition/verify'
RECOGNITION_SEARCH_URL = 'https://apicn.faceplusplus.com/v2/recognition/search'

CREATE_FACESET_URL = 'https://apicn.faceplusplus.com/v2/faceset/create'
ADD_FACE_TO_FACESET_URL = 'https://apicn.faceplusplus.com/v2/faceset/add_face'
TRAIN_FACESET_URL = 'https://apicn.faceplusplus.com/v2/train/search'


def create_person(person_name):
    data = {'api_key': API_KEY, 'api_secret': API_SECRET,
            'tag': 'person', 'person_name': person_name}

    r = requests.get(CREATE_PERSON_URL, data)
    return r.json()['person_name']


def face_detect(url):
    data = {'api_key': API_KEY, 'api_secret': API_SECRET,
            'url': url, 'mode': 'oneface', 'async': True}

    r = requests.get(FACE_DETECT_URL, data)
    session_id = r.json()['session_id']

    rr = get_session(session_id)
    rr_res = rr
    face_counts = len(rr_res['result']['face'])
    if face_counts == 0:
        print(face_counts)
        print('error')
        return -1
    #while face_counts == 0:
    #    r = requests.get(FACE_DETECT_URL, data)
    #    session_id = r.json()['session_id']

    #    rr = get_session(session_id)
    #    rr_res = rr
    #    face_counts = len(rr['result']['face'])
    #    print('while')
    #    time.sleep(1)

    print(rr_res)
    return rr_res['result']['face'][0]['face_id']

def add_face(face_id, person_name):
    data = {'api_key': API_KEY, 'api_secret': API_SECRET,
            'face_id': face_id, 'person_name': person_name}

    r = requests.get(ADD_FACE_URL, data)
    return r.json()['success']

def train_verify(person_name):
    data = {'api_key': API_KEY, 'api_secret': API_SECRET,
            'person_name': person_name}

    r = requests.get(TRAIN_VERIFY_URL, data)
    return r.json()['session_id']

def get_session(session_id):
    data = {'api_key': API_KEY, 'api_secret': API_SECRET,
            'session_id': session_id}

    r = requests.get(GET_SESSION_INFO_URL, data)
    return r.json()
    
def recognition_verify(other_face_id, person_name):
    data = {'api_key': API_KEY, 'api_secret': API_SECRET,
            'face_id': other_face_id, 'person_name': person_name}

    r = requests.get(RECOGNITION_VERIFY_URL, data)
    return r.json()

def recognition_search(key_face_id, count=1):
    data = {'api_key': API_KEY, 'api_secret': API_SECRET,
            'key_face_id': key_face_id, 'faceset_id': FACESET_ID,
            'count': count}

    r = requests.get(RECOGNITION_SEARCH_URL, data)
    return r.json()

    

'''
    faceset
'''
def create_faceset(faceset_name):
    data = {'api_key': API_KEY, 'api_secret': API_SECRET,
            'faceset_name': faceset_name}

    r = requests.get(CREATE_FACESET_URL, data)
    return r.json()

def add_face_to_faceset(face_id):
    data = {'api_key': API_KEY, 'api_secret': API_SECRET,
            'face_id': face_id, 'faceset_id': FACESET_ID}

    r = requests.get(ADD_FACE_TO_FACESET_URL, data)
    return r.json()

def train_faceset():
    data = {'api_key': API_KEY, 'api_secret': API_SECRET,
            'faceset_id': FACESET_ID}

    r = requests.get(TRAIN_FACESET_URL, data)
    return r.json()['session_id']

