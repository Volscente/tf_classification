# Base Image
FROM debian

# Change Directory
WORKDIR /opt/

# Create Directory
RUN mkdir tf_classification

# Install Git
RUN apt update \
    && apt install -y git

# Clone Repository
RUN git clone https://github.com/Volscente/tf_classification tf_classification