# rectangular_waveguide
Electrodynamics Programming Project

-This program calculates the intensity of an electric field in a rectangular waveguide, specifically for the transverse magnetic modes
in less than 50 lines of python code. This was a project in my Electrodynamics (PHYS-470) class in the spring semester of 2019. 

-Altering the dimensions of the waveguide will produce different graphs, I used generic parameters for the frequency and the wavelength
in my program to get the calculations to work for the plots. 

KNOWN BUGS:
-at the moment the (0,0), (0,1), and (1,0) modes can produce plots but not the desired result. I am looking into whether it is from a
calculation error, from the intensity of the field being plotted instead of the electric fields calculated value, or possibly due to the
way that python handles my equations. Other than this, all other modes that I have tested (1,1) and up all work just fine, and adjusting
the size of the waveguide helps in visualization of the modes.
