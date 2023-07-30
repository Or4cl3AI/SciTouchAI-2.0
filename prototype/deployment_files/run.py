```python
from flask import Flask
from prototype import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
```