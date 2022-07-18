# Learn how to read information from GitHub using Personal Access Tokens! 

# you need some way to reference a Personal Access Token (PAT) without hard-coding it - NEVER hard-code your PAT or commit it to GitHub
# the PAT needs the following permissions: repo
# how to generate PAT: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
with open('key.txt') as f:
    PAT = f.read()

import github3

github = github3.login(token=PAT)

#Check it's me!
sandra = github.me()
print(sandra)

#get the clone url for a specific named-repo - including private ones
repository = github.repository(sandra, "Onboarding_at_NewSpinCo")
print("Repository is private: " + str(repository.private))
print("Clone URL: " + str(repository.clone_url))
print("Repository description: " + str(repository.description))
