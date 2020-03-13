# ifq-buddy

A Slack bot to handle the download of IFQ issues

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This bot requires an AWS account. All services can run fine within the free tier.

You need to install the following tools:

* [Git](https://git-scm.com)
* [Node.js](https://nodejs.org/en/) — tested with v12.14.1 (via [nvm](https://github.com/nvm-sh/nvm)), required to run the Serverless Framework.
* [Python](https://www.python.org) 3.7, the language used to write all the application code. You should evaluate [pyenv](https://github.com/pyenv/pyenv#installation) as tool to manage Python versions.
* [Pipenv](https://pipenv.kennethreitz.org/en/latest/) — tested with version 2018.11.26, it's used to streamline development in Python projects.
* [AWS CLI](https://aws.amazon.com/cli/) - the AWS command line interface, used to manage environment setting using the [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html).


### Installing

A step by step series of steps that tell you how to get a development env running.

First, you need to get the project source code:

```bash
$ git clone https://github.com/zmoog/ifq-buddy.git

$ cd ifq-buddy
```

Create/activate the virtual environment for this project:

```bash
$ pipenv shell
```


Install the project dependencies:

```bash
# installs the Serverless Framework dependencies
$ npm install

# installs the Python deps
$ pipenv install -dev
```


Set some environment variables and aliases:

```bash

# we use the local version of Serverless here
$ alias sls='./node_modules/.bin/sls'

$ export PYTHONPATH=`pwd`:$PYTHONPATH 

# configure the shell to access your AWS account
$ export AWS_PROFILE=<YOUR_PROFILE_NAME>
```


Configure the parameter store variables (they will be used as environment variable, see `serverless.yml` for more details):

```bash
$ aws ssm put-parameter --name "/ifq_buddy/dev/ifq/username" --value "your email address" --type String
{
    "Version": 1,
    "Tier": "Standard"
}

$ aws ssm put-parameter --name "/ifq_buddy/dev/ifq/password" --value "secret!" --type String
{
    "Version": 1,
    "Tier": "Standard"
}
```


Let's run the lambda function locally to see if it's all working!

```bash
$ sls invoke local -f sync
{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v1.0! Your function executed successfully!\", \"input\": {}}"
}
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system.

If you have alread set up your development environment the actual deploy is easy.

```bash
$ sls deploy --stage dev  
Serverless: Generating requirements.txt from Pipfile...
Serverless: Parsed requirements.txt from Pipfile in /Users/mbranca/code/projects/zmoog/ifq-buddy/.serverless/requirements.txt...
Serverless: Using static cache of requirements found at /Users/mbranca/Library/Caches/serverless-python-requirements/75512bb3ef5416497bd7dbae33f748f83aef5eb55445c03e2ec3c17d0fb44d48_slspyc ...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service ifq-buddy.zip file to S3 (5.26 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.........
Serverless: Stack update finished...
Service Information
service: ifq-buddy
stage: dev
region: eu-west-1
stack: ifq-buddy-dev
resources: 6
api keys:
  None
endpoints:
  None
functions:
  sync: ifq-buddy-dev-sync
layers:
  None
Serverless: Run the "serverless" command to setup monitoring, troubleshooting and testing.
```


## Built With

* [Serverless Framework](https://serverless.com) - The serverless framework used to deploy on AWS
* [ifq](https://github.com/zmoog/ifq) - A tiny library used to scrape the IFQ website using [requests](https://requests.readthedocs.io/en/master/) and [lxml](https://lxml.de).

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/zmoog/76aef48ad9d9faa096c41c7b16f2fc7c) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Maurizio Branca** - *Initial work* - [zmoog](https://github.com/zmoog)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
