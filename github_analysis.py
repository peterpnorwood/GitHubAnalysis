import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas as pd

## Pulling Openshift Information
openshift = contributors_breakdown("openshift")

## Openshift Plots
num_bins = 10
x = [0,10,20,30,40,50,60,70,80,90,100] 
x_tix = ["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
n, bins, patches = plt.hist(openshift["percent"]*100, num_bins, facecolor="#CC0000", alpha=1)
plt.ylabel("Number of Repositories", size = 12.5)
plt.xlabel("Percentage of Contributors with Red Hat Listed as their Employer on Github")
plt.xticks(x, x_tix, size = 10)
plt.title("Openshift (Repositories With 10 or More Contributors)", size = 15)
plt.show()


plt.scatter(x = openshift["size"], y = openshift["percent"]*100, color = "#CC0000")
plt.ylabel("Percentage of Contributors with Red Hat Listed as their Employer on Github")
plt.yticks(x, x_tix, size = 10)
plt.title("Openshift (Repositories With 10 or More Contributors)", size = 15)
plt.xlabel("Number of Contributors", size = 12.5)
plt.ylabel("Percentage of Contributors From Red Hat", size = 12.5)


## Pulling Ansible Information
ansible = contributors_breakdown("ansible")

## Ansible Plots
num_bins = 7
n, bins, patches = plt.hist(ansible["percent"]*100, num_bins, facecolor="#CC0000", alpha=1)
plt.ylabel("Number of Repositories", size = 12.5)
plt.xlabel("Percentage of Contributors with Red Hat Listed as their Employer on Github")
plt.xticks(x, x_tix, size = 10)
plt.title("Ansible (Repositories With 10 or More Contributors)", size = 15)
plt.show()

plt.scatter(x = ansible["size"], y = ansible["percent"]*100, color = "#CC0000")
plt.ylabel("Percentage of Contributors with Red Hat Listed as their Employer on Github")
plt.yticks(x, x_tix, size = 10)
plt.title("Ansible (Repositories With 10 or More Contributors)", size = 15)
plt.xlabel("Number of Contributors", size = 12.5)
plt.ylabel("Percentage of Contributors From Red Hat", size = 12.5)

## Adding the Repos to the Plot
for i, txt in enumerate(ansible["repos"]):
    plt.text(x = ansible["size"][i], y = ansible["percent"][i]*100, s = txt[8:], rotation=-30, size = 10)
plt.show()
