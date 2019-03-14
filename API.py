import requests
import Config


def send_img_from_cam(cam, url=Config.send_img_api_url):
    file_path = cam.save_image()
    files = {'image': open(file_path, 'rb')}

    response = None

    try:
        response = requests.post(url, files=files)
    except Exception as e:
        print(e)
    print(response)
    return response
