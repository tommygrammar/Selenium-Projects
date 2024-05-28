from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from threading import  *

username_shark = "your email"
password_shark = "your password"

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, executable_path=r"your chromedriver path")

 #login webpage
driver.get("https://essayshark.com/")

def first_thread():


    button = driver.find_element(By.CLASS_NAME, "bb-accountContainer").click()


    #getlogin form
    login_form = driver.find_element(By.CLASS_NAME, "bb-authForm")

    #get login username input field and fill it
    login_field = login_form.find_element(By.CLASS_NAME, "bb-loginField")
    login_name = login_field.find_element(By.TAG_NAME, "input").send_keys(username_shark)


    #get login password input  field and fill it 
    password_field = login_form.find_element(By.CLASS_NAME, "bb-passwordField")
    login_password = password_field.find_element(By.TAG_NAME, "input").send_keys(password_shark)



    ##get  login button
    login_form = driver.find_element(By.CLASS_NAME, "bb-authForm")
    login_button = login_form.find_element(By.CLASS_NAME, "bb-button").click()


    ##applied field button
    WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.ID, 'available_tab')))

    #go to the available orders tab
    driver.get("https://essayshark.com/writer/orders/")


    while 1:


        available_orders_big_table = driver.find_element(By.ID, "available_orders")
        table = available_orders_big_table.find_element(By.CLASS_NAME, "table_orders")

        #look for the order table which holds the available order
        WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[10]")))

        trclass = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[10]")
        #acquire the available order id
        WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[10]/td[2]/a")))
        linko = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[10]/td[2]/a")
 

        #what is the writer's budget
        total_budget = float(((driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[10]/td[6]/span[2]")).text))


        try:
            try:
                pages_div = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[10]/td[4]")
             

                total_pages = int(pages_div.get_attribute("innerHTML")[1:2])
                        #open link in new tab
                driver.get(linko.get_attribute("href"))

                #get the recommended bid amount
                total_lowest_bid = total_budget/total_pages

                try:
                    bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                    bid_number = bid_input.find_element(By.ID, "id_bid").send_keys(total_lowest_bid)

                   

                    def apply_order_button():

                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))

                        
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        if tready == None:
                            while tready == None:
                                tready = apply_button.get_attribute("disabled")
                                if tready == "true":
                                    apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                    ready = apply_button.get_attribute("disabled")
                                    while ready == "true":
                                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                        ready = apply_button.get_attribute("disabled")
                                        if ready == None :
                                            apply_button.click()

                        elif tready == "true":
                            ready = apply_button.get_attribute("disabled")
                            while ready == "true":
                                apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                ready = apply_button.get_attribute("disabled")
                                if ready == None :
                                    apply_button.click()


                    def no_wait_apply_button():
                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                        apply_button.click()


                    time.sleep(1)
                    #confirming if instruction's box is there
                    if (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == True:
                    
                        #check for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")

                                                                                    

                                                                                    
                            p = 0
                            

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0                                                         
                                
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                                                                                    
                                                                                                
                                    p=0
                                   
                                except NoSuchElementException:
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                                                                                        
                                                                                                    
                                        p=0
                                       
                                    except NoSuchElementException:

                                        p = 1
                                        
                                    
                                    

                            





                        if p == 0:
                            ##check for download divs cos download containers have been found
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                              

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                               
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                                #check for download links because download divs have been found. Uses no wait button cos no instuction box exists
                            if z == 0:
                               
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                  
                                    no_wait_apply_button()
                                 



                                except NoSuchElementException:
                                    y = 1
                             
                                    
                                    if y == 1:
                                      
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                    
                                            download_link_two.click()
                                            z=0
                                         

                                            no_wait_apply_button()
                                           


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                                
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                  
                                                    download_link_three.click()
                                                    a = 0
                                                  

                                                    no_wait_apply_button()
                                     


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                     
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                       
                                                            download_link_four.click()
                                                      

                                                            no_wait_apply_button()
                                                        


                                                        except NoSuchElementException:

                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                               
                                                                download_link_five.click()
                                                            
                                                                

                                                                no_wait_apply_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                no_wait_apply_button()
                                                             

                                        
                        #since there is no wait button and no instructions box. Simply click
                        elif p == 1:
                         
                            no_wait_apply_button()
                         



                        driver.get("https://essayshark.com/writer/orders/")


                    ##this means that the instruction box its true
                    elif (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == False:
                        


                        #checing for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")
                                                                                            
                                                                                    
                            p = 0
                           

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0
                              
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                    p=0
                                  
                                except NoSuchElementException:
                                    p = 1
                                   
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                        p=0
                                      
                                    except NoSuchElementException:
                                        p = 1
                                        
                                    
                                    

                            





                        if p == 0:
                            ##looking for button to use
                            #download containers foun. Looking for the download div
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                  
                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                 
                                except NoSuchElementException:
                                        try:
                                            paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                            z = 0                                       
                                      
                                        except NoSuchElementException:
                                       
                                            z = 1
                                  
                                        apply_order_button()
                                        z = 1

                            if z == 0:
                               
                                #download div found, looking for the download links
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                
                                    apply_order_button()
                                   



                                except NoSuchElementException:
                                    y = 1
                                    
                                    
                                    if y == 1:
                                     
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                          
                                            download_link_two.click()
                                            z=0
                                          

                                            apply_order_button()
                                           


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                             
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                
                                                    download_link_three.click()
                                                    a = 0
                                                  

                                                    apply_order_button()
                                                  


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                       
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                              
                                                            download_link_four.click()
                                                         
                                                            

                                                            apply_order_button()
                                                        


                                                        except NoSuchElementException:
                                                           
                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                               
                                                                download_link_five.click()
                                                            
                                                                

                                                                apply_order_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                apply_order_button()
                                                           
                                                        

                                        
                        #no downoad containers were found and the instruction box was present. So wait before clicking
                        elif p == 1:
                        
                            apply_order_button()
                         



                        driver.get("https://essayshark.com/writer/orders/")


                except NoSuchElementException:
                    driver.get("https://essayshark.com/writer/orders/")


            
            except ValueError:
        #get the recommended bid amount
                driver.get(linko.get_attribute("href"))
                recommended_bid = driver.find_element(By.ID, "rec_bid")
                recommended_amount = recommended_bid.find_element(By.ID, "rec_amount")
                float_recommended_amount =  float(recommended_amount.text)
                total_recomended_amount =  float_recommended_amount

                #send the recommended bid amount to its input field
                bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                bid_number = bid_input.find_element(By.ID, "id_bid")
                bid_number.send_keys(total_recomended_amount)

                try:
                    bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                    bid_number = bid_input.find_element(By.ID, "id_bid").send_keys(total_recomended_amount)

                

                    def apply_order_button():

                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))

                        
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        if tready == None:
                            while tready == None:
                                tready = apply_button.get_attribute("disabled")
                                if tready == "true":
                                    apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                    ready = apply_button.get_attribute("disabled")
                                    while ready == "true":
                                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                        ready = apply_button.get_attribute("disabled")
                                        if ready == None :
                                            apply_button.click()

                        elif tready == "true":
                            ready = apply_button.get_attribute("disabled")
                            while ready == "true":
                                apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                ready = apply_button.get_attribute("disabled")
                                if ready == None :
                                    apply_button.click()


                    def no_wait_apply_button():
                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                        apply_button.click()


                    time.sleep(1)
                    #confirming if instruction's box is there
                    if (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == True:
              
                        #check for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")

                                                                                    

                                                                                    
                            p = 0
                           

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0                                                         
                               
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                                                                                    
                                                                                                
                                    p=0
                                   
                                except NoSuchElementException:
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                                                                                        
                                                                                                    
                                        p=0
                                       
                                    except NoSuchElementException:

                                        p = 1
                                       
                                    
                                    

                            





                        if p == 0:
                            ##check for download divs cos download containers have been found
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                               

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                  
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                                #check for download links because download divs have been found. Uses no wait button cos no instuction box exists
                            if z == 0:
                             
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                  
                                    no_wait_apply_button()
                                  



                                except NoSuchElementException:
                                    y = 1
                                    
                                    
                                    if y == 1:
                                       
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                           
                                            download_link_two.click()
                                            z=0
                              

                                            no_wait_apply_button()
                                           

                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                                
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                              
                                                    download_link_three.click()
                                                    a = 0
                                                   

                                                    no_wait_apply_button()
                                               


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                        
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                         
                                                            download_link_four.click()
                                                           

                                                            no_wait_apply_button()
                                                          

                                                        except NoSuchElementException:

                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                                   
                                                                download_link_five.click()
                                                              
                                                                

                                                                no_wait_apply_button()
                                                              


                                                            except NoSuchElementException:
                                                                
                                                                no_wait_apply_button()
                                                           
                                                        

                                        
                        #since there is no wait button and no instructions box. Simply click
                        elif p == 1:
                          
                            no_wait_apply_button()
                          



                        driver.get("https://essayshark.com/writer/orders/")


                    ##this means that the instruction box its true
                    elif (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == False:

                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")
                                                                                            
                                                                                    
                            p = 0
                          

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0
                             
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                    p=0
                                  
                                except NoSuchElementException:
                                    p = 1
                                  
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                        p=0
                                       
                                    except NoSuchElementException:
                                        p = 1
                                       
                                    
                                    

                            





                        if p == 0:
                            ##looking for button to use
                            #download containers foun. Looking for the download div
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                               

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                   
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                               
                                        apply_order_button()
                                       

                            if z == 0:
                               
                                #download div found, looking for the download links
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                   
                                    apply_order_button()
                               


                                except NoSuchElementException:
                                    y = 1
                                  
                                    
                                    if y == 1:
                                    
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                            
                                            download_link_two.click()
                                            z=0
                                            

                                            apply_order_button()
                                          


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                               
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                    
                                                    download_link_three.click()
                                                    a = 0
                                                 

                                                    apply_order_button()
                                                 


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                               
                                                        try:
                                                            
                                                            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]").click()
                                                                            
                                                           
                                                            
                                                            

                                                            apply_order_button()
                                                          


                                                        except NoSuchElementException:
                                                            
                                                            try:
                                                            
                                                                driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a").click()
                                                                               
                                                               
                                                            
                                                                

                                                                apply_order_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                apply_order_button()
                                                            
                                                        

                                        
                        #no downoad containers were found and the instruction box was present. So wait before clicking
                        elif p == 1:
                           
                            apply_order_button()
                           



                        driver.get("https://essayshark.com/writer/orders/")


                except NoSuchElementException:
                    driver.get("https://essayshark.com/writer/orders/")
        except StaleElementReferenceException:
            driver.get("https://essayshark.com/writer/orders/")


def second_thread():

    button = driver.find_element(By.CLASS_NAME, "bb-accountContainer").click()


    #getlogin form
    login_form = driver.find_element(By.CLASS_NAME, "bb-authForm")

    #get login username input field and fill it
    login_field = login_form.find_element(By.CLASS_NAME, "bb-loginField")
    login_name = login_field.find_element(By.TAG_NAME, "input").send_keys(username_shark)


    #get login password input  field and fill it 
    password_field = login_form.find_element(By.CLASS_NAME, "bb-passwordField")
    login_password = password_field.find_element(By.TAG_NAME, "input").send_keys(password_shark)



    ##get  login button
    login_form = driver.find_element(By.CLASS_NAME, "bb-authForm")
    login_button = login_form.find_element(By.CLASS_NAME, "bb-button").click()


    ##applied field button
    WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.ID, 'available_tab')))

    #go to the available orders tab
    driver.get("https://essayshark.com/writer/orders/")


    while 1:


        available_orders_big_table = driver.find_element(By.ID, "available_orders")
        table = available_orders_big_table.find_element(By.CLASS_NAME, "table_orders")

        #look for the order table which holds the available order
        WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[11]")))

        trclass = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[11]")
        #acquire the available order id
        WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[11]/td[2]/a")))
        linko = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[11]/td[2]/a")
 

        #what is the writer's budget
        total_budget = float(((driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[11]/td[6]/span[2]")).text))


        try:
            try:
                pages_div = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[11]/td[4]")
             

                total_pages = int(pages_div.get_attribute("innerHTML")[1:2])
                        #open link in new tab
                driver.get(linko.get_attribute("href"))

                #get the recommended bid amount
                total_lowest_bid = total_budget/total_pages

                try:
                    bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                    bid_number = bid_input.find_element(By.ID, "id_bid").send_keys(total_lowest_bid)

                   

                    def apply_order_button():

                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))

                        
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        if tready == None:
                            while tready == None:
                                tready = apply_button.get_attribute("disabled")
                                if tready == "true":
                                    apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                    ready = apply_button.get_attribute("disabled")
                                    while ready == "true":
                                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                        ready = apply_button.get_attribute("disabled")
                                        if ready == None :
                                            apply_button.click()

                        elif tready == "true":
                            ready = apply_button.get_attribute("disabled")
                            while ready == "true":
                                apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                ready = apply_button.get_attribute("disabled")
                                if ready == None :
                                    apply_button.click()


                    def no_wait_apply_button():
                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                        apply_button.click()


                    time.sleep(1)
                    #confirming if instruction's box is there
                    if (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == True:
                    
                        #check for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")

                                                                                    

                                                                                    
                            p = 0
                            

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0                                                         
                                
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                                                                                    
                                                                                                
                                    p=0
                                   
                                except NoSuchElementException:
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                                                                                        
                                                                                                    
                                        p=0
                                       
                                    except NoSuchElementException:

                                        p = 1
                                        
                                    
                                    

                            





                        if p == 0:
                            ##check for download divs cos download containers have been found
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                              

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                               
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                                #check for download links because download divs have been found. Uses no wait button cos no instuction box exists
                            if z == 0:
                               
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                  
                                    no_wait_apply_button()
                                 



                                except NoSuchElementException:
                                    y = 1
                             
                                    
                                    if y == 1:
                                      
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                    
                                            download_link_two.click()
                                            z=0
                                         

                                            no_wait_apply_button()
                                           


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                                
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                  
                                                    download_link_three.click()
                                                    a = 0
                                                  

                                                    no_wait_apply_button()
                                     


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                     
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                       
                                                            download_link_four.click()
                                                      

                                                            no_wait_apply_button()
                                                        


                                                        except NoSuchElementException:

                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                               
                                                                download_link_five.click()
                                                            
                                                                

                                                                no_wait_apply_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                no_wait_apply_button()
                                                             

                                        
                        #since there is no wait button and no instructions box. Simply click
                        elif p == 1:
                         
                            no_wait_apply_button()
                         



                        driver.get("https://essayshark.com/writer/orders/")


                    ##this means that the instruction box its true
                    elif (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == False:
                        


                        #checing for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")
                                                                                            
                                                                                    
                            p = 0
                           

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0
                              
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                    p=0
                                  
                                except NoSuchElementException:
                                    p = 1
                                   
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                        p=0
                                      
                                    except NoSuchElementException:
                                        p = 1
                                        
                                    
                                    

                            





                        if p == 0:
                            ##looking for button to use
                            #download containers foun. Looking for the download div
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                  
                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                 
                                except NoSuchElementException:
                                        try:
                                            paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                            z = 0                                       
                                      
                                        except NoSuchElementException:
                                       
                                            z = 1
                                  
                                        apply_order_button()
                                        z = 1

                            if z == 0:
                               
                                #download div found, looking for the download links
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                
                                    apply_order_button()
                                   



                                except NoSuchElementException:
                                    y = 1
                                    
                                    
                                    if y == 1:
                                     
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                          
                                            download_link_two.click()
                                            z=0
                                          

                                            apply_order_button()
                                           


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                             
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                
                                                    download_link_three.click()
                                                    a = 0
                                                  

                                                    apply_order_button()
                                                  


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                       
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                              
                                                            download_link_four.click()
                                                         
                                                            

                                                            apply_order_button()
                                                        


                                                        except NoSuchElementException:
                                                           
                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                               
                                                                download_link_five.click()
                                                            
                                                                

                                                                apply_order_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                apply_order_button()
                                                           
                                                        

                                        
                        #no downoad containers were found and the instruction box was present. So wait before clicking
                        elif p == 1:
                        
                            apply_order_button()
                         



                        driver.get("https://essayshark.com/writer/orders/")


                except NoSuchElementException:
                    driver.get("https://essayshark.com/writer/orders/")


            
            except ValueError:
        #get the recommended bid amount
                driver.get(linko.get_attribute("href"))
                recommended_bid = driver.find_element(By.ID, "rec_bid")
                recommended_amount = recommended_bid.find_element(By.ID, "rec_amount")
                float_recommended_amount =  float(recommended_amount.text)
                total_recomended_amount =  float_recommended_amount

                #send the recommended bid amount to its input field
                bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                bid_number = bid_input.find_element(By.ID, "id_bid")
                bid_number.send_keys(total_recomended_amount)

                try:
                    bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                    bid_number = bid_input.find_element(By.ID, "id_bid").send_keys(total_recomended_amount)

                

                    def apply_order_button():

                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))

                        
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        if tready == None:
                            while tready == None:
                                tready = apply_button.get_attribute("disabled")
                                if tready == "true":
                                    apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                    ready = apply_button.get_attribute("disabled")
                                    while ready == "true":
                                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                        ready = apply_button.get_attribute("disabled")
                                        if ready == None :
                                            apply_button.click()

                        elif tready == "true":
                            ready = apply_button.get_attribute("disabled")
                            while ready == "true":
                                apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                ready = apply_button.get_attribute("disabled")
                                if ready == None :
                                    apply_button.click()


                    def no_wait_apply_button():
                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                        apply_button.click()


                    time.sleep(1)
                    #confirming if instruction's box is there
                    if (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == True:
              
                        #check for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")

                                                                                    

                                                                                    
                            p = 0
                           

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0                                                         
                               
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                                                                                    
                                                                                                
                                    p=0
                                   
                                except NoSuchElementException:
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                                                                                        
                                                                                                    
                                        p=0
                                       
                                    except NoSuchElementException:

                                        p = 1
                                       
                                    
                                    

                            





                        if p == 0:
                            ##check for download divs cos download containers have been found
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                               

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                  
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                                #check for download links because download divs have been found. Uses no wait button cos no instuction box exists
                            if z == 0:
                             
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                  
                                    no_wait_apply_button()
                                  



                                except NoSuchElementException:
                                    y = 1
                                    
                                    
                                    if y == 1:
                                       
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                           
                                            download_link_two.click()
                                            z=0
                              

                                            no_wait_apply_button()
                                           

                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                                
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                              
                                                    download_link_three.click()
                                                    a = 0
                                                   

                                                    no_wait_apply_button()
                                               


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                        
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                         
                                                            download_link_four.click()
                                                           

                                                            no_wait_apply_button()
                                                          

                                                        except NoSuchElementException:

                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                                   
                                                                download_link_five.click()
                                                              
                                                                

                                                                no_wait_apply_button()
                                                              


                                                            except NoSuchElementException:
                                                                
                                                                no_wait_apply_button()
                                                           
                                                        

                                        
                        #since there is no wait button and no instructions box. Simply click
                        elif p == 1:
                          
                            no_wait_apply_button()
                          



                        driver.get("https://essayshark.com/writer/orders/")


                    ##this means that the instruction box its true
                    elif (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == False:

                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")
                                                                                            
                                                                                    
                            p = 0
                          

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0
                             
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                    p=0
                                  
                                except NoSuchElementException:
                                    p = 1
                                  
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                        p=0
                                       
                                    except NoSuchElementException:
                                        p = 1
                                       
                                    
                                    

                            





                        if p == 0:
                            ##looking for button to use
                            #download containers foun. Looking for the download div
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                               

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                   
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                               
                                        apply_order_button()
                                       

                            if z == 0:
                               
                                #download div found, looking for the download links
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                   
                                    apply_order_button()
                               


                                except NoSuchElementException:
                                    y = 1
                                  
                                    
                                    if y == 1:
                                    
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                            
                                            download_link_two.click()
                                            z=0
                                            

                                            apply_order_button()
                                          


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                               
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                    
                                                    download_link_three.click()
                                                    a = 0
                                                 

                                                    apply_order_button()
                                                 


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                               
                                                        try:
                                                            
                                                            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]").click()
                                                                            
                                                           
                                                            
                                                            

                                                            apply_order_button()
                                                          


                                                        except NoSuchElementException:
                                                            
                                                            try:
                                                            
                                                                driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a").click()
                                                                               
                                                               
                                                            
                                                                

                                                                apply_order_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                apply_order_button()
                                                            
                                                        

                                        
                        #no downoad containers were found and the instruction box was present. So wait before clicking
                        elif p == 1:
                           
                            apply_order_button()
                           



                        driver.get("https://essayshark.com/writer/orders/")


                except NoSuchElementException:
                    driver.get("https://essayshark.com/writer/orders/")
        except StaleElementReferenceException:
            driver.get("https://essayshark.com/writer/orders/")

def third_thread():

    button = driver.find_element(By.CLASS_NAME, "bb-accountContainer").click()


    #getlogin form
    login_form = driver.find_element(By.CLASS_NAME, "bb-authForm")

    #get login username input field and fill it
    login_field = login_form.find_element(By.CLASS_NAME, "bb-loginField")
    login_name = login_field.find_element(By.TAG_NAME, "input").send_keys(username_shark)


    #get login password input  field and fill it 
    password_field = login_form.find_element(By.CLASS_NAME, "bb-passwordField")
    login_password = password_field.find_element(By.TAG_NAME, "input").send_keys(password_shark)



    ##get  login button
    login_form = driver.find_element(By.CLASS_NAME, "bb-authForm")
    login_button = login_form.find_element(By.CLASS_NAME, "bb-button").click()


    ##applied field button
    WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.ID, 'available_tab')))

    #go to the available orders tab
    driver.get("https://essayshark.com/writer/orders/")


    while 1:


        available_orders_big_table = driver.find_element(By.ID, "available_orders")
        table = available_orders_big_table.find_element(By.CLASS_NAME, "table_orders")

        #look for the order table which holds the available order
        WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[12]")))

        trclass = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[12]")
        #acquire the available order id
        WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[12]/td[2]/a")))
        linko = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[12]/td[2]/a")
 

        #what is the writer's budget
        total_budget = float(((driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[12]/td[6]/span[2]")).text))


        try:
            try:
                pages_div = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[12]/td[4]")
             

                total_pages = int(pages_div.get_attribute("innerHTML")[1:2])
                        #open link in new tab
                driver.get(linko.get_attribute("href"))

                #get the recommended bid amount
                total_lowest_bid = total_budget/total_pages

                try:
                    bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                    bid_number = bid_input.find_element(By.ID, "id_bid").send_keys(total_lowest_bid)

                   

                    def apply_order_button():

                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))

                        
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        if tready == None:
                            while tready == None:
                                tready = apply_button.get_attribute("disabled")
                                if tready == "true":
                                    apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                    ready = apply_button.get_attribute("disabled")
                                    while ready == "true":
                                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                        ready = apply_button.get_attribute("disabled")
                                        if ready == None :
                                            apply_button.click()

                        elif tready == "true":
                            ready = apply_button.get_attribute("disabled")
                            while ready == "true":
                                apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                ready = apply_button.get_attribute("disabled")
                                if ready == None :
                                    apply_button.click()


                    def no_wait_apply_button():
                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                        apply_button.click()


                    time.sleep(1)
                    #confirming if instruction's box is there
                    if (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == True:
                    
                        #check for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")

                                                                                    

                                                                                    
                            p = 0
                            

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0                                                         
                                
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                                                                                    
                                                                                                
                                    p=0
                                   
                                except NoSuchElementException:
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                                                                                        
                                                                                                    
                                        p=0
                                       
                                    except NoSuchElementException:

                                        p = 1
                                        
                                    
                                    

                            





                        if p == 0:
                            ##check for download divs cos download containers have been found
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                              

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                               
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                                #check for download links because download divs have been found. Uses no wait button cos no instuction box exists
                            if z == 0:
                               
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                  
                                    no_wait_apply_button()
                                 



                                except NoSuchElementException:
                                    y = 1
                             
                                    
                                    if y == 1:
                                      
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                    
                                            download_link_two.click()
                                            z=0
                                         

                                            no_wait_apply_button()
                                           


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                                
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                  
                                                    download_link_three.click()
                                                    a = 0
                                                  

                                                    no_wait_apply_button()
                                     


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                     
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                       
                                                            download_link_four.click()
                                                      

                                                            no_wait_apply_button()
                                                        


                                                        except NoSuchElementException:

                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                               
                                                                download_link_five.click()
                                                            
                                                                

                                                                no_wait_apply_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                no_wait_apply_button()
                                                             

                                        
                        #since there is no wait button and no instructions box. Simply click
                        elif p == 1:
                         
                            no_wait_apply_button()
                         



                        driver.get("https://essayshark.com/writer/orders/")


                    ##this means that the instruction box its true
                    elif (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == False:
                        


                        #checing for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")
                                                                                            
                                                                                    
                            p = 0
                           

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0
                              
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                    p=0
                                  
                                except NoSuchElementException:
                                    p = 1
                                   
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                        p=0
                                      
                                    except NoSuchElementException:
                                        p = 1
                                        
                                    
                                    

                            





                        if p == 0:
                            ##looking for button to use
                            #download containers foun. Looking for the download div
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                  
                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                 
                                except NoSuchElementException:
                                        try:
                                            paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                            z = 0                                       
                                      
                                        except NoSuchElementException:
                                       
                                            z = 1
                                  
                                        apply_order_button()
                                        z = 1

                            if z == 0:
                               
                                #download div found, looking for the download links
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                
                                    apply_order_button()
                                   



                                except NoSuchElementException:
                                    y = 1
                                    
                                    
                                    if y == 1:
                                     
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                          
                                            download_link_two.click()
                                            z=0
                                          

                                            apply_order_button()
                                           


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                             
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                
                                                    download_link_three.click()
                                                    a = 0
                                                  

                                                    apply_order_button()
                                                  


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                       
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                              
                                                            download_link_four.click()
                                                         
                                                            

                                                            apply_order_button()
                                                        


                                                        except NoSuchElementException:
                                                           
                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                               
                                                                download_link_five.click()
                                                            
                                                                

                                                                apply_order_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                apply_order_button()
                                                           
                                                        

                                        
                        #no downoad containers were found and the instruction box was present. So wait before clicking
                        elif p == 1:
                        
                            apply_order_button()
                         



                        driver.get("https://essayshark.com/writer/orders/")


                except NoSuchElementException:
                    driver.get("https://essayshark.com/writer/orders/")


            
            except ValueError:
        #get the recommended bid amount
                driver.get(linko.get_attribute("href"))
                recommended_bid = driver.find_element(By.ID, "rec_bid")
                recommended_amount = recommended_bid.find_element(By.ID, "rec_amount")
                float_recommended_amount =  float(recommended_amount.text)
                total_recomended_amount =  float_recommended_amount

                #send the recommended bid amount to its input field
                bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                bid_number = bid_input.find_element(By.ID, "id_bid")
                bid_number.send_keys(total_recomended_amount)

                try:
                    bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                    bid_number = bid_input.find_element(By.ID, "id_bid").send_keys(total_recomended_amount)

                

                    def apply_order_button():

                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))

                        
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        if tready == None:
                            while tready == None:
                                tready = apply_button.get_attribute("disabled")
                                if tready == "true":
                                    apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                    ready = apply_button.get_attribute("disabled")
                                    while ready == "true":
                                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                        ready = apply_button.get_attribute("disabled")
                                        if ready == None :
                                            apply_button.click()

                        elif tready == "true":
                            ready = apply_button.get_attribute("disabled")
                            while ready == "true":
                                apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                ready = apply_button.get_attribute("disabled")
                                if ready == None :
                                    apply_button.click()


                    def no_wait_apply_button():
                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                        apply_button.click()


                    time.sleep(1)
                    #confirming if instruction's box is there
                    if (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == True:
              
                        #check for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")

                                                                                    

                                                                                    
                            p = 0
                           

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0                                                         
                               
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                                                                                    
                                                                                                
                                    p=0
                                   
                                except NoSuchElementException:
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                                                                                        
                                                                                                    
                                        p=0
                                       
                                    except NoSuchElementException:

                                        p = 1
                                       
                                    
                                    

                            





                        if p == 0:
                            ##check for download divs cos download containers have been found
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                               

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                  
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                                #check for download links because download divs have been found. Uses no wait button cos no instuction box exists
                            if z == 0:
                             
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                  
                                    no_wait_apply_button()
                                  



                                except NoSuchElementException:
                                    y = 1
                                    
                                    
                                    if y == 1:
                                       
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                           
                                            download_link_two.click()
                                            z=0
                              

                                            no_wait_apply_button()
                                           

                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                                
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                              
                                                    download_link_three.click()
                                                    a = 0
                                                   

                                                    no_wait_apply_button()
                                               


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                        
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                         
                                                            download_link_four.click()
                                                           

                                                            no_wait_apply_button()
                                                          

                                                        except NoSuchElementException:

                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                                   
                                                                download_link_five.click()
                                                              
                                                                

                                                                no_wait_apply_button()
                                                              


                                                            except NoSuchElementException:
                                                                
                                                                no_wait_apply_button()
                                                           
                                                        

                                        
                        #since there is no wait button and no instructions box. Simply click
                        elif p == 1:
                          
                            no_wait_apply_button()
                          



                        driver.get("https://essayshark.com/writer/orders/")


                    ##this means that the instruction box its true
                    elif (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == False:

                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")
                                                                                            
                                                                                    
                            p = 0
                          

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0
                             
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                    p=0
                                  
                                except NoSuchElementException:
                                    p = 1
                                  
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                        p=0
                                       
                                    except NoSuchElementException:
                                        p = 1
                                       
                                    
                                    

                            





                        if p == 0:
                            ##looking for button to use
                            #download containers foun. Looking for the download div
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                               

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                   
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                               
                                        apply_order_button()
                                       

                            if z == 0:
                               
                                #download div found, looking for the download links
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                   
                                    apply_order_button()
                               


                                except NoSuchElementException:
                                    y = 1
                                  
                                    
                                    if y == 1:
                                    
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                            
                                            download_link_two.click()
                                            z=0
                                            

                                            apply_order_button()
                                          


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                               
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                    
                                                    download_link_three.click()
                                                    a = 0
                                                 

                                                    apply_order_button()
                                                 


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                               
                                                        try:
                                                            
                                                            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]").click()
                                                                            
                                                           
                                                            
                                                            

                                                            apply_order_button()
                                                          


                                                        except NoSuchElementException:
                                                            
                                                            try:
                                                            
                                                                driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a").click()
                                                                               
                                                               
                                                            
                                                                

                                                                apply_order_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                apply_order_button()
                                                            
                                                        

                                        
                        #no downoad containers were found and the instruction box was present. So wait before clicking
                        elif p == 1:
                           
                            apply_order_button()
                           



                        driver.get("https://essayshark.com/writer/orders/")


                except NoSuchElementException:
                    driver.get("https://essayshark.com/writer/orders/")
        except StaleElementReferenceException:
            driver.get("https://essayshark.com/writer/orders/")

def fourth_thread():

    button = driver.find_element(By.CLASS_NAME, "bb-accountContainer").click()


    #getlogin form
    login_form = driver.find_element(By.CLASS_NAME, "bb-authForm")

    #get login username input field and fill it
    login_field = login_form.find_element(By.CLASS_NAME, "bb-loginField")
    login_name = login_field.find_element(By.TAG_NAME, "input").send_keys(username_shark)


    #get login password input  field and fill it 
    password_field = login_form.find_element(By.CLASS_NAME, "bb-passwordField")
    login_password = password_field.find_element(By.TAG_NAME, "input").send_keys(password_shark)



    ##get  login button
    login_form = driver.find_element(By.CLASS_NAME, "bb-authForm")
    login_button = login_form.find_element(By.CLASS_NAME, "bb-button").click()


    ##applied field button
    WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.ID, 'available_tab')))

    #go to the available orders tab
    driver.get("https://essayshark.com/writer/orders/")


    while 1:


        available_orders_big_table = driver.find_element(By.ID, "available_orders")
        table = available_orders_big_table.find_element(By.CLASS_NAME, "table_orders")

        #look for the order table which holds the available order
        WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[13]")))

        trclass = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[13]")
        #acquire the available order id
        WebDriverWait(driver, 100000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[13]/td[2]/a")))
        linko = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[13]/td[2]/a")
 

        #what is the writer's budget
        total_budget = float(((driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[13]/td[6]/span[2]")).text))


        try:
            try:
                pages_div = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[5]/div/div[2]/table/tbody/tr[13]/td[4]")
             

                total_pages = int(pages_div.get_attribute("innerHTML")[1:2])
                        #open link in new tab
                driver.get(linko.get_attribute("href"))

                #get the recommended bid amount
                total_lowest_bid = total_budget/total_pages

                try:
                    bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                    bid_number = bid_input.find_element(By.ID, "id_bid").send_keys(total_lowest_bid)

                   

                    def apply_order_button():

                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))

                        
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        if tready == None:
                            while tready == None:
                                tready = apply_button.get_attribute("disabled")
                                if tready == "true":
                                    apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                    ready = apply_button.get_attribute("disabled")
                                    while ready == "true":
                                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                        ready = apply_button.get_attribute("disabled")
                                        if ready == None :
                                            apply_button.click()

                        elif tready == "true":
                            ready = apply_button.get_attribute("disabled")
                            while ready == "true":
                                apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                ready = apply_button.get_attribute("disabled")
                                if ready == None :
                                    apply_button.click()


                    def no_wait_apply_button():
                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                        apply_button.click()


                    time.sleep(1)
                    #confirming if instruction's box is there
                    if (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == True:
                    
                        #check for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")

                                                                                    

                                                                                    
                            p = 0
                            

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0                                                         
                                
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                                                                                    
                                                                                                
                                    p=0
                                   
                                except NoSuchElementException:
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                                                                                        
                                                                                                    
                                        p=0
                                       
                                    except NoSuchElementException:

                                        p = 1
                                        
                                    
                                    

                            





                        if p == 0:
                            ##check for download divs cos download containers have been found
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                              

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                               
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                                #check for download links because download divs have been found. Uses no wait button cos no instuction box exists
                            if z == 0:
                               
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                  
                                    no_wait_apply_button()
                                 



                                except NoSuchElementException:
                                    y = 1
                             
                                    
                                    if y == 1:
                                      
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                    
                                            download_link_two.click()
                                            z=0
                                         

                                            no_wait_apply_button()
                                           


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                                
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                  
                                                    download_link_three.click()
                                                    a = 0
                                                  

                                                    no_wait_apply_button()
                                     


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                     
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                       
                                                            download_link_four.click()
                                                      

                                                            no_wait_apply_button()
                                                        


                                                        except NoSuchElementException:

                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                               
                                                                download_link_five.click()
                                                            
                                                                

                                                                no_wait_apply_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                no_wait_apply_button()
                                                             

                                        
                        #since there is no wait button and no instructions box. Simply click
                        elif p == 1:
                         
                            no_wait_apply_button()
                         



                        driver.get("https://essayshark.com/writer/orders/")


                    ##this means that the instruction box its true
                    elif (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == False:
                        


                        #checing for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")
                                                                                            
                                                                                    
                            p = 0
                           

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0
                              
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                    p=0
                                  
                                except NoSuchElementException:
                                    p = 1
                                   
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                        p=0
                                      
                                    except NoSuchElementException:
                                        p = 1
                                        
                                    
                                    

                            





                        if p == 0:
                            ##looking for button to use
                            #download containers foun. Looking for the download div
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                  
                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                 
                                except NoSuchElementException:
                                        try:
                                            paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                            z = 0                                       
                                      
                                        except NoSuchElementException:
                                       
                                            z = 1
                                  
                                        apply_order_button()
                                        z = 1

                            if z == 0:
                               
                                #download div found, looking for the download links
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                
                                    apply_order_button()
                                   



                                except NoSuchElementException:
                                    y = 1
                                    
                                    
                                    if y == 1:
                                     
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                          
                                            download_link_two.click()
                                            z=0
                                          

                                            apply_order_button()
                                           


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                             
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                
                                                    download_link_three.click()
                                                    a = 0
                                                  

                                                    apply_order_button()
                                                  


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                       
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                              
                                                            download_link_four.click()
                                                         
                                                            

                                                            apply_order_button()
                                                        


                                                        except NoSuchElementException:
                                                           
                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                               
                                                                download_link_five.click()
                                                            
                                                                

                                                                apply_order_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                apply_order_button()
                                                           
                                                        

                                        
                        #no downoad containers were found and the instruction box was present. So wait before clicking
                        elif p == 1:
                        
                            apply_order_button()
                         



                        driver.get("https://essayshark.com/writer/orders/")


                except NoSuchElementException:
                    driver.get("https://essayshark.com/writer/orders/")


            
            except ValueError:
        #get the recommended bid amount
                driver.get(linko.get_attribute("href"))
                recommended_bid = driver.find_element(By.ID, "rec_bid")
                recommended_amount = recommended_bid.find_element(By.ID, "rec_amount")
                float_recommended_amount =  float(recommended_amount.text)
                total_recomended_amount =  float_recommended_amount

                #send the recommended bid amount to its input field
                bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                bid_number = bid_input.find_element(By.ID, "id_bid")
                bid_number.send_keys(total_recomended_amount)

                try:
                    bid_input = driver.find_element(By.CLASS_NAME, "fortop")
                    bid_number = bid_input.find_element(By.ID, "id_bid").send_keys(total_recomended_amount)

                

                    def apply_order_button():

                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))

                        
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        tready = apply_button.get_attribute("disabled")
                        if tready == None:
                            while tready == None:
                                tready = apply_button.get_attribute("disabled")
                                if tready == "true":
                                    apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                    ready = apply_button.get_attribute("disabled")
                                    while ready == "true":
                                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                        ready = apply_button.get_attribute("disabled")
                                        if ready == None :
                                            apply_button.click()

                        elif tready == "true":
                            ready = apply_button.get_attribute("disabled")
                            while ready == "true":
                                apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                                ready = apply_button.get_attribute("disabled")
                                if ready == None :
                                    apply_button.click()


                    def no_wait_apply_button():
                        apply_button = (bid_input.find_element(By.CLASS_NAME, "btn_f_submit"))
                        apply_button.click()


                    time.sleep(1)
                    #confirming if instruction's box is there
                    if (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == True:
              
                        #check for download containers
                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")

                                                                                    

                                                                                    
                            p = 0
                           

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0                                                         
                               
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                                                                                    
                                                                                                
                                    p=0
                                   
                                except NoSuchElementException:
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                                                                                        
                                                                                                    
                                        p=0
                                       
                                    except NoSuchElementException:

                                        p = 1
                                       
                                    
                                    

                            





                        if p == 0:
                            ##check for download divs cos download containers have been found
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                               

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                  
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                                #check for download links because download divs have been found. Uses no wait button cos no instuction box exists
                            if z == 0:
                             
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                  
                                    no_wait_apply_button()
                                  



                                except NoSuchElementException:
                                    y = 1
                                    
                                    
                                    if y == 1:
                                       
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                           
                                            download_link_two.click()
                                            z=0
                              

                                            no_wait_apply_button()
                                           

                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                                
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                              
                                                    download_link_three.click()
                                                    a = 0
                                                   

                                                    no_wait_apply_button()
                                               


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                                        
                                                        try:
                                                            
                                                            download_link_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]")
                                                                         
                                                            download_link_four.click()
                                                           

                                                            no_wait_apply_button()
                                                          

                                                        except NoSuchElementException:

                                                            try:
                                                            
                                                                download_link_five = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a")
                                                                                   
                                                                download_link_five.click()
                                                              
                                                                

                                                                no_wait_apply_button()
                                                              


                                                            except NoSuchElementException:
                                                                
                                                                no_wait_apply_button()
                                                           
                                                        

                                        
                        #since there is no wait button and no instructions box. Simply click
                        elif p == 1:
                          
                            no_wait_apply_button()
                          



                        driver.get("https://essayshark.com/writer/orders/")


                    ##this means that the instruction box its true
                    elif (driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div").get_attribute("Style") == "display: none;") == False:

                        try:
                            main_download_container = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]")
                                                                                            
                                                                                    
                            p = 0
                          

                        except NoSuchElementException:
                            try:
                                main_download_container_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl[2]")
                                p=0
                             
                            except NoSuchElementException:

                                try:
                                    main_download_container_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl")
                                    p=0
                                  
                                except NoSuchElementException:
                                    p = 1
                                  
                                    try:
                                        main_download_container_four = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl")
                                        p=0
                                       
                                    except NoSuchElementException:
                                        p = 1
                                       
                                    
                                    

                            





                        if p == 0:
                            ##looking for button to use
                            #download containers foun. Looking for the download div
                            try:
                                
                                paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div" )                                           
                                z = 0                                      
                               

                            except NoSuchElementException:
                                try:
                                    paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div" )
                                    z = 0                                       
                                   
                                except NoSuchElementException:
                                    try:
                                        paper_inst = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div" )
                                        z = 0                                       
                                      
                                    except NoSuchElementException:
                                       
                                        z = 1
                               
                                        apply_order_button()
                                       

                            if z == 0:
                               
                                #download div found, looking for the download links
                                try:
                                    
                                    download_link_one = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a")
                                                                                        
                                    download_link_one.click()
                                    y = 0
                                   
                                    apply_order_button()
                               


                                except NoSuchElementException:
                                    y = 1
                                  
                                    
                                    if y == 1:
                                    
                                        try:
                                            
                                            download_link_two = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[3]/div[2]/div[2]/dl/dd/div/a[1]")
                                            
                                            download_link_two.click()
                                            z=0
                                            

                                            apply_order_button()
                                          


                                        except NoSuchElementException:
                                            z=1
                                            if z==1:
                                               
                                                try:
                                                    
                                                    download_link_three = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a")
                                                    
                                                    download_link_three.click()
                                                    a = 0
                                                 

                                                    apply_order_button()
                                                 


                                                except NoSuchElementException:
                                                    a=1
                                                    if a == 1:
                                               
                                                        try:
                                                            
                                                            driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl[2]/dd/div/a[1]").click()
                                                                            
                                                           
                                                            
                                                            

                                                            apply_order_button()
                                                          


                                                        except NoSuchElementException:
                                                            
                                                            try:
                                                            
                                                                driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[4]/div[2]/div[2]/dl/dd/div/a").click()
                                                                               
                                                               
                                                            
                                                                

                                                                apply_order_button()
                                                            


                                                            except NoSuchElementException:
                                                                
                                                                apply_order_button()
                                                            
                                                        

                                        
                        #no downoad containers were found and the instruction box was present. So wait before clicking
                        elif p == 1:
                           
                            apply_order_button()
                           



                        driver.get("https://essayshark.com/writer/orders/")


                except NoSuchElementException:
                    driver.get("https://essayshark.com/writer/orders/")
        except StaleElementReferenceException:
            driver.get("https://essayshark.com/writer/orders/")


first_thread()

order2 = Thread(target=second_thread)
order2.start()

order3 = Thread(target=third_thread)
order3.start()

order4 = Thread(target=fourth_thread)
order4.start()

