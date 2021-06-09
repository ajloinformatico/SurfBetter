 #!/bin/sh
gunicorn --chdir back __init__:api --thread 2 -b 0.0.0.0:5000
# gunicorn --chdir app app:app -w 2 --thread 2 -b 0.0.0.0:5000
