FROM python:3.7
RUN apt-get update && apt-get install -y python3-pip
# Copy contents into image
COPY . .
RUN pip3 install pymysql
# Install pip dependencies from requirements
RUN pip3 install -r requirements.txt
# Set YOUR_NAME environment variable

# Expose the correct port
EXPOSE 5001
# Create an entrypoint
ENTRYPOINT ["/usr/local/bin/python3" , "app.py"]