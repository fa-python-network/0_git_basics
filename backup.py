#this script brings joy

from classGreeting import Greeting
from marks import Marks

M = Marks()
gr = Greeting()

print ("\n{0}, {1}!\n{2}".format(gr.grtng(), gr.getName(), gr.compliment()))
	
print("Теперь поможем вычислить количество баллов, которые Вы поставите нам за данную работу :)")
m1 = M.getGeneralMark()
m2 = M.getAddMark1()
m3 = M.getAddMark2()
m4 = M.getAddMark3()
print("Итоговое количество баллов = {0}".format(m1+m2+m3+m4))
