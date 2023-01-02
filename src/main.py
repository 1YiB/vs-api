# file for testing vs_api module

from vs_api import OpenVSX

app = OpenVSX()

namespace  = app.namespace('svelte')
print(namespace)
