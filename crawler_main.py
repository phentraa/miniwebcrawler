'''
Author:         Kovács Péter
Date:           2022.06.
Description:    A small web crawler which can look for links in a given html source and
                follow them recursively up to a given depth. 
                It produces a site tree as an output to the console, or into a given file.

                In this main file you can specify which iteration of your program will run. 
                (iterations: stages of current development process)
'''

# You can import crawler_iteration_x.py files here which contains the actual run() function
from crawler_iterations import crawler_iteration_3 as crawler

# Run iteration 1,2 or 3
if __name__ == "__main__":
    print("Crawler is working...")
    crawler.run()  
    print("Crawler finished!")