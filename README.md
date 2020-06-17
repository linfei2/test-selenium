# Automated registration test
> Registration with invalid e-mail address on https://www.eobuwie.com.pl/. The test is automated with Selenium WebDriver.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Test Case](#test-case)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
Project based on Page Object Pattern, created for software testing postgraduate course. The purpose of this test is to make sure a user cannot complete registration process providing invalid e-mail address. 

## Technologies
* Python 2.7.17
* Selenium WebDriver

## Setup
Selenium installation:
pip install selenium

Chromedriver installation:
https://sites.google.com/a/chromium.org/chromedriver/downloads

## Test Case

### Title
Registration with invalid e-mail address on https://www.eobuwie.com.pl/
### Environment
Chrome 83.0.4103.61, Ubuntu (64-bit)
### Prerequisite
Browser is opened, user is not logged in
### Steps
* Go to https://www.eobuwie.com.pl/
* Click "Akceptuję" [Accept] on a banner related to content customization
* Click "Zarejestruj" [Register] button
* Enter first name
* Enter last name
* Enter invalid e-mail address
* Enter password
* Confirm password
* Accept website's policy
* Click "Załóż nowe konto" [Create new account]
### Expected result
Registration process is not completed. An error "Wprowadzono niepoprawny adres e-mail" [Invalid e-mail address entered] appears.
### Actual result and comments
Test succeeded. It may be sensitive to website structure changes due to XPATH locators used in the code.

## Inspiration
Based on the code written by Karol Kolański.

## Contact
dominika.matczynska@gmail.com
