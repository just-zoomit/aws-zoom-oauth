#!/bin/bash

aws lambda update-function-code --function-name my-function --zip-file fileb://my-deployment-package.zip --region us-east-1