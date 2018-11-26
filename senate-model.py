import math
import lib.scraper

state = str(input("Input state in which election is held:   "))
year = int(input("Enter year in which election is taking place"))

incumbent = str(input("Incumbent? Y/N   "))
inc_party = str(input("Party of incumbent? D/R  "))

midterm = str(input("Midterm? Y/N   "))
mid_pres = str(input("Party of President? D/R   "))

last_job_d = str(input("Democrat's last job?    "))
last_job_r = str(input("Republican's last job?  "))
