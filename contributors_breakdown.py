import pandas as pd
from github import Github
import time

def contributors_breakdown(product, account="redhat1502", password="1502redhat"):
    
    """
    Gets a breakdown of how many contirbutors to Red Hat products on Github work at Red Hat
    
    :param product:     The Red Hat Product of interest's github name.  For example "ansible" and "openshift", or "openstack.org"
    :param accout:      github account to log into the api, default is an account made for this project
    :param password:    github password to log into the apim default is a password made for this project
    :return:            a dataframe with three columns: repository, percentage of repository contirbutors that list Red Hat as their company on Github, and number of contributors
    """
    
    git = Github(account,password)
    org = git.get_organization(product)
    
    ## Creating the vectors that the loop will fill  
    percs_dist = []
    repos_dist = []
    size_dist = []

    for repos in org.get_repos():
        
        print((str(git.rate_limiting)[:5].replace("'","").replace("(",""))).replace(",","")
        print(repos)
        
        ## If the limit is getting low, this will let the program wait until the rate limit is reset
        if int(str(git.rate_limiting)[:5].replace("'","").replace("(","").replace(",","")) < 300:
           time_left = int(git.rate_limiting_resettime) - int(time.time())
           print(time_left)
           time.sleep(time_left + 10)
            
        
        ## Temporary vectors
        percs = []
        companies = []
        users = []
    
        ## Creating the string of the repos and pulling the contributors
        repo_str = str(repos)[22:].replace('"','').replace(')','')
        repo = git.get_repo(repo_str)
        cont = repo.get_contributors()
    
        ## Keeping only the repositories with 10 or more contributors
        lst = []
        for x in cont:
            lst.append(x)
    
        if len(lst) < 10:
            continue
    
        ## Grabbing and cleaning all the users    
        for x in cont:
            user = str(x)[17:].replace('"','').replace(')','')
            users.append(user)
    
        ## Grabbing all the users' companies
        for x in users:
            user = git.get_user(x)
            companies.append(user.company)
            
        ## Created a binary variable if Red Hat or Ansible appears as the company name
        companies = pd.Series(companies).str.lower()
        df = (companies.str.contains("redhat|red hat|ansible|@ansible")*1).fillna(0.0)
    
        ## Getting the number of contributors to filter out the small ones later
        size = df.size
    
        ## Calculating what percent of contributors have Red Hat listed    
        perc = df.mean()
    
        ## Appending the percent and size to the overall vectors
        repos_dist.append(repo_str)
        percs_dist.append(perc)
        size_dist.append(size)
    
    
    ## Creating and retuing the final dataframe    
    contributors_breakdown = pd.DataFrame({"repos" : repos_dist,
                                            "percent" : percs_dist,
                                            "size" : size_dist})
    
    return(contributors_breakdown)
