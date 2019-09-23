#this script brings joy

from marks import Marks

M = Marks()

print ("Good morning, Michail Viktorovich!")
print ("Are you drinking coffee now? y/n")
answer = input()

if answer == "y":
	print("Enjoy your coffee and good day!")
elif answer == "n":
	print ("It's so good for your health. Good day!")
else:
	print ("Your answer should be y or n. Repeat, please")
	
print("Теперь поможем вычислить количество баллов, которые Вы поставите нам за данную работу :)")
m1 = M.getGeneralMark()
m2 = M.getAddMark1()
m3 = M.getAddMark2()
m4 = M.getAddMark3()
print("Итоговое количество баллов = {0}".format(m1+m2+m3+m4))