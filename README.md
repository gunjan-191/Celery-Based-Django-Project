# Celery-Based-Django-Project

Celery is a powerful task queue system often used with Django to handle asynchronous tasks. While Redis is a popular choice for Celery's message broker due to its speed and reliability, it's not the only option available. Celery supports multiple brokers including RabbitMQ, Amazon SQS, and even in-memory storage. Here, I'll guide you through setting up Celery with Django using RabbitMQ as the message broker instead of Redis.

#Install Celery:
#First, install Celery using pip:
pip install celery

1) .To install RabbitMQ, you can follow these general steps. However, please note that installation steps might vary slightly depending on your operating system. Here, I'll outline the general steps for installing RabbitMQ on a Linux-based system:
sudo apt update


Install RabbitMQ Server:
Install RabbitMQ server using your package manager. For Debian-based systems like Ubuntu, you can use apt:
sudo apt install rabbitmq-server
This command will install RabbitMQ and its dependencies.

Access RabbitMQ Management Console (Optional):

RabbitMQ comes with a web-based management interface that you can use to monitor and manage your RabbitMQ server. By default, the management plugin is enabled. You can access it using a web browser at:

http://localhost:15672/


Run Celery worker:
Open a terminal, navigate to your Django project directory, and run the Celery worker:
celery -A yourproject worker --loglevel=info
Replace yourproject with the name of your Django project.
