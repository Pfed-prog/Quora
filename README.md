# Quora
This repo is aimed at working with Quora Partners page. 
The script uses specified login and password to send requests for an answer from the partners page. 

# How to run:
Windows:
```python
py quora.py
```
Linux Debian:
```python
python3 quora.py
```
Edit the line in the script with your password and email:
```python
my_bot = Bot('Email', 'Password')
```
# Tested on
Windows 10 64-bit using Chrome browser &&
Kali Linux 20.20.4 32-bit
# Installation
Selenium:
```bash
pip3 install selenium
```
webdrivers for Firefox:
https://github.com/mozilla/geckodriver/releases/tag/v0.28.0
