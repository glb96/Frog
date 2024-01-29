###############################################################################################
#########                          Start of the input file                            #########  
#########                                 Header                                      #########  
###############################################################################################

# Import the usual numpy module to help constructing some list in the parameter file. Note that you can not use this module in this file if you want.
import numpy as np
import os
# Import the module where all the Classes are defined. 
from Frog.class_GP import  GlobalParameter
from Frog.class_Molecule import MoleculeType
# Initialize the General Parameter object and the list of all the molecule type
GP = GlobalParameter()
L_moleculetype = []

# Some definition usefull later on in the input script:
concentration = 20
N_total = 2000
N_eau = int(N_total - N_total*concentration*0.01)

###############################################################################################
#########                                 Header                                      #########  
#########                            General Parameters                               #########
###############################################################################################
path = '../../Tutorials/Traj/Mixture/Meth_wat_bulk'

GP.MD_file_name_topology = os.path.join(path, 'mixture_water_methanol.data')
GP.MD_file_name_traj = os.path.join(path, 'mixture_water_methanol.dcd')
GP.MD_file_type = 'LAMMPS'

GP.general_path = './'

GP.nbr_time_step = 1 # nbr of time step to treat, if N_time = 0 all the time will be treated, the default is 1 
GP.trotter_step = 1 # how many consecutive frame are not treated (1 means every frame are treated, 2, only one over 2, ect..). The default is 1

GP.nbr_parra = 1  # nbr of parralel run. By default equal to 1.
GP.MD_cut_trajectory = True

GP.MD_check_GP() # last line of the GP definition

###############################################################################################
######### General Parameters relative to files, directory and some basic informations #########
#########                    Definition of the molecules type                         #########
###############################################################################################

# note: This code supposed that the number of atom/molecule is constant during the simulation 

######################## Repeat these lines for every molecule type: start ##########################

molecule_type_name = 'Water_TIP4P2005'
where_are_molecules = [1, N_eau]

moleculetype = MoleculeType(GP, molecule_type_name, where_are_molecules)

L_diagram_analysis_to_perform = [
    ['molecular_orientation', 'Plane_xy', [4, 10], 'join'],
    ['molecular_orientation', 'Averaged', [1, 5], 'independent']
                              ]

special_selection = ['Plane_xy', 10, [8]] # to make this test fast

moleculetype.read_diagram_input(GP, L_diagram_analysis_to_perform, special_selection=special_selection)

moleculetype.read_optic_properties_input(GP)

moleculetype.end_initialize(GP)
L_moleculetype.append(moleculetype)

######################## Repeat these lines for every molecule type: end ##########################
######################## Repeat these lines for every molecule type: start ##########################

molecule_type_name = 'Methanol_OPLSAA'
where_are_molecules = [N_eau+1,N_total]

moleculetype = MoleculeType(GP, molecule_type_name, where_are_molecules)

L_diagram_analysis_to_perform = [
    ['molecular_orientation', 'Plane_xy', [5, 10], 'join'],
    ['molecular_orientation', 'Averaged', [1, 5], 'independent']
                              ]

special_selection = ['Plane_xy', 10, [1]] # to make this test fast

moleculetype.read_diagram_input(GP, L_diagram_analysis_to_perform, special_selection=special_selection)

moleculetype.read_optic_properties_input(GP)

moleculetype.end_initialize(GP)
L_moleculetype.append(moleculetype)

######################## Repeat these lines for every molecule type: end ##########################

###############################################################################################
#########                    Definition of the molecules type                         #########
#########                          End of the input file                              #########
###############################################################################################

