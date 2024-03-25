from ail_typo_squatting import formatOutput, runAll
import math, os

resultList = list()

domainList = ["store.steampowered.com", "rockstargames.com", "signin.rockstargames.com", "epicgames.com",  "ubisoftconnect.com", "account.ubisoft.com",  "ea.com", "signin.ea.com", "auth.eu.shadow.tech", "shadow.tech"]

#Cannot typosquat login urls as "/" character causes problems in path of folders
loginList = ["store.steampowered.com/login", "epicgames.com/id/login", "microsoft.com/store", "play.google.com/store/games"]

limit = math.inf
formatOutput = ["regex", "yara"]
pathOutput = "."

for domain in domainList:
    for FormatOutput in formatOutput:
        resultList = runAll(
            domain=domain, 
            limit=math.inf, 
            formatoutput=FormatOutput, 
            pathOutput=pathOutput, 
            verbose=False, 
            givevariations=False,
            keeporiginal=False
        )

        
        resultList = list()
        
print("Rules created in this folder")