import random
import time , os , sys
from time import sleep
import colorama
from colorama import Back , Fore , Style

os.system("pip install colorama ")
colorama.init(autoreset=True)

coins = 0


  #############################################################
##                            QUESTIONS                        ##
  #############################################################

def end():
	print(Fore.GREEN + """
	██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗ 
        ██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗
        ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
        ██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
        ╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║
         ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                 """)
	mess = ("You Finished The Game Soldier , Thanks For Playing , Wait For More Levels In Next The Update")
	for char in mess:
		sys.stdout.write(char)
		sys.stdout.flush()
		if char !="/n":
		    time.sleep(0.1)
	os.system("exit")

def qs18():
	global coins
	print("Take A Break Soldier , Its The Last Question !")
	countdown(5)
	print(Fore.GREEN + "Do You Want 1000000 Coins ?")
	coin = input("yes / no : ")
	if coin == "yes":
		print(Fore.RED  +  "Nope")
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		coins = 0
		qs1()
	else:
		print(Fore.YELLOW + "you are a nice guy")

	print(Fore.GREEN +"-10 * 10 * 4 * -3 * 2 * 8 + (-5) - 33 + (-15)")
	qs8 = input("===E ")
	if qs8 == "19147":
		print(Fore.GREEN +"You Are A Legend")
		coins = coins + 1000
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		end()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()

def qs17():
	global coins
	print(Fore.GREEN +"4 - (-4)")
	qs8 = input("===E ")
	if qs8 == "8":
		print(Fore.GREEN +"You Are A Legend")
		coins = coins + 15
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs18()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()

def qs16():
	global coins
	print(Fore.GREEN +"4 - 4 x 10 - 4 x 3 - (-10)")
	qs8 = input("===E ")
	if qs8 == "-26":
		print(Fore.GREEN +"Nice Keep It Up!")
		coins = coins + 15
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs17()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()



def qs15():
	global coins
	print(Fore.GREEN +"5 x 1000 - 5 x (-1000)")
	qs8 = input("===E ")
	if qs8 == "4787":
		print(Fore.GREEN +"Good")
		coins = coins + 15
		print(Fore.YELLOW + "Your Coins Now Are : " +  Fore.MAGENTA + str(coins))
		qs16()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()





def qs14():
	global coins
	print(Fore.GREEN +"5 x (-6) + (-1)")
	qs8 = input("===E ")
	if qs8 == "-31":
		print(Fore.GREEN +"+999 Respect ")
		coins = coins + 15
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs15()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()

def qs13():
	global coins
	print(Fore.GREEN +"999 x (1-1)")
	qs8 = input("===E ")
	if qs8 == "0":
		print(Fore.GREEN +"You Are A Hero")
		coins = coins + 15
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs14()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()

def qs12():
	global coins
	print(Fore.GREEN +"-1 x (-5) + 5")
	qs12 = input("===E ")
	if qs12 == "10":
		print(Fore.GREEN +"Keep It Up")
		coins = coins + 15
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs13()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()


def qs11():
	global coins
	print(Fore.GREEN +"Take A Break Soldier !")
	countdown(5)
	####### box ###########
	print(Fore.LIGHTBLACK_EX +"would you like to buy a legendry mystery box? ")
	y = input("yes/no : ")
	if y == "yes":
		if coins > 50:
			coins = coins - 50
			legendrybox()
		else:
			print(Fore.BLACK + "YOU DONT HAVE ENOUGH COINS")
	####### box ends ###########
	print(Fore.GREEN +"10 * 10 * 3 * 2 * 8 + 5 - 3 + (-15)")
	qs8 = input("===E ")
	if qs8 == "4787":
		print(Fore.GREEN +"You Are A Legend")
		coins = coins + 15
		print(Fore.YELLOW + "Your Coins Now Are : " +Fore.MAGENTA + str(coins))
		qs12()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " +str(coins))
		print(Fore.RED + "loser ...")
		qs1()

def qs10():
	global coins
	print(Fore.GREEN +"10 * 2 * 440 / 2 = ?")
	qs8 = input("===E ")
	if qs8 == "4400":
		print(Fore.GREEN +"Nice")
		coins = coins + 15
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs11()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()






def qs9():
	global coins
	print(Fore.GREEN +"10 + 2 * 3 / 2 = ?")
	qs8 = input("===E ")
	if qs8 == "13":
		print(Fore.GREEN +"Good")
		coins = coins + 10
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs10()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()





def qs8():
	global coins
	print(Fore.GREEN +"1 / 0.1 = ?")
	qs8 = input("===E ")
	if qs8 == "10":
		print(Fore.GREEN +"You Are A Legend")
		coins = coins + 10
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs9()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()


def qs7():
	global coins
	print(Fore.GREEN +"80 / 4 = ?")
	qs7 = input("===E ")
	if qs7 == "20":
		print(Fore.GREEN +"Nice")
		coins = coins + 10
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs8()
	else :
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " +str(coins))
		print(Fore.RED + "loser ...")
		qs1()



def qs6():
	global coins
	print(Fore.GREEN +"6 x 6 x 5 - 2 = ?")
	qs6 = input("===E ")
	if qs6 == "178":
		print(Fore.GREEN +"Perfect")
		coins = coins + 10
		print(Fore.YELLOW + "Your Coins Now Are : " + str(coins))
		qs7()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		print(Fore.RED + "loser ...")
		qs1()






def qs5():
	global coins
	print(Fore.GREEN +"Take A Break Soldier !")
	countdown(5)
	####### box ###########
	print(Fore.LIGHTBLACK_EX +"would you like to buy a box? ")
	y = input("yes/no :")
	if y == "yes":
		if coins > 25:
			coins = coins - 25
			rarebox()
		else:
			print(Fore.BLACK + "YOU DONT HAVE ENOUGH COINS")
	####### box ends ###########
	print(Fore.GREEN +"10 * 10 * 10 - 7 = ?")
	qs5 = input("===E ")
	if qs5 == "993":
		print(Fore.GREEN +"+999 Respect")
		coins = coins + 10
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs6()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		print(Fore.RED + "loser ...")
		qs1()




def qs4():
	global coins
	print(Fore.GREEN +"4 * 5 - 10 + 5 = ?")
	qs4 = input("===E ")
	if qs4 == "15":
		print(Fore.GREEN +"Its Easy ")
		coins = coins + 10
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs5()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		print(Fore.RED + "loser ...")
		qs1()



def qs3():
	global coins
	print(Fore.GREEN +"1 * 1000 = ?")
	qs3 = input("===E ")
	if qs3 == "1000":
		print(Fore.GREEN +"Very Easy")
		coins = coins + 10
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs4()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()
        




def qs2():
	global coins
	print(Fore.GREEN +"8 * 8 = ?")
	qs2 = input("===E ")
	if qs2 == "64":
		print(Fore.GREEN +"Easy Question")
		coins = coins + 10
		print(Fore.YELLOW + "Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs3()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		qs1()
		






def qs1():
	global coins
	print(Fore.YELLOW +"Get Ready Soldier !!")
	countstart(3)
	print(Fore.GREEN +"4 + 4 = ?")
	qs1 = input("===E ")
	if qs1 == "8":
		print(Fore.GREEN +"GO GO GO")
		coins = coins + 10
		print(Fore.YELLOW +"Your Coins Now Are : " + Fore.MAGENTA + str(coins))
		qs2()
	else:
		print(Fore.RED + """
            ███████╗ █████╗ ██╗██╗     ███████╗██████╗ 
            ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗
            █████╗  ███████║██║██║     █████╗  ██║  ██║
            ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║
            ██║     ██║  ██║██║███████╗███████╗██████╔╝
            ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝ 
			""")
		coins = 0
		print(Fore.RED + "Your Coins Now Are : " + str(coins))
		print(Fore.RED + "loser ...")
		start()





  ####################################################
##                   START AND FUNCTIONS              ##
  ####################################################



#############     ITEMS     #################




#print("would you like to buy a box? ")
#		y = input("yes/no :")
#		if y == "yes":
#			if coins > 25:
#			    coins = coins - 25
#			    box()
#			else:
#				print("no")

def countdown(timer):
    
    while timer:
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        timer -= 1
      
    print(Fore.RED + 'Break Ends')

def countstart(timer):
    
    while timer:
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        timer -= 1
      
    print(Fore.RED + 'Go Go Go ! !')

def rarebox():
	global coins
	x = random.randint(20, 50)
	coins = coins + x
	print("You Got " + str(x) +" Coins")
	print ("You Have : " + str(coins) + " Coins")

def legendrybox():
	global coins
	my_list = [0 , 0  , 10 , 10 , 10 , 10 , 50 , 50 , 100 , 250]
	x = random.choice(my_list)
	coins = coins + x
	print("You Got " + str(x) +" Coins")
	print ("You Have : " + str(coins) + " Coins")


def info():
	print(Fore.MAGENTA + """
        ██╗███╗   ██╗███████╗ ██████╗ 
        ██║████╗  ██║██╔════╝██╔═══██╗
        ██║██╔██╗ ██║█████╗  ██║   ██║
        ██║██║╚██╗██║██╔══╝  ██║   ██║
        ██║██║ ╚████║██║     ╚██████╔╝
        ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝  """)
	colorama.init(autoreset=True)
	print (Fore.LIGHTBLACK_EX + "Made By " + Fore.RED + "Clown" + Fore.LIGHTBLACK_EX + " And" + Fore.BLUE + " Pain")
	mess2 = ("""
		1 - Rules
		2 - Updates
		3 - Mystery Boxs
		5 - Back
		""")
	for char in mess2:
		sys.stdout.write(char)
		sys.stdout.flush()
		if char !="/n":
		    time.sleep(0.1)
	info = input("===E ")
	if info == "1":
		print(Fore.RED + """
		1 - Its Not Allowed To Use Calculator!
		2 - Its Not Allowed To Edit The Code And Say Its Your Own!
		3 - Its Not Allowed To Sell This Project!
			""")
	if info == "2":
		print(Fore.RED + """
			New Update In March :
			- Timer For Questions
			- GodLike Mystery Box
			- Lifes
			- New Languages ( Arabic And French)
			- New Questions
			""")
	if info == "3":
		print(Fore.RED + """
	        Rare Mystery Boxs ===E Question 5 (Price : 25 Coins)
	        [Rewards] :
	        20-50 Coins

	        Legendry Mystery Boxs ===E Question 11 (Price : 50) 
	        [Rewards] :
	        40% = 10 Coins
	        20% = 0 Coins 
	        20% = 50 Coins
	        10% = 100 Or 250 Coins ]

	        GodLike Mystery Boxs ===E SOON
			""")
	else:
		start()


def start():
	colorama.init(autoreset=True)
	print(Fore.MAGENTA + """ 
	███╗   ███╗ █████╗ ████████╗██╗  ██╗███████╗
        ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║██╔════╝
        ██╔████╔██║███████║   ██║   ███████║███████╗
        ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║╚════██║
        ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║███████║
        ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝""")
	global coins
	print(Fore.YELLOW + "coins : " + Fore.MAGENTA + str(coins))
	mess = ("What Do You Want To Do :")
	for char in mess:
		sys.stdout.write(char)
		sys.stdout.flush()
		if char !="/n":
		    time.sleep(0.1)

	mess2 = ("""
		1 - Game
		2 - Information
		5 - Exit
		""")
	for char in mess2:
		sys.stdout.write(char)
		sys.stdout.flush()
		if char !="/n":
		    time.sleep(0.1)

	ready = input("===E ")
	if ready == "1":
		print(Fore.RED + "OK :)")
		qs1()
	if ready == "2":
		info();
	else:
		os.system("exit")


start()