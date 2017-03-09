#!/user/bin/env python3
# -*- coding: utf-8 -*-

__autuor__ = 'lixin'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coreweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(requset):
	users = await User.findAll()
	return {
		'__template__': 'test.html',
		'users': users
	}
	