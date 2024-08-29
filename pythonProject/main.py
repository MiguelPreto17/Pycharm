import pulp

p_max = 25
c_max = 50
c_min = 0


SOC_initial = 25

p1_rede = pulp.LpVariable('p1_rede', 0)
p2_rede = pulp.LpVariable('p2_rede', 0)
p3_rede= pulp.LpVariable('p3_rede', 0)


p1_bat = pulp.LpVariable('p1_bat', 0,p_max)
p2_bat = pulp.LpVariable('p2_bat', 0,p_max)
p3_bat = pulp.LpVariable('p3_bat', 0,p_max)

SOC1 = pulp.LpVariable('soc1', 0,c_max)
SOC2 = pulp.LpVariable('soc2', 0,c_max)
SOC3 = pulp.LpVariable('soc', 0,c_max)

ct = [0.12,0.13,0.08]

demand = [15,10,5]

dt=1


min_c = pulp.LpProblem ("Minimize Z",pulp.LpMinimize)



#Função objetivo

min_c += ct[0]*p1_rede*dt + ct[1]*p2_rede+dt + ct[2]*p3_rede*dt

#restrições

SOC0 = SOC_initial
SOC1 = SOC0 + p1_bat*dt
SOC2 = SOC1 + p2_bat*dt
SOC3 = SOC2 + p3_bat*dt

p1_rede = p1_bat*dt + demand [0]
p2_rede = p2_bat*dt + demand [1]
p3_rede = p3_bat*dt + demand [2]

status = min_c.solve()


print(min_c)

pulp.LpStatus[status]

print (p1_rede.value)
print (p2_rede.value)
print (p3_rede.value)


pulp.value(min_c.objective)