![](https://github.com/him-28/PII_project/workflows/PII%20Removal/badge.svg)

# PII Removal

Created a python based utility that removes Personally Identifiable Information(PII) from the PDF kept in `input` directory and saves the result in the `output` directory.

## Running PII Removal Locally

Command:

 ```bash
 docker run -v ~/output:~/pii_project/output -it --name pii_project --rm him-28/pii_project
 ```
