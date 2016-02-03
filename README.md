# 人脸识别－－毕业设计

基于 `opencv-python` 的人脸识别项目，使用其中的 `FaceRecognizer` 的组件作为基础开发的项目。

## 使用方法

### Mac OS X
```shell
brew tap homebrew/science
brew install opencv
```
接着下载源码 `git clone git@github.com:zhengxiaowai/face-recognition.git`
或者 `git clone https://github.com/zhengxiaowai/face-recognition.git`

```shell
cd face-recognition
virtualenv --no-site-packages --python=/usr/bin/pthon2.7 venv
source venv/bin/activate
pip install -r requirement.txt
cp /usr/local/Cellar/opencv/2.4.9/cv.py venv/lib/python2.7/site-packages
cp /usr/local/Cellar/opencv/2.4.9/cv2.so venv/lib/python2.7/site-packages
python run.py
```

- q: 退出
- enter： 训练model
- space： 识别


