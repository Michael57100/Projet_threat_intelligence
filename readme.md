# Online Gaming Threats AIL Rules

A library of rules to detect potentially fraudulent gaming websites.

# Description:

The goal is to create a list of files using the AIL-typosquatting library in order to create relevant files that could detect copycats of famous gaming websites. 

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