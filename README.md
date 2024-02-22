## Waits in Playwright Testing with Python

This repo contains code to show how waits in Playwright can be implemented on a chrome browser on LambdaTest cloud platform.

This project uses Pytest as testing framework to run the tests.

### Setup


1. Fork this repo
   * `cd waits-in-playwright`
2. Create a virtual environment with the following command on the terminal

   ```bash
   python3 -m venv env
   ```
3. Activate virtual environment

   ```bash
   source env/bin/activate
   ```
4. Install the following dependencies:
   * Install node package managet

     ```javascript
     npm install
     ```
   * Install PlayWright

     ```bash
     pip3 install playwright==1.39.0
     ```
   * Install other requirements for the project

     ```bash
     pip install -r requirements.txt
     ```
5. In order to run your Playwright tests, you will need to set your LambdaTest username and access key in the environment variables. Click the **Access Key** button at the top-right of the Automation Dashboard to access it.

   \
6. Set your **Username** and **Access Key** as follows:
   * **Linux:**

     ```bash
     export LT_USERNAME="YOUR_LAMBDATEST_USERNAME"
     export LT_ACCESS_KEY="YOUR_LAMBDATEST_ACCESS_KEY"
     ```
   * **Windows:**

   ```bash
   set LT_USERNAME="YOUR_LAMBDATEST_USERNAME"
   set LT_ACCESS_KEY="YOUR_LAMBDATEST_ACCESS_KEY"
   ```

### How to Run the Test

To run the *waits in Playwright* on Chrome on LambdaTest cloud platform:

Navigate into the tests directory: `cd tests`

Run the command: `pytest` on your terminal

* Go to your LambdaTest dashboard
* Click **Automation** on the left side bar
* Click  **Web Automation**
* Select **Configure Test Suite**
* Select **Playwright** as testing framework
* Select **Python** as programming language
* Click **View Results**

You should see results of your test performed as seen in the screenshot below:




