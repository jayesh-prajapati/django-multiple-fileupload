# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import os


def document_directory_path(instance, filename):
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(basename)
    file_type = ""
    image_list = ['.jpeg', '.jpg', '.gif', '.bmp', '.svg', '.psd', 'cpt',
                  'psp', 'cxf', 'pdn', 'jfif', 'exif', 'tiff', 'ppm', 'pgm ', 'pnm']
    video_list = ['.mp4', '.avi', '.wmv', '.m4a', '.3gp', '.3gpp', '.wav',
                  'mov', 'webm', 'hdv', 'vob', 'm4v', 'f4v', 'm4b', 'oga', 'ogv']
    if ext.lower() in image_list:
        file_type = "images"
    elif ext.lower() in video_list:
        file_type = "videos"
    else:
        file_type = "others"
    path = 'media/uploads/%Y/%m/%d/{}/{}{}'.format(file_type, name, ext)
    return datetime.now().strftime(path)


class Fileup(models.Model):
    file = models.FileField(upload_to=document_directory_path)

    def filename(self):
        return os.path.basename(self.file.name)
