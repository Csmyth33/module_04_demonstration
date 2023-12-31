"""
Description: This program will provide salary increases of 20% to all 
executives at PiXELL-River Financial.  Prior to implementing this change, 
the program will see how many executives will end up with salaries greater than 
the high-salary mark.
Author: ACE Faculty
Edited by: Cooper Smyth
Date: Oct 10, 2023
Usage: 
"""
import logging


data = []
new_data = []

HIGH_SALARY = 120000
RECOMMENDED_INCREASE = 0.20

#set file to null (None is null in Python)
file = None

#LECTURE SECTION 1

logging.basicConfig(level = logging.DEBUG, 
                    filename = 'app.log', 
                    filemode = 'w', 
                    format = '%(asctime)s - %(levelname)s - %(message)s')

try:
      file = open('module_4_data.txt')
      data = file.readlines()

      1 / 0

      
      print("File Closed")
except FileNotFoundError as e:
      #print('File not found', e)
      logging.critical(e)
except Exception as e:
      #print('General exception:', e)
      logging.critical(e)
finally:
      if file is not None:
            file.close()
            print('Closed File.')


#LECTURE SECTION 2
try:
      # CEO/Chair of Board,Jo-Anne Sinclair,140000
      if len(data) == 0:
            raise Exception('No data exists.')
      else:
            for record in data:
                  items = record.split(',')
                  title = items[0]
                  name = items[1]
                  salary = float(items[2])
                  
                  #LECTURE SECTION 3
                  if salary > HIGH_SALARY:
                        logging.warning(f"{name}'s salary {salary}"
                                        + f"is currently above the "
                                        +f"recommended maximum of "
                                        +f"{HIGH_SALARY}.")
                  #REQUIREMENT:  NOTE RECORDS THAT EXCEED OR WILL EXCEED HIGH_SALARY AMOUNT
                  salary *= (1 + RECOMMENDED_INCREASE)
                  new_data.append([title,name,salary])
except Exception as e:
      #print(e)
      logging.critical(e)


#LECTURE SECTION 4
try:
      file = open('updated_salaries.txt', 'w')
      for record in new_data:
            row = ""
            for index, item in enumerate(record):
                  row += str(item)
                  if index < len(record) - 1:
                        row += (",")
            row += '\n'
            file.write(row)
except Exception as e:
      #print('Exception writing data', e)
      logging.critical(e)
#LECTURE SECTION 5
logging.debug('Debug level message')
logging.info('Info level message')
logging.warning('warning level message')
logging.error('Error level message')
logging.critical('critical level message')



print("End of Program")

