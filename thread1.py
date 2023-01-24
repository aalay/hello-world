#main therd
# class vishal:
# 	def vishal1(self):
# 		for i in range (1,10):
# 			print("vishal")



# class aalay:
# 	def aalay1(self):
# 		for i in range(5):
# 			print("aalay")


# t1=vishal()
# t2= aalay()

# t1.vishal1()
# t2.aalay1()


#therding



# from threading import*
# class vishal(Thread):
# 	def run(self):
# 		for i in range (100):
# 			print("vishal")



# class aalay(Thread):
# 	def run(self):
# 		for i in range(100):
# 			print("aalay")


# t1=vishal()
# t2= aalay()

# t1.run()
# t2.run()



from time import sleep

from threading import *


class vishal(Thread):

	def run(self):
		for i in range (100):
			print("vishal")
			sleep(1)



class aalay(Thread):

	def run(self):
		for i in range(100):
			print("aalay")
			sleep(1)


t1=vishal()
t2= aalay()

t1.start()
t2.start()




# str= "this is string example"
# str.split()
# str1[1]=str.replace(" is"," was")
# print(str1)