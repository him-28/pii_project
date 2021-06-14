install:
	docker-compose -f PII_removal.yaml run --rm install

build:
	docker build --no-cache -t PII_project:latest --target PII_project .

exe:
	mkdir -p ~/output
	docker run -v ~/output:~/PII_project/output -it --name pii_project --rm him-28/PII_project

tag:
	docker tag PII_project:latest him-28/PII_project:latest

push:
	docker push him-28/PII_project:latest


