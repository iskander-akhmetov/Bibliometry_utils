#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
from selenium import webdriver
import time
import argparse
import tqdm

def main():
    #parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--author_gs_page', help="Author's Google Schoolar page URL")
    
    args = parser.parse_args()
    
    author_gs_page = 'https://scholar.google.com/citations?user=-AEEg5AAAAAJ'
    
    if not args.author_gs_page:
        print("No Author's Google Schoolar page URL, quitting")
        quit
    else:
        author_gs_page = args.author_gs_page
        print("Author's Google Schoolar page URL:", author_gs_page)
    
    


    # # Open an autor GS page

    driver = webdriver.Chrome()
    driver.get(author_gs_page)


    # get author name
    author_name = driver.find_element_by_id('gsc_prf_in').text
    print(author_name,'GS page')


    #open the full publication list
    element = driver.find_element_by_id('gsc_bpf_more')
    while element.is_enabled():
        element.click()
        time.sleep(1)


    # # Collect titles

    titles = driver.find_elements_by_class_name('gsc_a_t')
    print(len(titles)-2, 'publication titles found.')

    print('Getting the titles...')
    titles = [t.text.split('\n') for t in tqdm.tqdm(titles[2:])]
    #titles


    # # Collect numbers of citations
    
    citations = driver.find_elements_by_class_name('gsc_a_c')
    #len(citations)


    #number extraction routine
    num_only = lambda s: ''.join([c for c in s if c in '1234567890'])
    #num_only('54\n*')

    print('Getting numbers of citations...')
    citations = [int(num_only(c.text)) if c.text != '' else 0 for c in tqdm.tqdm(citations[2:])]
    #citations


    # # Collect publication years

    years = driver.find_elements_by_class_name('gsc_a_y')
    #len(years)

    print('Getting years of publication...')
    years = [num_only(y.text) if y.text != '' else '' for y in tqdm.tqdm(years[2:])]
    years
    
    driver.close()
    


    # # Create dataset

    df = pd.DataFrame(titles, columns=['Title', 'Authors', 'Publisher'])
    df['Citations'] = citations
    df['Year'] = years
    #df


    # save dataset


    df.to_csv(author_name.replace(' ','_') + '.csv', index=False)
    print('The data is saved in ' + author_name.replace(' ','_') + '.csv')

if __name__ == "__main__":
    main()



