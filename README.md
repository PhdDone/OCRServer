# OCR server

####Workflow
Upload a image file to server -> server stores the image and run OCR -> server returns the image and OCR results

####Usage
```
sudo yum update
sudo yum install -y python-devel python-setuptools python-pip
sudo pip install --upgrade pip
sudo pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python app.py
```

####References:
https://realpython.com/blog/python/setting-up-a-simple-ocr-server/
https://realpython.com/blog/python/setting-up-a-simple-ocr-server/
https://github.com/ibininja/upload_file_python