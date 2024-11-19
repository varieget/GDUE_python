"""
Tom
num：13456
addr：Foo street 45
"""

dname = dict({
    "stu": [
        {"name": "Tom", "num": "123456", "addr": "Foo street 45"},
        {"name": "Lily", "num": "456789", "addr": "Bar street  23"},
        {"name": "Jack", "num": "789123", "addr": "5th street 56"},
    ]
})

searchname = input()
print(searchname)

for name in dname['stu']:
    if name['name'] == searchname:
        print("num:", name['num'])
        print("addr:", name['addr'])
