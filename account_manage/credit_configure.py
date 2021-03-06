import os

class configure:
    def __init__(self,input_command):
        self.command  = input_command
        self.commands = ["init","list"]
        self.ZONE= {"KOR-Central A":"1", "KOR-Central B":'2', "KOR-HA":'3', "KOR-Seoul M2":"4", "JPN":"5", "US-West":"6",}
        self.RESPONSE_TYPE=['json','xml']
    def configure_list(self):
        try:
            credit_file = open("credit.txt","r")
        except:
            print("no credit file detected \nplease type 'ucloud configure init' to create credit files")
            exit(-1)
        credit =[]
        for line in credit_file:
            credit.append(line)
        if(len(credit) <3):
            print("credit file is not completed \n type 'ucloudcli configure init' to complete credit first")
        print("API_KEY : ", credit[0])
        print("Secret Key : ", credit[1])
        print("Zone : ", credit[2])
        print("response Type: ", credit[3])
        return
    def configure_init(self):
        m2_zone = False
        apikey_in = input("[api_key] :")
        secret_in = input("[secret key} :")
        zone_in = input("[data center] or type 'help' to check all aviliable zones :")
        while(zone_in == 'help' or zone_in not in self.ZONE):
            for name in self.ZONE:
                print(name)
            zone_in = input("[data center] or type 'help' to check supported zones :")
    #    for i in ZONE:
    #        if(zone_in.lower() == i):
    #            zone_in=i
        response = input("[response type] or type 'help' to check supported response :")
        while(response == 'help' or response not in self.RESPONSE_TYPE):
            for name in self.RESPONSE_TYPE:
                print(name)
            response = input("[response type] or type 'help' to check supported response :")
        if zone_in == "KOR-Seoul M2":
            m2_zone = True
        t = open("credit.txt","w")
        t.write(apikey_in+"\n")
        #if(secret_in != ""):
        t.write(secret_in+"\n")
        t.write(zone_in+"\n")
        t.write(response+"\n")
        t.write(str(m2_zone)+ "\n")
        t.close()
        os.system("chmod u=rwx,g=rx,o= credit.txt")
        return


        
    def command_process_configure(self):
        command = self.command
        if command == "init":
            self.configure_init()
        elif command == "list":
            self.configure_list()
        elif command == "help":
            print("==========Supported configure commands==========")
            for i in self.commands:
                print("ucloud configure ",i)
            print("================================================")
        else:
            print("no command matched for "+"'ucloud configure"+command+"'"+ "\n" +"type 'ucloud configure help' to to view supported configure command'")
            exit(-1)
    
    ##def command_process_server(command):
    ##    if ctype == "List"
    ##        
    ##    elif ctype == "ListAvailableProductTypes":
    ##        ListAvailableProductTypes()
    ##    elif ctype == "deployVirtualMachnine":
    ##        deployVirtualMachine()
    ##    elif ctype == "startVirtualMachine" :
    ##        startVirutualMachine()
    ##    else:
    ##        print("no command matched")

