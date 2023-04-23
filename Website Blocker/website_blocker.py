import datetime
import time

end_time = datetime.datetime(2023,4,25)
site_block = ["www.cornhub.com", "www.fleXvideos.com"]
host_path = "Enter the path of hosts file present in drivers folder"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        print("Start Blocking")
        with open(host_path, "r+") as host_file:
            contents = host_file.read()
            for website in site_block:
                if website not in contents:
                    host_file.write(redirect + " " + website + "\n")
                else:
                    pass

    else:
        with open(host_path, "r+") as host_file:
            contents = host_file.readlines()
            host_file.seek(0)
            for lines in contents:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            
            host_file.truncate() 

        time.sleep(5)




