from ail_typo_squatting import formatOutput, runAll
import math, os

resultList = list()
domainList = ["store.steampowered.com", "rockstargames.com", "signin.rockstargames.com", "epicgames.com",  "ubisoftconnect.com", "account.ubisoft.com",  "ea.com", "signin.ea.com", "auth.eu.shadow.tech", "shadow.tech"]
tamereList = ["store.steampowered.com/login", "epicgames.com/id/login", "microsoft.com/store", "play.google.com/store/games"]
limit = math.inf
formatoutput = "yara"
pathOutput = "."
current_directory = os.getcwd()

for domain in domainList:

    resultList = runAll(
        domain=domain, 
        limit=math.inf, 
        formatoutput=formatoutput, 
        pathOutput=pathOutput, 
        verbose=False, 
        givevariations=False,
        keeporiginal=False
    )

    print(resultList)
    resultList = list()