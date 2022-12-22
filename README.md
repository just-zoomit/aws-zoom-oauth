<!-- GETTING STARTED -->
## Getting Started

This is an simple example python script that shows how to implement an AWS Lambda function that exchange the code for an access token and Retrieve the user’s details from direct invocation.


### Prerequisites

* AWS Account 
* Zoom Account 
* Python 3.7 or greater

### Installation

1. Create [Zoom Marketplace OAuth App](https://marketplace.zoom.us/docs/guides/build/oauth-app/) and get Client ID and Client Secert 


2. Clone the repo
   ```sh
   git clone https://github.com/just-zoomit/aws-zoom-oauth.git
   ```
3. Install requests
   ```sh
   pip install --target ./package requests
   ```

4. Deploy your .zip file to the AWS lambda function

    ```sh
    sh lambda-update.sh 
    ```

5. In the lambda console, verify the function updated as expected. 
