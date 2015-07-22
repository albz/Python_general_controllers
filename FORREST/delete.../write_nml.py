### writing DUED namelist using Python
### at present all values are given, no way to chose it
### at present no Path is given
###
###
###  A. Marocchino 20-05-2010
###


###--- Function that writes the namelist ---###
def write_nml(path, l, times_NI, times_NJ, C_Filter):

	### --- INPUT paramters ---###
	NI       = 10
	NJ       = 1.46*285

	#times_NI = 1.0
	#times_NJ = 1.0

	#l        = 100
	angle    = 180/l;
	A_0      = 1e-8
	C_Filter = 0.19
	### --- ###

	### ---
	NI = round( NI * times_NI )
	NJ = round( NJ * times_NJ )
	### ---

	### Opening file ###
	nml = open(path+"/dued.nml","w")
	### --- ###

	### START
	nml.write("&START\n")
	nml.write("\tBEGIN  =.T.,\n") 
	nml.write("\tLdump=.f.,\n") 
	nml.write("\tstub = 'afRTI-test023'\n")
	nml.write("&END\n")


	### VAR
	nml.write("&VAR\n") 
	nml.write("\tDTWRIT =1.0D-10,\n")
	nml.write("\tTMAX   =9.35e-9,\n")
	nml.write("\tNMAX=200000,\n")
	nml.write("\tKWR =5000,\n")
	nml.write("\tIPLOT  =.T.,\n")
	nml.write("\tKPLOT  =1,\n")
	nml.write("\tRELMAX =0.15,\n")
	nml.write("\tDTMAX  =5.D-11,\n")
	nml.write("\tDTMIN  =1.D-25,\n")
	nml.write("\tLOOPM  =20,\n")
	nml.write("\tPRECTI =1e-2,\n")
	nml.write("\tNMAXRE =20,\n")
	nml.write("\tASQ    =2.5,\n")
	nml.write("\tKICCG  =.T.,\n")
	nml.write("\tPACC=1.D-12,\n")
	nml.write("\tKITERM=200,\n")
	nml.write("\tWR=.F.,\n")
	nml.write("\tWZ=.F.,\n")
	nml.write("\tWUR=.F.,\n")
	nml.write("\tWUZ=.F.,\n")
	nml.write("\tWUROPO=.F.,\n")
	nml.write("\tWUTETA=.F.,\n")
	nml.write("\tWROPOL=.F.,\n")
	nml.write("\tWTETA=.F.,\n")
	nml.write("\tWDENS=.F.,\n")
	nml.write("\tWTEMP=.F.,\n")
	nml.write("\tWSLASE=.F.,\n")
	nml.write("\tWPRES=.F.,\n")
	nml.write("\tWZS=.F.,\n")
	nml.write("\tWFDEUT=.F.,\n")
	nml.write("\tWFTRIT=.F.,\n")
	nml.write("\tWJACOB=.F.,\n")
	nml.write("\tWAFLEI=.F.,\n")
	nml.write("\tWAFLEJ=.F.,\n")
	nml.write("\tWAFLRI=.F.,\n")
	nml.write("\tWAFLRJ=.F.,\n")
	nml.write("\tWSLASE=.T.,\n")
	nml.write("\tWSR=.F.,\n")
	nml.write("\tWSALFE=.F.,\n")
	nml.write("\tWSALFI=.F.,\n")
	nml.write("\tWEALFA=.F.,\n")
	nml.write("\tWFDEUT=.F.,\n")
	nml.write("\tWFTRIT=.F.,\n")
	nml.write("\tWOUTT0=.F.,\n")
	nml.write("\tVECTWR(1)=1.200D-8,\n")
	nml.write("\tVECDTW(1)=0.250D-9,\n")
	nml.write("\tWEACHS=.T.,\n")
	nml.write("\tNDEBUGLEV=1,\n")
	nml.write("\tLCHEME    = .T. ,\n")
	nml.write("\tLREZON(1) = .F.,\n")
	nml.write("\tLREZON(2) = .T. ,\n")
	nml.write("\tLREZON(4) = .T.,\n")
	nml.write("\tLREZON(5) = .T.,\n")
	nml.write("\tLREZON(9) = .T.,\n")
	nml.write("\tLREZON(10) = .F.,\n")
	nml.write("\tLREZON(12) = .T.,\n")
	nml.write("\tLREZON(13) = .T.,\n")
	nml.write("\tREACON(63) = 1.0,\n")
	nml.write("\tREACON(81)=0.06,\n")
	nml.write("\tREACON(82)=0.06,\n")
	nml.write("\tREACON(68)=1.0,\n")
	nml.write("\tREACON(85)=0.0,\n")
	nml.write("\tREACON(84)=0.0,\n")
	nml.write("\tIGRICO(3)=1,\n")
	nml.write("\tLMESHCOLLISIONS=.F.,\n")
	nml.write("\tJMIN_COLL=4,\n")
	nml.write("\tJMAX_COLL=" + str(NJ+2) + ",\n")
	nml.write("\tIMIN_COLL=2,\n")
	nml.write("\tIMAX_COLL=" + str(NI+2) + ",\n")
	nml.write("\tLHGFILTER=.TRUE.\n")
	nml.write("\tCOEF_HGFILTER=" + str(C_Filter) + ",\n")
	nml.write("\tIMIN_FILTER=1,\n")
	nml.write("\tIMAX_FILTER=" + str(NI+2) + ",\n")
	nml.write("\tJMIN_FILTER=5,\n")
	nml.write("\tJMAX_FILTER=" + str(NJ+2) + ",\n")
	nml.write("&END\n\n")


	### FIX NCASE
	nml.write("&FIX NCASE=0001,\n")
	nml.write("\tDUED=.T.,\n")
	nml.write("\tGCYL=.T.,\n")
	nml.write("\tGROTET=.T.,\n")
	nml.write("\tTETAMD=" + str(angle) + ",\n")
	nml.write("\tPERBC=.F.,\n")
	nml.write("\tRIGRR=.f.,\n")
	nml.write("\tRIGLR=.F.,\n")
	nml.write("\tRIGLZ=.F.,\n")
	nml.write("\tRIGUZ=.f.,\n")
	nml.write("\tNTEMP=2,\n")
	nml.write("\tTROOM=1.000E3,\n")
	nml.write("\tLMULTG=.F.,\n")
	nml.write("\tNGROUP=2,\n")
	nml.write("\tFREQ(1)  =     1.,\n")
	nml.write("\tFREQ(2)  =    10.,\n")
	nml.write("\tKOPACI=7,\n")
	nml.write("\tHYDRO=.T.,\n")
	nml.write("\tTHC=.T.,\n")
	nml.write("\tAFL=0.06,\n")
	nml.write("\tLASER=.T.,\n")
	nml.write("\tALAM=0.35,\n")
	nml.write("\tFLACRD=0.d0,\n")  ### Originally 1.0d0
	nml.write("\tILASR=45,\n")
	nml.write("\tTPULSE=10.799e-9,\n")
	nml.write("\tTRISE =1.d-12,\n")
	nml.write("\tS00=7.96d17,\n")
	nml.write("\tCOET(1)=1d-12,\n")
	nml.write("\tCOEW(1)=1.d-7,\n")
	nml.write("\tCOET(2)=0.3d-10,\n")
	nml.write("\tCOEW(2)=0.50,\n")
	nml.write("\tCOET(3)=4.0d-9,\n")
	nml.write("\tCOEW(3)=0.50,\n")
	nml.write("\tCOET(4)=4.4d-9,\n")
	nml.write("\tCOEW(4)=0.63,\n")
	nml.write("\tCOET(5)=4.8d-9,\n")
	nml.write("\tCOEW(5)=0.84,\n")
	nml.write("\tCOET(6)=5.2d-9,\n")
	nml.write("\tCOEW(6)=1.20,\n")
	nml.write("\tCOET(7)=5.6d-9,\n")
	nml.write("\tCOEW(7)=1.7,\n")
	nml.write("\tCOET(8)=6.0d-9,\n")
	nml.write("\tCOEW(8)=2.7,\n")
	nml.write("\tCOET(9)=6.4d-9,\n")
	nml.write("\tCOEW(9)=4.5,\n")
	nml.write("\tCOET(10)=6.8d-9,\n")
	nml.write("\tCOEW(10)=9.5,\n")
	nml.write("\tCOET(11)=7.2d-9,\n")
	nml.write("\tCOEW(11)=20.0,\n")
	nml.write("\tCOET(12)=7.5d-9,\n")
	nml.write("\tCOEW(12)=26.0,\n")
	nml.write("\tCOET(13)=10.6d-9,\n")
	nml.write("\tCOEW(13)=26.0,\n")
	nml.write("\tCOET(14)=10.8d-9,\n")
	nml.write("\tCOEW(14)=0.0,\n")
	nml.write("\tRLASER=" + str(angle) + ",\n")
	nml.write("\tWIDTH =" + str(angle) + ",\n")
	nml.write("\tTETMIN=0.0,\n")
	nml.write("\tTETMAX=" + str(angle) + ",\n")
	nml.write("\tRFOC=0.0,\n")
	nml.write("\tZFOC=0.0,\n")
	nml.write("\tNRAY=" + str(NI) + ",\n")
	nml.write("\tCRAYAB=1.D-5,\n")
	nml.write("\tLST=.F.,\n")
	nml.write("\tLREFRACT=.F.,\n")
	nml.write("\tLBURN=.F.,\n")
	nml.write("\tKALFDT=0,\n")
	nml.write("\tRADLOS=.F.,\n")
	nml.write("&END\n\n")
 
 
	### INDA
	nml.write("&INDA\n")
	nml.write("\tKMESH=1,\n")
	nml.write("\tNPI=" + str(NI) + ",\n")
	nml.write("\tNPJ=" + str(NJ) + ",\n")
	nml.write("\tNZONI=1,\n")
	nml.write("\tNZONJ=3,\n")
	nml.write("\tNLZI(1)=" + str(NI) + ",\n")
	nml.write("\tNLZJ(1)=" + str(round(20*times_NJ))  + ",\n")
	nml.write("\tNLZJ(2)=" + str(round(115*times_NJ)) + ",\n")
	nml.write("\tNLZJ(3)=" + str(NJ - round(115*times_NJ) - round(20*times_NJ)) + ",\n")
	nml.write("\tZZ0(1)=0.0000,\n")
	nml.write("\tZZ0(2)=0.0833,\n")
	nml.write("\tZZ0(3)=0.0925,\n")
	nml.write("\tZZ0(4)=0.1044,\n")
	nml.write("\tTETA0D(1)=0.D0,\n")
	nml.write("\tTETA0D(2)=" + str(angle) + ",\n")
	nml.write("\tFMESHI(1)=1.000,\n")
	nml.write("\tFMESHJ(1)=0.95,\n")
	nml.write("\tFMESHJ(2)=1.00000,\n")
	nml.write("\tFMESHJ(3)=1.00000,\n\n")
	
	nml.write("\tIMAT0(1,1)=1,\n")
	nml.write("\tT00(1,1)=2.00E1,\n")
	nml.write("\tRO00(1,1)=1.00D-4,\n")
	nml.write("\tFDEUT0(1,1)=0.5D0,\n")
	nml.write("\tFTRIT0(1,1)=0.5D0,\n\n")
	
	nml.write("\tIMAT0(1,2)=1,\n")
	nml.write("\tT00(1,2)=2.00E1,\n")
	nml.write("\tRO00(1,2)=0.25,\n")
	nml.write("\tFDEUT0(1,2)=0.5D0,\n")
	nml.write("\tFTRIT0(1,2)=0.5D0,\n\n")
	
	nml.write("\tIMAT0(1,3)=1,\n")
	nml.write("\tT00(1,3)=2.00E1,\n")
	nml.write("\tRO00(1,3)=0.25,\n")
	nml.write("\tFDEUT0(1,3)=0.5D0,\n")
	nml.write("\tFTRIT0(1,3)=0.5D0,\n\n")
	
	nml.write("\tDT0=1.D-15,\n\n")
	
	nml.write("\tNJMAC0=9,\n")
	nml.write("\tJMINR0=2,\n")
	nml.write("\tJMAXR0=" + str(NJ+2) + ",\n")
	nml.write("\tJMAXA0=" + str(NJ+2) + ",\n")
	nml.write("\tJLZ10(1)=2,\n")
	nml.write("\tJLZ10(2)=" + str(round(22*times_NJ)) + ",\n")
	nml.write("\tJLZ10(3)=" + str(round(52*times_NJ)) + ",\n")
	nml.write("\tJLZ10(4)=" + str(round(135*times_NJ)) + ",\n")
	nml.write("\tJLZ10(5)=" + str(round(235*times_NJ)) + ",\n")
	nml.write("\tJLZ10(6)=" + str(round(250*times_NJ)) + ",\n")
	nml.write("\tJLZ10(7)=" + str(round(255*times_NJ)) + ",\n")
	nml.write("\tJLZ10(8)=" + str(round(260*times_NJ)) + ",\n")
	nml.write("\tJLZ10(9)=" + str(round(270*times_NJ)) + ",\n")
	nml.write("\tJLZ10(10)="+ str(NJ+2) + ",\n\n")
		
	nml.write("\tPERT=.T.,\n\n")
	nml.write("&END\n\n")
	
	
	### EOSDA
	nml.write("&EOSDA\n")
	nml.write("\tEOSIG=.F.,\n")
	nml.write("\tKWREOS=.T.,\n")
	nml.write("\tNMAT=1,\n")
	nml.write("\tAM0(1)=2.5,\n")
	nml.write("\tZM0(1)=1.,\n")
	nml.write("\tDS(1)=0.25,\n")
	nml.write("\tCS(1)=1.2E5,\n")
	nml.write("\tDHVAP(1)=3D9,\n")
	nml.write("\tNEL(1)=1,\n")
	nml.write("\tZEL(1,1)=1.,\n")
	nml.write("\tFEL(1,1)=1.,\n")
	nml.write("\tTIMIN=0.1,\n")
	nml.write("\tNDECTI=11,\n")
	nml.write("\tNPTDEC=8,\n")
	nml.write("\tROMIN=1.D-8,\n")
	nml.write("\tNDECRO=13,\n")
	nml.write("\tNPRDEC=7,\n")
	nml.write("\tIOPTAB(1)=52714101,\n")
	nml.write("\tIDNLTE(1)=0,\n")
	nml.write("\tZSMIN   = 1.0,\n")
	nml.write("&END\n\n")
 
 
	### PERTXV
	nml.write("&PERTXV\n")
	nml.write("\tPERTX=.T.,\n")
	nml.write("\tPERTV=.F.,\n")
	nml.write("\tPEREXP=.T.,\n")
	nml.write("\tDEL0X=" + str(A_0) + ",\n")  #Initial Amplitude - perturbation
	nml.write("\tDEL0V=0.0,\n")
	nml.write("\tNHLAM=1,\n") #1
	nml.write("\tNSEP=" + str(round(270*times_NJ)) + ",\n")
	nml.write("\tDELTFI=0.,\n")
	nml.write("\tFATESP=0.0,\n") # 1.0
	nml.write("\tMAXMOD=1,\n")
	nml.write("\tDEL0XR(1)=1.,\n")
	nml.write("\tDEL0VR(1)=0.,\n")
	nml.write("\tR0PERT=10000000,\n")
	nml.write("&END\n\n")
 
 
	### POLARMESH
	nml.write("&POLARMESH\n")
	nml.write("\tLPOLARMESH=.FALSE.\n")
	nml.write("&END\n")
 
 
	### EBEAM
	nml.write("&EBEAM\n")
	nml.write("\tLEBEAM=.f.,\n")
	nml.write("&end\n")
	nml.write("&mtdata\n")
	nml.write("\tlinputFile1D= .f.,\n")
	nml.write("\tinputFile1D = '\?\?.dat' \n")
	nml.write("&end\n\n")

	nml.write("&mtale\n")
	nml.write("&end\n")
	nml.write("c1\n")
	nml.write("c2\n")
	nml.write("c3\n")
	nml.write("c4\n")
	nml.write("finefile")


	###
	nml.close()
	###
	
	return 1
###--- END FUNCTION NML-WRITING ---###
######################################


# path = "/Users/alberto/Documents/Python_Programs/cazzo"
# write_nml(path, 100, 1, 1, 0.19)