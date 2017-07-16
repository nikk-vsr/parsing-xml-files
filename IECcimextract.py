'''functions outside the class'''
#'''returns  the number of feeder branches in the network'''
#findgenfun()
#'''returns the no of substations in the network'''
#findsubstationfun()
#'''returns the number of buses in a substation'''
#substationbusesfun()
'''functions inside the class'''
#Function that finds the number of nodes either
#in feeder section or in a substation.'''
#findnodes()
#'''function which performs the action of
#getting the terminals of components'''
#stackfun()
#'''returns the number of breakers in any single
#feeder section or any single substation'''
#findbreakers()
#'''funciton which gives the detailed view of
#which terminal connected to which node'''
#temtonodefun()
#'''function which checks whether a
#paritcular substation config is ringbus or not'''
#ringbuschekcfun()
#''' similar as above but for
#doublebus doublebreaker substaion config.'''
#twobustwobreakerfun()






'''sample output for each variable in the program can be seen in readme file'''

from elementtree import ElementTree as etree  # Command for importing elementTree package 

'''  r in  brackets of the parse represents readable and writable'''
tree= etree.parse(r'N:\myinternwork\files xml of bus systems\9busi_in_61850.xml')

root= tree.getroot()  # Gets the root the xml which was parsed . 

cim= "{http://iec.ch/TC57/2008/CIM-schema-cim13#}" #namespace uri for cim
rdf= "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}" #namespace uri for rdf

'''empty lists are created for each component because, we don't know how many generators, tranformers,substaions etc;
for the code be generic empty list is created based on search results each elements in the list will be appended'''

linelist=[]   #created for transmission lines or AC line segments
linenames=["L{0}".format(i) for i in range(1,10)]
# line names are given L1,L2,L3 .... hence these are stored in a list for seearching purpose

nodelistgen=[]
#created for storing the terminals connected to each node as a elements  in the list for whole feeder sections
nodelistsub=[] # similar to above but created for substations
 
breakerlistgen=[]
# created for storing the terminals connected to each breaker as a elements in the list for all feeder sections 
breakerlistsub=[] # similar to above but createdfor substation section
buslist=[] # stores the terminal connected to the bus of all the feeder sections. 

''' search for attribute values requires the name to search since convention is standard
 we could predefine the all the variables in a list so that we can iterate through each element of list .''' 
busnames=["G{0}_BB1".format(i) for i in range(1,101)]

trlist1=[] # stores the transformer primary winding connected terminals 
trlist2=[]  # similar as above but for secondary winding 

''' Names of transformer windings TF11, TF21 ,............
            TF12,TF22,.... are stored in tranames1 , trnames2 respectively'''  
trnames1=["TF{0}1".format(i) for i in  range(1,50)]
# Assuming  50 transformers are the maximum transformers in a network, could be changd based on requirement

trnames2=["TF{0}2".format(i) for i in  range(1,50)]
# more the number slower the program would be due to unncessary searches.

''' since the names of each component in feeder section and substaions differ
                        we need to create the varaibles for each of them'''
''' breakersG1, breakersG2,... are the lists which contains the
   names (attribute values of tag breaker in cim file) of breakers in the feeder section respectively.'''
breakersG1=["G1_BR{0}".format(i) for i in range(1,50) ]
breakersG2=["G2_BR{0}".format(i) for i in range(1,50)]
breakersG3=["G3_BR{0}".format(i) for i in range(1,50)]

''' breakersS1,breakersS2,........ are  the lists which contains the
        names(attribute values of tag breaker in cim file) of breakers in the substations respectively'''
breakersS1=["S1_BR{0}".format(i) for i in range(1,50)]
breakersS2=["S2_BR{0}".format(i) for i in range(1,50)]
breakersS3=["S3_BR{0}".format(i) for i in range(1,50)]
breakersS4=["S4_BR{0}".format(i) for i in range(1,50)]
breakersS5=["S5_BR{0}".format(i) for i in range(1,50)]
breakersS6=["S6_BR{0}".format(i) for i in range(1,50)]

''' Based on the maximum conditions the lists can be declared as far as required. '''
     #could create more as above but ,unnecessarily program runs slow if not needed.

'''Similar as breakers, nodes can also be created for each feeder sections, substations '''
nodesG1=["G1_CN{0}".format(i) for i in range(1,10)]
nodesG2=["G2_CN{0}".format(i) for i in range(1,10)]
nodesG3=["G3_CN{0}".format(i) for i in range(1,10)]

''' node names of each substation are  written in a list for searching the attribute value purpose''' 
nodesS1=["S1_CN{0}".format(i) for i in range(1,50)]
nodesS2=["S2_CN{0}".format(i) for i in range(1,50)]
nodesS3=["S3_CN{0}".format(i) for i in range(1,50)]
nodesS4=["S4_CN{0}".format(i) for i in range(1,50)]
nodesS5=["S5_CN{0}".format(i) for i in range(1,50)]
nodesS6=["S6_CN{0}".format(i) for i in range(1,50)]

''' nodeblocks list is the list created for storing the object names of the
         comprehensive nodes in particular feeder sections,substations '''
#i.e. nodesG1 is the object for storing all the nodes in the feeder sections 1
nodesblocks=[nodesG1,nodesG2,nodesG3,nodesS1,nodesS2,nodesS3,nodesS4,nodesS5,nodesS6]

# EVEN THOUGH NAMES ARE OF SERIES LIKE G1,G2,G3,.. S1,S2,S3 IT CAN'T BE WRITTEN IN A FOR LOOP FORM FOR AUTOCREATION
# AS THESE ARE NOT STRINGS, THESE ARE OBJECTS. FOR MORE NUMBER U HAVE TO ADD IT MANUALLY .

'''breakerblocks list is also as similar as above, but for the breakers in substations respectively.'''
breakerblocks=[breakersG1,breakersG2,breakersG3,breakersS1,breakersS2,breakersS3,breakersS4,breakersS5,breakersS6]
#i.e. breakersG1 is the object for storing the breakers in the feeder section1 

'''findgenfun() for finding the number of feeder branches in the network'''
'''In the code written below, the main goal is to iterate through out xml 
    for specific attribute values and increase the count as soon as it found '''

'''logic behind doing that is,since the names of components are known( standard IEC61850)
these can be used anywhere for iterating purpose. '''

              
def findgenfun():
    for x in range(0,500):  # Assuming there are maximum of 500 subchilds of root(extend the number if there are more)
        for i in range(0,10): # Assuming there are 10 generators are there in network,if there are more extend the number
            try:
                if root[x].attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID']=='G{0}_BB1'.format(i):
                    #searching for the each praticular attribute value like G1_BB1 etc.,
                    findgens=i
                    # Number of feeder branches= number of generators, modifying the i value as soon an value was found
            except IndexError:
#Catching the error ,Since the search may cross the number (like [400][5] may not exist ) than which is existing it will raise an error.
                pass  # As we need to continue the search for further pass can be used 
    return findgens  # returns the value of number of feeder sections in network when called
                    
'''findsubstation() for finding the no of substations in the network '''
def findsubstationfun():
    for x in range(0,500):  # similar to the above search for the attributes like S1 ,S2 ,S3........
        for i in range(0,10):
            try:
                if root[x].attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID']=='S{0}'.format(i):
                    subs=i
            except IndexError:
                pass
    return subs

'''for finding the number of nodes in each block'''
blocksg=[]
#empty list created for storing the number of connectivity Nodes in each feeder sections as elements while runtime
blocksu=[]
#empty list created for storing the number of connectivity Nodes in each substation sections as elements while runtime


class findnodesall:
    def __init__(self,i,name):
        self.name=name
        self.i=i
        taglist=[]
    def findnodes(self):
        # Function that finds the number of nodes either in feeder section or in a substation.
        taglist=tree.findall('{0}ConnectivityNode'.format(cim))
        # gets all the child elements of root named connectivityNode
        m =[] #temporary variable used for return  
        for k in range(0,1500): # assuming there are 1500 childs to the maximum for the root. 
            for l in range(0,10): #assuming the maximum of 10 sub childs are there for each child.
                try:
                    if taglist[k].attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID']==(self.name)[l]:
                        m.append(1)
       
                except IndexError:
                   pass
        return len(m)
''' As findgenfun() can't always be a natural number since when file parsed is of substation
           then the generators would be zero  Hence it is recommended to check always'''
if findgenfun()!=None:  
    for i in range (0,findgenfun()):
        blocksg.append(findnodesall(i,nodesblocks[i]))
        #objects for passing to the function( variables of it are G1_CN1,G1_CN2,..)
if findgenfun()!=None:
    for i in range (0,findgenfun()):
        blocksg[0].findnodes()  # gives the number of nodes  in feeder section 1

        blocksg[1].findnodes()  # gives the number of nodes in feeder section 2

for i in range (0,findsubstationfun()):
    blocksu.append(findnodesall(i,nodesblocks[i+3]))
    # variables in each objects for this are S1_CN1,S1_CN2 etc.,

#print no of nodes in substaion S1" , blocksu[0].findnodes()

''' Since in each substaion , different types of bus bar schemes are used there could be buses of
more than one. Hence, the function is created for getting the number of buses in each substation'''
def substation_busesfun():  
    for child in root:
        for n in range(1,5):
            if child.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID']=="S1_BB{0}".format(n):
                                     # searching the attribute value S1_BB1,S1_BB2... 
                k=n                  #alloting the value of last bus it found to the k 
    return k                         # returns the number of buses in the substation S1.

'''class created for gettting the node, breaker,generator,transformer etc., '''

class nodebreaker_terminals:
    def __init__(self,i,name): 
        self.i=i
        self.name=name
    def stackfun(self):             # function which performs the action of getting the terminals of components
        listem=[]                   # temporary variable just used for return the answer while call.
        for x in range(0,1000):     # assuming there are 1000 childs to the max for the root
            for j in range(0,20):   # assuming the 20 subchilds to the max for each child.
                try:   
                    if root[x].attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID']==(self.name):
                        # checkingg for attribute value of particular node in a feeders section or substation
                        if root[x][j].tag=="{0}ConductingEquipment.Terminals".format(cim):
    #since it has many childs we need to search for required tag for getting terminals
                            n1= root[x][j].attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource']
    # after finding the tag get the attirbute of it and append it in a list & continue loop
                            listem.append(n1)
                except KeyError:
                    pass
                except IndexError:
                    pass
        return listem

if findgenfun()!= None:
    for i in range(0,blocksg[0].findnodes()):                   #In range of  no of nodes in the feeder section 1 
        nodelistgen.append(nodebreaker_terminals(i,nodesG1[i])) #based on the range, equivalent number of objects will be decided
        nodelistgen[i].stackfun()
    #stores the list of terminals connected to each node corresponding to feeder section 1 (G1)
    #print nodelistgen[0].stackfun() prints the terminals connected to node1
for i in range(0,blocksu[0].findnodes()):                       # In range of no of nodes in the substation S1
    nodelistsub.append(nodebreaker_terminals(i,nodesS1[i]))     #based on the range equivalent number of objects will be created
    nodelistsub[i].stackfun()
    # stores the list of terminals connected to each node corresponding to the substaion 1 (S1)


'''class created for finding the breakers in the feeder section and substations '''
class findbreakersall:
    def __init__(self,i,name):
        self.name=name
        self.i=i
    def findbreakers(self):
        taglist=tree.findall('{0}Breaker'.format(cim))   #taglist will be filled with all object instances with the cim:breaker tag
        m =[]                                            #temporay variable for used for return
        for k in range(0,1500):                          #Assuming there aren't of  more than 1500 childs for the root. 
            for l in range(0,10):                        #Assuming there are not more than 10 sub childs for each child
                try:
                    if taglist[k].attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID']==(self.name)[l]:
                        m.append(1)
                except IndexError:
                   pass
        return len(m)
tempg=[]
'''empty list created for storing the number of breakers in the each
           feeder section respectively as elements of tempg  during runtime'''             
if findgenfun()!= None:
        for i in range (0,findgenfun()):                            # running the for loop for range upto number of feeder sections
            tempg.append(findbreakersall(i,breakerblocks[i]))       # i represents the feeder sections number
#print  " no of breakers in a gen branch 1 ",tempg[0].findbreakers()    

temps=[]
'''empty list  created for storing the number of breakers in the each
           substation respectively as elements of temps  during runtime'''

for i in range (0,findsubstationfun()):                             #running the for loop in range upto number of substations
    temps.append(findbreakersall(i,breakerblocks[i+3]))             # i represents the substaion number
#print " no of breakers in S1 ", temps[0].findbreakers()
    
'''For getting Breaker terminals in the each feeder section '''
if findgenfun()!= None:
    for i in range(0,tempg[0].findbreakers()):
        # running the for loop in range of number of breakers in feeder section 1  
        breakerlistgen.append(nodebreaker_terminals(i,breakersG1[i]))
# creates the objects for storing the terminals connected to each breaker of a feeder section  in a object during runtime 
#breakerlistgen[1].stackfun()   # list index out of range over i>1
'''For getting breaker terminals in the each substation '''        
for i in range(0,temps[0].findbreakers()):
    #running the for loop in range of number of breakers in substation 1
    breakerlistsub.append(nodebreaker_terminals(i,breakersS1[i]))
    #creates the objects for storing the terminals connected to each breaker of a substation in a object
#breakerlistsub[3].stackfun()
    
''' for getting the terminals connected to bus'''
if findgenfun()!= None:
    for i in range(0,findgenfun()):
        #running the for loop in range number of feeder sections
        buslist.append(nodebreaker_terminals(i,busnames[i]))
        #creates the objects for storing the terminal connected to each bus of a feeder section
#buslist[0].stackfun()
        
'''for getting the terminals connected to the transformer winding1 '''
if findgenfun()!= None:
    for i in range(0,findgenfun()):
        #running the for loop in range number of feeder sections
        trlist1.append(nodebreaker_terminals(i,trnames1[i]))
        #creates the objects for storing the terminals connected to tr winding 1 
# trlist1[0].stackfun()

'''for getting the terminals connected to the transformer winding1 '''
if findgenfun()!= None:
    for i in range(0,findgenfun()):
        #running the for loop in range number of feeder sections
        trlist2.append(nodebreaker_terminals(i,trnames2[i]))
        #creates the objects for storing the terminals connected to tr winding 2
#print " terminals coonected to transformer " ,trlist2[0].stackfun()

''' line segment terminals''' 
for i in range(0,6):
    linelist.append(nodebreaker_terminals(i,'L{0}'.format(i+1)))
    #creates the objects for storing the terminals connected to the line as each element of the list.
# print linelist[5].stackfun() i.e. prints the terminal connected to either ends of the  line segment L6

'''class created for getting the nodes for each terminal reverse of the work done by nodebreaker_terminals'''
class terminals:
    def __init__(self,name):
        self.name=name  # created for giving the name of substation which will be given by instance variable
        termn=[]  #list created for storing the noode to which the terminal is connected as element in the list respectively. 
        termb=[]  # simlar to above breaker is connected to a terminal, termb stores the breakers to which the terminal is connected.
        
    def temtonodefun(self): #function that gives the nodes connected to the terminal, breakers connected to terminal .
        for x in range(0,1000):          #Assuming there aren't of more than 1500 childs for the root rdf.
            for y in range(0,50):        #assuming there aren't more than 50 terminals 
               try: #method that performs 
                   if root[x].attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID']==(self.name+'_T{0}'.format(y)):
                       #searching for the attribute value S1_T1, S1_T2.. S2_T1,S_T,...
                       a=root[x][1].attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource']
                       b=root[x][0].attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource']
                       termn.append(a)  #appends each node connected to corresponding terminal with  each iteration 
                       termb.append(b)  #appends breaker connected to  corresponding terminal with each interation
                   
               except KeyError:
                    pass
               except IndexError:
                    pass
        return termn,termb
    
sul=[]  # getting the node connected to the terminals in  substation S1
for i in  range(0,blocksu[0].findnodes()):
     sul.append(terminals('S{0}'.format(i+1))) #creates instances with variables name S1,S2 like that while iteration
#print sul[0].temtonodefun() gives the nodes connected to the each terminal,
     #breakrer connected to the same terminal in list
#nob=(sul[0].temtonodefun())
#print nob[0]
#q=(sul[0].temtonodefun())[1]
#p=nob[0]
#q=nob[1]

#dictstermsn={}
#dictstermsb={}
#for i in range(0,len(p)):
#    dictstermsn[i+1]=p[i]
#    dictstermsb[i+1]=q[i]
#print dictstermsb
#print dictstermsn

''' logic inside substation check is that, each substation configurtion has a different number
of nodes and breakers with ceratin relation. This relation can be used to find the substation configuration''' 

class substationcheck:  #( class which checks the substation configurations present in the whole network
    def __init__(self,i):
        self.i=i
        lit=[]                 #temporary list used for return 
    def ringbuscheckfun(self): # function that checks whether particular substation is ringbus or not
        for k in range(0,blocksu[self.i].findnodes()):
            if len(nodelistsub[k].stackfun())>2:  # if no of nodes are greater than 2 
                lit.append(k)                       #all node will be appended in lit

        if len(lit)< blocksu[0].findnodes() and len(lit)>1:
            return True
    def twobustwobreakercheckfun(self): # function that checks whether substaion is doublebusdoublebreaker or not 
        if temps[self.i].findbreakers()==2*(((blocksu[self.i].findnodes())-2)):
            #no of breakers must be 2 times the nodes - 2 
            return True
    def one1bytwobreakercheckfun(self): # similarly for all 
        if temps[self.i].findbreakers()==1.5*((blocksu[self.i].findnodes())-2):
            #no of breakers in the substation must be 3/2 time the nodes -2 
            return True
    def transferbuscheckfun(self):
        if (blocksu[self.i].findnodes())==2 and temps[self.i].findbreakers()>2:
            #no of nodes must be 2 and  the breakers  must be greater than 2 
            return True
        
    def nosplitcheckfun(self):
        if (blocksu[self.i].findnodes())==(temps[self.i].findbreakers()+1):
            # no of nodes must be equal to no of breakers
            return True
        
    def onebreakertwobuscheckfun(self):
        if (blocksu[self.i].findnodes()-2)==2*((temps[self.i].findbreakers())-1):
            #(no of nodes -2 ) must be (double the no of breakers -1) 
            return True
#subsplit=substationcheck(0)
#print " S1 is ringbus", subsplit.ringbuscheckfun()
#print " S1 double bus double breaker " ,subsplit.twobustwobreakercheckfun()

