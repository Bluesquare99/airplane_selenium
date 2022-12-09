Airplane Article 1: Deploying Selenium Using Airplane.dev

Selenium is a powerful tool that can be used for end-to-end testing and web scraping, among other uses, as it simulates a user interacting with a site.  Running it locally isn't all too hard but I've consistently struggled to deploy it easily.  This is my guide for how to do so.

Airplane.dev is a wonderful deployment option that offers features such as scheduling, connections to databases, and piping the output to channels like Slack or email. There's an easy-to-use CLI for uploading your code to Airplane, as well.
In Airplane's docs there's an article outlining how to implement Selenium, but it didn't work for me initially or after some (admittedly minor) troubleshooting. So, I'm offering up this repo as the way that I did it, from which I now have a functioning Selenium script.  

The important elements of this repo are:
- main.py, which creates the webdriver.  It uses ChromeDriverManager to install the latest ChromeDriver version so you don't have to worry about versions. 
- airplane_preinstall.sh, which runs a shell script to install necessary packages related to Chrome before installing dependencies from a requirements.txt file
- requirements.txt, which airplane looks for to install dependencies

Have fun!  
