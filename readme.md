# Online Gaming Threats AIL Rules

A library of rules to detect potentially fraudulent gaming websites.

# Description:

The goal is to create a list of files using the [AIL-typosquatting](https://github.com/typosquatter/ail-typo-squatting) library in order to create relevant files that could detect copycats of famous gaming websites. 

Often times, scammers will try to replicate the look of a legit website to convince targets to log in on their copied website and retrieve the credentials to then steal any item of value on the account.

# How to use:
1. Install ail-typo-squatting
```
pip3 install ail-typo-squatting
```

2. Clone the project:
```
git clone https://github.com/Michael57100/Projet_threat_intelligence.git
```

3. Enter the folder and launch the .py file:
```
cd Projet_threat_intelligence
python3 ./gaming_threats.py
```

You should now see a bunch of new .yar and .regex files in the current folder.

# TODO

Given the time constraint of this project, not everything we wanted to achieve has been done.

To fully test the different URLs, it would have been optimal to make a capture of the different typosquatted websites and compare them to the legit website.

There are two approaches that we have thought of to implement this:

1. Check relevant HTML tags such as nav, footer and img: these should be copied 1 to 1 on a relevant copycat website to fool the end user and make him believe he is on the legit website. If those tags were at least 60% (could be more or less) similar to the legit site then it could be considered as fraudulent.

2. Use [Lookyloo](https://github.com/Lookyloo/lookyloo) or another capture tool that creates a screenshot of the instance and renders it in an image file to then analyze the screenshot with AI and compare it to the legit website. Upon a decided threshold of similarity, the website could then be considered as malicious.