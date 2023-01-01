# file for testing vs_api module

from vs_api import OpenVSX

app = OpenVSX()

search = app.search("python indent",2,'Formatters')
print(search)
