
          _        _______  _______    ______   _______  _______ _________ _______  _        _______  _______ 
|\     /|( \      (  ____ \(       )  (  __  \ (  ____ \(  ____ \\__   __/(  ____ \( (    /|(  ____ \(  ____ )
| )   ( || (      | (    \/| () () |  | (  \  )| (    \/| (    \/   ) (   | (    \/|  \  ( || (    \/| (    )|
| |   | || |      | (_____ | || || |  | |   ) || (__    | (_____    | |   | |      |   \ | || (__    | (____)|
( (   ) )| |      (_____  )| |(_)| |  | |   | ||  __)   (_____  )   | |   | | ____ | (\ \) ||  __)   |     __)
 \ \_/ / | |            ) || |   | |  | |   ) || (            ) |   | |   | | \_  )| | \   || (      | (\ (   
  \   /  | (____/\/\____) || )   ( |  | (__/  )| (____/\/\____) |___) (___| (___) || )  \  || (____/\| ) \ \__
   \_/   (_______/\_______)|/     \|  (______/ (_______/\_______)\_______/(_______)|/    )_)(_______/|/   \__/
                                                                                                                  by Mario Pereira

This script uses the ipaddress module in Python to design a maximum of 6 subnets, the script will output the primary details for these subnets based only
on script user’s hosts requirements, these subnets will follow a sequential hierarchy so long as user inputs requirements from largest to smallest.


 _______           _______  _______  _______  _______  _______ 
(  ____ )|\     /|(  ____ )(  ____ )(  ___  )(  ____ \(  ____ \
| (    )|| )   ( || (    )|| (    )|| (   ) || (    \/| (    \/
| (____)|| |   | || (____)|| (____)|| |   | || (_____ | (__    
|  _____)| |   | ||     __)|  _____)| |   | |(_____  )|  __)   
| (      | |   | || (\ (   | (      | |   | |      ) || (      
| )      | (___) || ) \ \__| )      | (___) |/\____) || (____/\
|/       (_______)|/   \__/|/       (_______)\_______)(_______/
                                                          

This is intended for when its necessary to spontaneously calculate Subnet Addressing Schemes.

 _______  _______  _______          _________ _______  _______  _______  _______  _       _________ _______ 
(  ____ )(  ____ \(  ___  )|\     /|\__   __/(  ____ )(  ____ \(       )(  ____ \( (    /|\__   __/(  ____ \
| (    )|| (    \/| (   ) || )   ( |   ) (   | (    )|| (    \/| () () || (    \/|  \  ( |   ) (   | (    \/
| (____)|| (__    | |   | || |   | |   | |   | (____)|| (__    | || || || (__    |   \ | |   | |   | (_____ 
|     __)|  __)   | |   | || |   | |   | |   |     __)|  __)   | |(_)| ||  __)   | (\ \) |   | |   (_____  )
| (\ (   | (      | | /\| || |   | |   | |   | (\ (   | (      | |   | || (      | | \   |   | |         ) |
| ) \ \__| (____/\| (_\ \ || (___) |___) (___| ) \ \__| (____/\| )   ( || (____/\| )  \  |   | |   /\____) |
|/   \__/(_______/(____\/_)(_______)\_______/|/   \__/(_______/|/     \|(_______/|/    )_)   )_(   \_______)
                                                                                                            

Some basic IPv4 knowledge
Basic VLSM process knowledge
Must input required subnet hosts from Largest to Smallest for accurate results and proper hierarchical output.

 _______          _________ ______   _______ 
(  ____ \|\     /|\__   __/(  __  \ (  ____ \
| (    \/| )   ( |   ) (   | (  \  )| (    \/
| |      | |   | |   | |   | |   ) || (__    
| | ____ | |   | |   | |   | |   | ||  __)   
| | \_  )| |   | |   | |   | |   ) || (      
| (___) || (___) |___) (___| (__/  )| (____/\
(_______)(_______)\_______/(______/ (_______/
                                             

Run the script read the instructions before input.
Only number keys and the space bar are necessary for script input.
Script has very basic input validation in it so dont press any letters or the space bar while running.