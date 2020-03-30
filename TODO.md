
 - ownCloud/NextCloud ([pyocclient](https://github.com/owncloud/pyocclient))

 - Telegram (**python-telegram-bot**, see also [here](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e))

 - Document additional permissions on AWS/user 
    ```
    User: arn:aws:iam::901528470952:user/samuel is not authorized to perform: cloudformation:DescribeStacks on resource: arn:aws:cloudformation:eu-central-1:901528470952:stack/ifq-buddy-dev/*
    ```
   - IAMFullAccess
   - AmazonS3FullAccess
   - AWSCloudFormationFullAccess
   - AWSLambdaFullAccess??