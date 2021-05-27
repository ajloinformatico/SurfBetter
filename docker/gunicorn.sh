 #!/bin/sh
 gunicorn --chdir app app:app -w 2 --thread 2 -b 0.0.0.0:80
