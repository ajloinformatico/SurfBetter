 #!/bin/sh
gunicorn --chdir -w 4 manager:api -b 0.0.0.0:5000
# gunicorn --chdir app app:app -w 2 --thread 2 -b 0.0.0.0:5000
