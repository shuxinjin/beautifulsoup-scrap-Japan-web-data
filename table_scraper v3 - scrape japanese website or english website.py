
"""
Created on Thu Nov 28 23:04:58 2019

@author: shuxin.jin@hotmail.com
"""
#imports
import requests
from bs4 import BeautifulSoup
from docutils.parsers.rst.directives import encoding
import csv


import chardet


################global setting ,please change it to your setting ####################
#japanese
#nation_language1 = 'shift_jis',japanese website
nation_language1 = 'shift_jis'
# English website
nation_language2 = 'utf-8'
#getting raw html
url = "https://search.sbisec.co.jp/v2/popwin/info/stock/pop6040_usequity_list.html"
#raw_html = requests.get(url).text
raw_html = requests.get(url)
#print(raw_html.encoding) 驛帑ｹ滂ｿｽ竏ｵ蟀ｿ陟托ｿｽ (request 霑ｪ諛�蝎ｪ 闕ｳ蝣ｺ�ｽｸ�ｿｽ陞ｳ螢ｼ�ｽｯ�ｽｹ)
#setting the language you scrape website.
raw_html.encoding = nation_language1

#assign coding 
#raw_html.encoding = nation_language1


#preparing BeautifulSoup file
#bs_html = BeautifulSoup(raw_html.text, 'lxml')
#bs_html = BeautifulSoup(raw_html.text, 'lxml')
#bs_html = BeautifulSoup(raw_html.text , 'html.parser')
bs_html = BeautifulSoup(raw_html.text , 'html.parser')
#field number , 
field_num =4
#if header length less than this, no necessary to process more.
MinMeaningLen=10 
#save folder
flder_n = 'C:/jintmp/20191224'
#####################################################################################

def gen_csv_file(i,soup,table):
    #initialisation of parameters
    csv_string = ""
    stripped = ""
    j=1
    #geting headers from table
    headers = [header.text for header in table.find_all('th')]
    #preparing headers to csv format
    headers_string = ""
    for head in headers:
        headers_string = headers_string + head + ","
    headers_string = headers_string[:-1] + "\n"
    #let the fun begins!
    if len(headers_string)<MinMeaningLen:
        pass
    else:
        #fd = open(flder_n+'/table_dat_crap'+str(i)+'.csv','a+',encoding='utf-8')
        #with open(flder_n+'/table_dat_crap'+str(i)+'.csv','a+',encoding='utf-8') as fd:
        with open(flder_n+'/rakuten_data_crap'+str(i)+'.csv','a+',encoding= nation_language2) as fd:
            #write = csv.writer(fd)
            #write = csv.writer(fd,delimiter=';',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            #not this write is abandoned for double quotes be bring to the file.
            write = csv.writer(fd,delimiter=';',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            #write.writerow( [table.get_text()])
    
              
#             list_of_rows = []
#             for row in table.findAll('tr'):
#                 list_of_cells = []
#                 #headers
#                 header = [header.text for header in row.find('th')]
#                 #only one,
#                 list_of_cells.append(header)    
#                 for cell in row.findAll('td'):
#                     text = cell.text.replace('&nbsp;', '')
#                     list_of_cells.append(text) 
#                 list_of_rows.append(list_of_cells)
#             #    
#             writer.writerows(list_of_rows)
            
            #writing headers to csv file
            #write.writerow([headers_string])
            
            #writing rows to csv table
############################
#             for tr in table.find_all('tr'):
#                 #special format,it is a format table tr  -->th-->td
#                 ths = tr.find_all('th')
#                 row1 = [elem.text.encode(nation_language1) for elem in ths ]
#                   
#                 tds = tr.find_all('td')
#                 row = [elem.text.encode(nation_language1) for elem in tds ]
#                 rowss = row1+row
#                 write.writerow(row1+row)
#                 #print(str(rowss))         



#########################   


############################
#             for tr in table.find_all('tr'):
#                 #special format,it is a format table tr  -->th-->td
#                 ths = tr.find_all('th')
#                 row1 = [elem.text.encode(nation_language1) for elem in ths ]
#                    
#                 tds = tr.find_all('td')
#                 row = [elem.text.encode(nation_language1) for elem in tds ]
#                 rowss = row1+row
#                 write.writerow(row1+row)
                #print(str(rowss))         



#########################   
            for tr in table.find_all('tr'):
                #special format,it is a format table tr  -->th-->td
                ths = tr.find_all('th')
                for element1 in ths:
                    element = element1.get_text() #element1.text.encode(nation_language2)
                    if j%(field_num+1) == 0:
                        j = 1
                        #right??
                        #write.writerow( [ csv_string + "\n" ]  )   
                        fd.write( csv_string + "\n" )
                        stripped = ""
                        csv_string = ""
                       
                           
                    #all this replacing and striping is nessescary due to
                    #some trash in html table
                    if  element ==None:
                        pass
                    else:
                        stripped = element.replace("\n", "")
                        stripped = stripped.replace("\t", "")
                        stripped = stripped.replace("\xa0", " ")
                            
                        #getting rid of blank spaces
                        stripped = " ".join(stripped.split())
          
                    
                    if j == (field_num):
                        csv_string += stripped 
                    else:
                        csv_string += stripped + ","  
                    j = j + 1
                       
                   
                tds = tr.find_all('td')
                for element1 in tds:
                    element = element1.get_text() #element1.text.encode(nation_language2)
                    if j%(field_num+1) == 0:
                        j = 1
                        #right??
                        #write.writerow([ csv_string + "\n" ]  )
                        fd.write(  csv_string + "\n"  )
                        stripped = ""
                        csv_string = ""
                       
                           
                    #all this replacing and striping is nessescary due to
                    #some trash in html table
                    if  element ==None:
                        pass
                    else:
                        stripped = element.replace("\n", "")
                        stripped = stripped.replace("\t", "")
                        stripped = stripped.replace("\xa0", " ")
                            
                        #getting rid of blank spaces
                        stripped = " ".join(stripped.split())
          
                    if j == (field_num):
                        csv_string += stripped 
                    else:
                        csv_string += stripped + ","  
                    j = j + 1
########################################################
#             for element in table.get_text():
#                 #nessescary condition fo making new line in csv

#             #    
#             write.writerow(csv_string)    
            print('gen one csv succesfully')  
    

    print('finished one table processing')    
    
    
    
#define one method
def get_new_data( page_url, soup):
        title_node = soup.find('title')
        i =1
        table_node = soup.find_all('table')
        for table in table_node:
            print("scraping no."+str(i) +" .table ,and your required data should existed in some special index table:" )

            gen_csv_file(i,soup,table)
            i =i +1
            print("table scraping count :"+str(i)  )


#bs_html = BeautifulSoup(raw_html, 'html5lib')

get_new_data(url,bs_html)
print(" you SHOULD check the index of table and context,please choose the corresponding file." )


# #geting rows from html table
# rows = []
#  
# table = bs_html.find("table")
# for row in table.find_all('td'):
#     rows.append(row.getText())
# 
# 
# #clearing the file
# open('summary_table.csv', 'w').close()

