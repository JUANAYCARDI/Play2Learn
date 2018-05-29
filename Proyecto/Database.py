def getData():
	file = open('login.txt','r')
	data = []
	for line in file:
		line = line.replace('\n',' ')
		data.append(line.split(','))
	return data

def checkData(usuario, contraseña):
    data = getData()
    user = usuario
    passw = contraseña
    role = ''
    i = 1
    j = 0
    while i < len(data):
        if user in data[i]:
        	if passw in data[i]:
            	   if 'admin ' in data[i]:
            		      return True
            	   else:
            		      return False   	
        	else:
        		return 'wrong'
        else:
            i+=1
    return None

def addUser(userID, usuario, correo, contraseña, grado):
    file = open('usersData.txt')
    data = []
    print(data)
    
    for line in file:
        line = line.replace('\n',' ')
        data.append(line.split(','))
    i=0
    while i < len(data):
        if userID not in data[i]:
             i+=1       
        else:
            return 'UserIDE'   
    i=0      
    while i < len(data):
        if usuario not in data[i]: 
            i+=1
        else:
            return 'UserE'   
    i=0 
    while i < len(data):
            if correo not in data[i]:
                i+=1
            else:
                return 'MailE'
    f = open('usersData.txt','a')
    f.write(str(userID) + ',' + str(usuario) + ',' + str(correo) + ',' + str(contraseña) + ',' + str(grado) + '\n')  
    f.close()
    addLogin(usuario, contraseña)
    addGameData(userID)
    return 'Done'                                                

def addLogin(usuario, contraseña):
    f = open('login.txt','a')
    f.write(str(usuario) + ',' + str(contraseña) + ',' + 'user' + '\n')  
    f.close()

def addGameData(userID):
    f = open('gameData.txt','a')
    f.write(str(userID) + ',' + '5' + ',' + '0' + ',' + '0' + '\n')  
    f.close()    

def checkGrade(usuario):
    file = open('usersData.txt', 'r')
    data = []
    i = 0
    for line in file:
        line = line.replace('\n',' ')
        data.append(line.split(','))
    grado = data[i][4]
    while i < len(data):
        if usuario == data[i][1]:
            grado = data[i][4]
            return grado
        else:
            i+=1

def checkLife(userID):
    file = open('gameData.txt','r')
    data = []
    for line in file:
        line = line.replace('\n',' ')
        data.append(line.split(','))
    for line in data: 
        if userID in line:
            return line[1]

def checkCquestions(userID):
    file = open('gameData.txt','r')
    data = []
    for line in file:
        line = line.replace('\n',' ')
        data.append(line.split(','))
    for line in data: 
        if userID in line:
            return line[2]

def checkIquestions(userID):
    file = open('gameData.txt','r')
    data = []
    for line in file:
        line = line.replace('\n',' ')
        data.append(line.split(','))
    for line in data: 
        if userID in line:
            return line[3]

def checkUserID(usuario):
    file = open('usersData.txt', 'r')
    data = []
    for line in file:
        line = line.replace('\n',' ')
        data.append(line.split(','))
    i = 0
    while i < len(data):
        if usuario in data[i]:
            return data[i][0]
        else: 
            i+=1




	









