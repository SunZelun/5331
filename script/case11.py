#alert cookie
import webbrowser
import requests

# Set up form elements - these will become the input elements in the form

data= {
   'qty' : 1, 
   'Price' : 1
}

url = "http://localhost/5331/case11.php"
r = requests.post(url, data=data)

print r.text
