# ifq-buddy

A Slack bot to handle the download of IFQ issues

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This bot requires an AWS account. All services can run fine within the free tier.

You need to install the following tools:

* [Node.js](https://nodejs.org/en/) — tested with v12.14.1 (via nvm), required to run the Serverless Framework.
* [Python](https://www.python.org) 3.7, the language used to write all the application code.
* [Pipenv](https://pipenv.kennethreitz.org/en/latest/) — tested with version 2018.11.26, it's used to streamline development in Python projects.
* [AWS CLI](https://aws.amazon.com/cli/) - the AWS command line interface, used to manage environment setting using the [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html).


### Installing

A step by step series of steps that tell you how to get a development env running.

First, you need to get the project source code:

```bash
$ git clone git@github.com:zmoog/ifq-buddy.git  # you can also use the https endpoint

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

```
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

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
