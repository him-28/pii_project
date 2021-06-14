install:
	docker-compose -f PII_removal.yaml run --rm install

build:
	docker build --no-cache -t pii_project:latest --target pii_project .

exe:
	mkdir -p /home/$USER/output
	docker run -v /home/$USER/output:/home/himanshu/pii_project/output -it --name pii_test --rm him-28/pii_project

tag:
	docker tag pii_project:latest him-28/pii_project:latest

push:
	docker push him-28/pii_project:latest


