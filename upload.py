#!/usr/bin/env python
# -*- coding: utf-8 -*-


from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import os

def upload(filepath):
    qiniu_domain =  'http://7xtq0y.com1.z0.glb.clouddn.com/'
    #需要填写你的 Access Key 和 Secret Key
    access_key = 'NhxOewLDWpAs_THJNvtKN8kZHG3r0_tkWOaJSycc'
    secret_key = 'Cx7AJItEyNWaEG1eLvu85PpCGq0vAaX1xmvJC7c0'

    #构建鉴权对象
    q = Auth(access_key, secret_key)

    #要上传的空间
    bucket_name = 'images'

    #上传到七牛后保存的文件名
    key = os.path.basename(filepath)
    qiniu_url = qiniu_domain + key

    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    #要上传文件的本地路径
    localfile = filepath

    ret, info = put_file(token, key, localfile)
    print(info)
    print('===============')
    print(qiniu_url)

    return qiniu_url
