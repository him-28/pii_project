![](https://github.com/him-28/PII_project/workflows/PII%20Removal/badge.svg)

# PII Removal

Created a python based utility that removes Personally Identifiable Information(PII) from the PDF kept in `input` directory and saves the result in the `output` directory.

## Running PII Removal Locally

Command:

 ```bash
 
 git clone https://github.com/him-28/pii_project.git

 cd pii_project

 docker build . -t him-28/pii_project

 docker run -v /home/$USER/output:/home/himanshu/pii_project/output -it --name pii_test --rm him-28/pii_project

 ```
