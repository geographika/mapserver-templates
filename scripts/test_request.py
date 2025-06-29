r"""
C:\VirtualEnvs\misc\Scripts\Activate.ps1
cd D:\GitHub\mapserver-templates\scripts
python test_request.py
"""
import http.client
from urllib.parse import urlparse

# Target URL
url = "http://localhost:8080/oapifdemo/ogcapi/"
parsed_url = urlparse(url)

# Establish connection
conn = http.client.HTTPConnection(parsed_url.hostname, parsed_url.port)

# Make request
conn.request("GET", parsed_url.path, headers={"Accept": "application/json"})

# Get response
response = conn.getresponse()
print("Status code:", response.status)
print("Response headers:", response.getheaders())
print("Response body:", response.read().decode())

# Make request
conn.request("GET", parsed_url.path, headers={"Accept": "text/html"})

# Get response
response = conn.getresponse()
print("Status code:", response.status)
print("Response headers:", response.getheaders())
print("Response body:", response.read().decode())

conn.close()
