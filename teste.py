data = {'status': 'success', 'photos': [{'url': 'http://www.wallpapermaiden.com/image/2016/11/10/redhead-model-smiling-blue-eyes-bare-shoulders-pink-lipstick-open-mouth-girls-9129.jpg', 'pid': 'F@03d1a5d56d64bc036f9e45253715b9ab_44aad7d559364', 'width': 2048, 'height': 1362, 'tags': [{'uids': [], 'label': None, 'confirmed': False, 'manual': False, 'width': 29.35, 'height': 39.43, 'yaw': -9, 'roll': -3, 'pitch': -15, 'attributes': {'face': {'value': 'true', 'confidence': 72}, 'gender': {'value': 'female', 'confidence': 100}, 'glasses': {'value': 'false', 'confidence': 100}, 'dark_glasses': {'value': 'false', 'confidence': 69}, 'smiling': {'value': 'true', 'confidence': 20}, 'age_est': {'value': '23', 'confidence': 50}, 'mood': {'value': 'neutral', 'confidence': 80}, 'lips': {'value': 'parted', 'confidence': 89}, 'eyes': {'value': 'open', 'confidence': 100}, 'neutral_mood': {'value': 'true', 'confidence': 80}, 'anger': {'value': 'false', 'confidence': 45}, 'disgust': {'value': 'false', 'confidence': 0}, 'fear': {'value': 'false', 'confidence': 0}, 'happiness': {'value': 'true', 'confidence': 62}, 'sadness': {'value': 'false', 'confidence': 0}, 'surprise': {'value': 'true', 'confidence': 73}}, 'points': None, 'similarities': None, 'tid': 'TEMP_F@03d1a5d56d64bc036f9e4525042b01f8_44aad7d559364_52.10_37.00_0_1', 'recognizable': True, 'center': {'x': 52.1, 'y': 37.0}, 'eye_left': {'x': 61.28, 'y': 23.35, 'confidence': 94, 'id': 449}, 'eye_right': {'x': 47.31, 'y': 24.89, 'confidence': 97, 'id': 450}, 'mouth_center': {'x': 54.79, 'y': 44.86, 'confidence': 93, 'id': 615}, 'nose': {'x': 56.49, 'y': 38.62, 'confidence': 93, 'id': 403}}]}],
'usage': {'used': 2, 'remaining': 98, 'limit': 100, 'reset_time': 1559022039, 'reset_time_text': 'Tue, 28 May 2019 05:40:39 +0000'}, 'operation_id': '6f035cc3db4f4735bc1f768bd0cb07c7', 'cur_date': '20190528020610127569', 'dev_type': 'entrance'}


print(data['photos'][0]['tags'][0]['attributes']['gender'])