Web Applications
================

Local Applications
------------------

- Apps created so far are accessible from the local device only
- Basic functions (`print` and `input`) interact with the system in text mode
- These limitation make it challenging to create modern apps

Hypertext
---------

- Text document with links to other text documents
- Provides the basis for the world wide web

---

![Hyperlinked documents](https://upload.wikimedia.org/wikipedia/commons/4/41/Sistema_hipertextual.jpg)

HTTP
----

- Hypertext transfer protocol
- Provides a mechanism to request hypertext documents from remote systems

Flask
-----

- Python package to implement HTTP servers

Example
-------

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world!"
```

URL
-----

- Provides a unique identifier for a hypertext document
- Sent by a user agent as part of an HTTP request

HTML
----

- Hypertext markup language
- Domain specific language used to describe hypertext documents

Hyperlinks
----------

- Created in HTML using `<a>` tags
- A hypertext reference (`href`) may be included to link to another document

Example
-------

```python
from flask import Flask

app = Flask(__name__)

@app.route("/page1")
def page1():
    return "Page 1 <a href=/page2>Go to page 2</a>"

@app.route("/page2")
def page2():
    return "Page 2 <a href=/page1>Go to page 1</a>"
```

Extended Example
----------------

```python
from flask import Flask, request, session
import languagemodels

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def home():
    if not "history" in session:
        session["history"] = ""
        
    usertext = request.args.get("usertext", "")
    session["history"] += f"<p>User: {usertext}"    
    
    response = languagemodels.do(f"Respond to a user: {usertext}")
    session["history"] += f"<p>Bot: {response}"
    
    return """
<form action=/>
<input type=text name=usertext />
<input type=submit />
</form>
""" + session["history"]
```
