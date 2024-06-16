import requests

class TestTool:
    def __init__(self):
        self.session = requests.Session()
        self.myHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        
    def get_api(self):
        pass
    
    def post_api(self, url, filename, binnary_data):
        response = self.session.post(url, headers = self.myHeader, files={'file': (filename, binnary_data, f'image/{filename.split(".")[-1]}')})
        return response

class TestModule(TestTool):
    def __init__(self):
        super().__init__()
        
    def png_image_convert(self):
        url = 'http://127.0.0.1:8080/api/v1/img-convert/png/to/JPEG'
        filename = 'cat.png'
        with open('imgs/cat.png','rb') as f:
            binnary_data = f.read()
        response = self.post_api(url, filename, binnary_data)
        with open('imgs/cat.jpg', 'wb+') as f:
            f.write(response.content)
        return response


if __name__ == "__main__":
    tm = TestModule()
    
    img = tm.png_image_convert()
    if img.status_code == 200:
        print('Success png image convert ')
    else:
        print('Failed png image convert')
    
    
    
    
        
    