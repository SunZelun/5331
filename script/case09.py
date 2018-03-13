import requests

# Set up form elements - these will become the input elements in the form
data= {
   'csrf_token' : 'wkjdb-iouer-234k3-wklu3k', 
   'data' : '<script>alert("CSRF Token never changed")</script>)'
}

r = requests.post('http://localhost/5331/case09.php', data=data)

print r.text
