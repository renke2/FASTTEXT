#-*- coding:utf-8 -*-

import os
import sys
import json
import time
from flask import Blueprint, render_template, request, \
        send_from_directory, redirect, url_for, flash
from utils import interface_fasttext
mod = Blueprint('emotion', __name__, url_prefix='/emotion')

@mod.route('/')
def index():
    """返回页面
    """
    return 'false url'

@mod.route('/calculate_emotion', methods=['GET']) 
def short_calculate_test():
    text = request.args.get('text', '')
    label = interface_fasttext(text)
    return json.dumps(label)
