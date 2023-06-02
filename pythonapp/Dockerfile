FROM --platform=linux/amd64 python:3.9

# Install necessary tools and libraries
RUN apt-get update && \
  apt-get install -y curl gnupg unixodbc-dev gpg-agent


# Add Microsoft repository for ODBC Driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
  mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \
  sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/debian/10/prod buster main" > /etc/apt/sources.list.d/microsoft.list' && \
  apt-get update

# Install Microsoft ODBC Driver for SQL Server
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17

COPY queries.py /queries.py
COPY Mall_Customers.csv /Mall_Customers.csv
COPY alchemy_engine.py /alchemy_engine.py
COPY main.py /main.py
COPY kmeans_functions.py /kmeans_functions.py

RUN pip install pypyodbc
RUN pip install pandas 
RUN pip install sqlalchemy
RUN pip install scikit-learn

ENV annual_income=15
ENV spending_score=35

# Set the default command to run your Python script
CMD ["python", "/main.py", "15", "32"]

