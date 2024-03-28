
class fileHandling:
    
    def __init__(self,file):
        self.file = file;

    ## This function is to create a new data entry into a file
    def newDataEntryToFile(self): 
        
        item=[];  

        while True:   
            user=input("\n Enter data into the file? (y/n) : ")
            item.append(user);

            if user.casefold() == 'n':
                break;
        userIput= '\n'.join(item);
        try:
            with open(self.file, 'w') as myfile:
                myfile.writelines(userIput);
        except Exception:
            print("There is a problem with your file")
    
    ## This function is to add more data to an exisiting data in a file       
    def AddingDataToFileContent(self): 

        item=[];  
        while True:   
            user=input("\n Enter data into the file? (y/n) : ")
            item.append(user);

            if user.casefold() == 'n':
                break;
        userIput= '\n'.join(item);

        try:
            with open(self.file, 'a') as myfile:
                myfile.writelines(userIput);
        except Exception:
            print("There is a problem with your file")

    ## This function is to display the content of a file
    def displayFileContent(self): 
        try:  
            with open(self.file, 'r') as myfile:
                content=myfile.readlines();
        except Exception:
            print("There is a problem with your file")
            
        for i in content[:-1]:
            print(i.strip('\n'));

            
file='my_file.txt';
p = fileHandling(file);
#p.newDataEntryToFile()
p.AddingDataToFileContent()
p.displayFileContent()

