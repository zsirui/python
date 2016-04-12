# hash.py

***

这是一个包括CRC32算法，MD5算法和SHA算法的库

### 使用说明

```
import hash

# 计算字符串的CRC32值
crc1 = hash.CRC32('hello, world')
print(crc1.value)

# 计算加盐字符串的CRC32值
salt = 'example'
crc1 = hash.CRC32('hello, world', salt)
print(crc1.value)

# 计算文件的CRC32值
crc2 = hash.CRC32('/user/Documents/file.txt')
print(crc2.value)

# 比较两个CRC32值（不用区分大小写）
h = hash.HASH()
print(h.Compare(crc1.value, crc2.value))

# 计算字符串的MD5值
m1 = hash.MD5('hello, world')
print(m1.value)

# 计算加盐字符串的MD5值
salt = 'example'
m1 = hash.MD5('hello, world', salt)
print(m1.value)

# 计算文件的MD5值
m2 = hash.MD5('/user/Documents/file.txt')
print(m2.value)

# 比较两个MD5值
print(m1.Compare(m1.value, m2.value))

# 计算字符串的SHA1值
s = hash.SHA('hello, world', 'sha1')
print(s.value)

# 计算加盐字符串的SHA1值
salt = 'example'
s = hash.SHA('hello, world', 'sha1', salt)
print(s.value)

# 计算文件的SHA1值
s = hash.SHA('/user/Documents/file.txt', 'sha1')
print(s.value)

# 计算字符串的SHA224值
s = hash.SHA('hello, world', 'sha224')
print(s.value)

# 计算加盐字符串的SHA224值
salt = 'example'
s = hash.SHA('hello, world', 'sha224', salt)
print(s.value)

# 计算文件的SHA224值
s = hash.SHA('/user/Documents/file.txt', 'sha224')
print(s.value)

# 计算字符串的SHA256值
s = hash.SHA('hello, world', 'sha256')
print(s.value)

# 计算加盐字符串的SHA256值
salt = 'example'
s = hash.SHA('hello, world', 'sha256', salt)
print(s.value)

# 计算文件的SHA256值
s = hash.SHA('/user/Documents/file.txt', 'sha256')
print(s.value)

# 计算字符串的SHA384值
s = hash.SHA('hello, world', 'sha384')
print(s.value)

# 计算加盐字符串的SHA384值
salt = 'example'
s = hash.SHA('hello, world', 'sha384', salt)
print(s.value)

# 计算文件的SHA384值
s = hash.SHA('/user/Documents/file.txt', 'sha384')
print(s.value)

# 计算字符串的SHA512值
s = hash.SHA('hello, world', 'sha512')
print(s.value)

# 计算加盐字符串的SHA512值
salt = 'example'
s = hash.SHA('hello, world', 'sha512', salt)
print(s.value)

# 计算文件的SHA512值
s = hash.SHA('/user/Documents/file.txt', 'sha512')
print(s.value)
```