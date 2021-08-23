FLASK_APP=app.py flask run --host=0.0.0.0 --port=8090


docker build -t claytantor/gpt-neo-poc:latest .


aws configure
pip install awscli
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 705212546939.dkr.ecr.us-west-2.amazonaws.com
docker tag claytantor/gpt-neo-poc:latest 705212546939.dkr.ecr.us-west-2.amazonaws.com/claytantor/gpt-neo-poc:latest
docker push 705212546939.dkr.ecr.us-west-2.amazonaws.com/claytantor/gpt-neo-poc:latest
