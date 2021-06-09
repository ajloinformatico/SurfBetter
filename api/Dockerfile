# Flask
FROM python:3
# Create api directory
RUN mkdir /api
# Set work directory
WORKDIR /api
# Copy API data
COPY * .
# RUN mkdir /database
# COPY database/database.db /database
# Run Api dependency
RUN pip3 install -r apirequirements.txt
# RUN mkdir database
# RUN touch database/database.db
# Expose port
EXPOSE 5000
# Run flask by gunicorn server
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "wsgi:app"]
