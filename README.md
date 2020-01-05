# clydeatdlsu
Azure Web App

### Setup
- [x] Python Environment

### Steps

1. Create new repo and clone.
```bash
> git clone <github repo here>
> cd <github repo name>
```

2. Create python script.
```python
# hello.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello Azure!</h1>"
```

3. Install and run flask.
```bash
> conda activate base
(base) > pip install flask
(base) > $env:FLASK_APP = "hello.py"
or
(base) > set FLASK_APP=hello.py
(base) > flask run
 * Serving Flask app "hello.py"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

4. Create ```.gitignore``` file.
```text
venv/
__pycache__/
.vscode/
```

5. Create azure resource group [here](https://portal.azure.com/#home).
  1. Go to left navigation and click Resources
  2. Add new resources
  3. Fill in input fields
    * Subscription: Azure subscription 1
    * Resource group: clydeatuic-flask-resource-group
    * Region: (Asia Pacific) Southeast Asia
  4. Review and create.

6. 