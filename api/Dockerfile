# Flask
FROM python:3
# Create api directory
RUN mkdir /api
# Set work directory
WORKDIR /api
# Copy API data
COPY * .
# Run Api dependency
RUN pip3 install -r apirequirements.txt
RUN mkdir database
RUN touch database/database.db
# Expose port
# EXPOSE 5000
# Run flask
CMD ["python3","main.py"]

# Set gunicorn server ["./gunicorn.sh"]
# ENTRYPOINT ["./gunicorn.sh"]