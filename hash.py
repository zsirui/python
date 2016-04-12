#!/usr/bin/python
#-*- coding:utf-8 -*-

import hashlib
from os.path import isfile
from zlib import crc32

class HASH():
	"""docstring for hash"""
	def __init__(self, src = '', salt = ''):
		self.src = src
		self.salt = salt

	def Compare(self, src, target):
		if src.upper() == target.upper():
			return True
		else:
			return False
		

class MD5(HASH):
	def __init__(self, src, salt = ''):
		HASH.__init__(self, src, salt)
		self.value = self.md5Value(self.src)

	def md5Value(self, src):
		m = hashlib.md5()
		if isfile(src):
			with open(src, 'rb') as fh:
				while True:
					data = fh.read(8192)
					if not data:
						break
					m.update(data)
		else:
			m.update(src + self.salt)
		return m.hexdigest()
		
class CRC32(HASH):
	"""docstring for CRC32"""
	def __init__(self, src, salt = ''):
		HASH.__init__(self, src, salt)
		self.value = self.crcValue(self.src)
		
	def crcValue(self, src):
		crc = 0
		if isfile(src):
			with open(src, 'rb') as fh:
				while True:
					data = fh.read(8192)
					if not data:
						break
					crc = crc32(data, crc)
		else:
			crc = crc32(src + self.salt, crc)
		return str(hex(crc & 0xffffffff))[2:]

class SHA(HASH):
	"""docstring for SHA"""
	def __init__(self, src, Type, salt = ''):
		HASH.__init__(self, src, salt)
		self.type = self.setType(Type)
		self.value = self.shaValue(src, self.type)

	def setType(self, Type):
		typelist = [['SHA1', hashlib.sha1()], ['SHA224', hashlib.sha224()], ['SHA256', hashlib.sha256()], ['SHA384', hashlib.sha384()], ['SHA512', hashlib.sha512()]]
		for t, m in typelist:
			if Type.upper() == t:
				return m
		return typelist[0][1]

	def shaValue(self, src, Type):
		s = Type
		if isfile(src):
			with open(src, 'rb') as fh:
				while True:
					data = fh.read(8192)
					if not data:
						break
					s.update(data)
		else:
			s.update(src + self.salt)
		return s.hexdigest()
