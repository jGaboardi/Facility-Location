# -*- coding: utf-8 -*-
# p-Dispersion Facility Location Problem
# This script creates a linear programming file to be read into an optimizer.
'''
GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
'''
# Developed by:  James D. Gaboardi, MSGIS
#                08/2015
#                Â© James Gaboardi

'''
Adapted from:   
    Maliszewski, P. J. 
    M. J. Kuby
    and M. W. Horner 
    2012. 
    A comparison of multi-objective spatial dispersion models for managing 
        critical assets in urban areas. 
    Computers, Environment and Urban Systems. 
    36 (4):331â341.
'''


#  Terminology & General Background for Facility Location and 
#                    Summation Notation:

#   *        The objective of the p-Dispersion Facility Location Problem 
#                    is to maximize the minimum distance bewteen 
#                    facilities (generally noxious).

#   *   [i] - a specific origin
#   *   [j] - a specifc destination
#   *   [n] - the set of origins
#   *   [m] - the set of destinations
#   *   [dij] - matrix of travel costs between nodes
#   *   [M] - largest value in dij
#   *   [D] - Maximized minimum distance between facilities
#   *	[yi] - each service facility
#   *   [p] - the number of facilities to be sited

#    1. IMPORTS
# Other imports may be necessary for matrix creation and manipulation 
import numpy as np


#    2. DEFINED FUNCTIONS
# Objective Function
#
def get_objective_function_pDisp():
    outtext = ' obj: D\n'
    return outtext

# Facility Constraint
# *** '= 1\n' indicates 1 facility  
def get_p_facilities():
    outtext = ''
    for i in range(1, service_nodes+1):
        temp = ''
        temp += 'y' + str(i)
        outtext += temp + ' + '
    outtext = ' c1:  ' + outtext[:-2] + '= 2\n'
    return outtext


# Inter-Facility Distance Constraints   n(n-1)/2
def get_inter_facility():
    outtext = ''
    counter=1
    for orig in range(service_nodes):
        for dest in range(service_nodes):
            if dest > orig:
                counter = counter+1
                outtext += ' c' + str(counter) + ':  ' + str(dij[orig,dest]) + ' + ' + str(2*M) + ' - ' + str(M) + ' y' + str(orig+1) + ' - ' + str(M) + ' y' + str(dest+1) +  ' D >= 0\n'
            else:
                pass
    return outtext       
#ð· â¤ ðij + ð (2 â ði â ðj) ,âð; âð > ð)           
    
            
            

# Declaration of Bounds
def get_bounds_facility():
    outtext = ''
    for i in range(service_nodes):
        outtext += ' 0 <= y' + str(i+1) + ' <= 1\n'
    return outtext

# Declaration of Decision Variables (form can be: Binary, Integer, etc.)
# In this case decision variables are binary.
def get_facility_decision_variables_pDisp():  
    outtext = ''
    for i in range (1, service_nodes+1):
        outtext += ' y' + str(i) + ' '
    return outtext

#    3. DATA Creation & VARIABLE DECLARATION
# Distance Matrix
dij = np.random.randint(10, 50, 16)
dij = dij.reshape(4,4)
# Service Nodes
service_nodes = len(dij)
# Max Value in dij
M = np.amax(dij)

#    4. START TEXT FOR .lp FILE
# Declaration of Objective Function
text = "p-Dispersion Facility Location Problem\n"
text += "'''\n"
text += 'Maximize\n'          
text += get_objective_function_pDisp()
# Declaration of Constraints
text += 'Subject To\n'                    
text += get_p_facilities()
text += get_inter_facility()
# Declaration of Bounds
text += 'Bounds\n' 
text += get_bounds_facility()
# Declaration of Decision Variables form: Binaries
text += 'Binaries\n'
text += get_facility_decision_variables_pDisp()
text += '\n'
text += 'End\n'
text += "'''\n"
text += "Â© James Gaboardi, 2015"                


#   5. CREATE & WRITE .lp FILE TO DISK
# Fill path name  --  File name must not have spaces.
outfile = open('/Users/jgaboardi/Desktop/LP.lp', 'w')
outfile.write(text)
outfile.close()        ñí²íµ¬ð·¨ð¡ó®ò½¶æ½¦á»«rsion Facilitï¿í´ð¶´ðó óñ ðí²í±í²í¹»ò¦¯í²í±£ò¬  ï¿í°òó ñí¾í±óñ°íºí±ó²¹ð¶ªï¿í±³+ï¿í°í³íºò¿¯ ñí²íµ¬ð·¨ð¡ó®   D   D   D   D   D   D   D   D í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿í¿ò¢®í¿í° ò¢®í´í¼ í¿í¹¹ð ó¤ó¥ í±í½í¿í¹¥í¿í° í°í°²ò¢®í¿í° ó¶ í±íµ°ó¦½³í¿í¹¯í³í±µð¦¼­í³í½¥í¿íµ¶í³íµ°í¿í±¡ô©ò²ó®ó¤ó¶ ð´ ò¡ò¢§í¿í° í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·ó®ó¤ó¶ ð´ ò¡ò¢§í¿í° í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·í·ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³                                                                         ï¡í°               ï¼í°                      ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ì³ñð°ñ ð°¥ð¬ð²ò´ó ¯ó° í¿í±¦ð ñªí³í±£íµí±©í¿í±¥í´í±ð°®ò´ó ¯í³í°í·í±¥í¿í±´í¿í°½ô¢ñ­í²í±©ñ°í²í±²ó°©í¿í±®ðò£ò¬í¸í±´ó ð°¯í³í±¡ó°©í¿í±®í±í±ð ¯ñ¬í»í±­ð ®í³í°í·í±¥í¿í±´í¼í°«ð  ñ°§í»í°§ð ®í³í°í·í±¥í¿í±´í¼í°«                                                                                     í²íµ