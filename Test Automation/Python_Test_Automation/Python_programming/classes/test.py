
# You need to return the urls by which js scripts were downloaded for example.com and all of it subdomains

urls = [
    'http://example.com/resources/main.js?tag_id=a123b',
    'https://example.com/resources/index.js',
    'https://www.example.com/resources/script.js',
    'https://www.example.com/js/script.js',
    'https://sub.domain.example.com/resources/script.js',
    'https://example.com/resources/style.css',
    'https://example.com/images/image1',
    'https://example.com/postback?downloaded_resource=index.js&time=10',
    'https://google.com/postback?downloaded_url=http%3A%2F%2Fexample.com%2Fresources%2Fmain.js%3Ftag_id%3Da123b',
    'https://google.com/script.js',
    'https://amazon.com/postback?downloaded_url=http%3A%2F%2Fexample.com%2Fresources%2Fmain.js%3Ftag_id%3Da123b',
    'https://amazon.com/script.js',
    'https://yahoo.com/postback?downloaded_url=http%3A%2F%2Fexample.com%2Fresources%2Fmain.js%3Ftag_id%3Da123b',
    'https://yahoo.com/script.js',
]

# expected result:
# [
#     'http://example.com/resources/main.js?tag_id=a123b',
#     'https://example.com/resources/index.js',
#     'https://www.example.com/resources/script.js',
#     'https://www.example.com/js/script.js',
#     'https://sub.domain.example.com/resources/script.js',
# ]

# has context menu
# Compose

# l=[i for i in urls if ("example.com/" and ".js" )in i]
# print(l)
l=[]
for i in urls:
    if "example.com/" in i:
        if "%" not in i:
            l.append(i)
l1=[]
for i in l:
    if ".js" in i:
        if "&" not in i:
            l1.append(i)
print(l1)


