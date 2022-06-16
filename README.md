# Dynamic_Systems_Fingerprint_Model
"Final Project",UNAM (https://www.unam.mx/) -TICs-Dynamic Systems 2022-1 class,taught by Dr. Victor de la Luz 


____
## Table of Contents
* [Team_Members](#Team_Members)
* [Project Overview](#Project_Overview)
* [Introduction](#Introduction)
* [Equations](#Equations)
* [Justification](#Justification)
* [Hypothesis](#Hypothesis)
* [Goals](#Goals)
* [Technologies](#Technologies)
* [Packages](#Packages)
* [Results](#Results)
* [References](#References)
* [License](#License)

# Team_Members

* Luis Aarón Nieto Cruz. ([LuisAaronNietoCruz](https://github.com/LuisAaronNietoCruz))
* Jadiel Zúñiga Rodriguez. ([JZRodriguez](https://github.com/JZRodriguez))
* Miguel Ángel Zamorano Presa. ([miguelzpresa](https://github.com/miguelzpresa))
____
# Project_Overview
This project aims to develop a model for fingerprint formation. 

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Fingerprints%20patterns%202.jpg 'Fingerprints')

# Introduction
Fingerprints Growth formation pattern is dictated by highly complex interactions of multiple initial conditions, listed  below. The main goal is to generate fongerprints based of the paper " fingerprint formation model published in the scientific journal EUROPHYSICS LETTERS, "DOI: 10.1209/epl/i2004-10161-2""
 
## What are fingerprints?
Fingerprints are skin patterns with friction ridges. Our fingers, palms and soles are characterized by ridges (hills) and valleys (furrows). Their formation occurs during fetal development, beginning at approximately the 10th week of gestation, being completed by the 17th week, and remaining throughout life.

## What are the patterns of fingerprints? 
There are three basic patterns of fingerprints: 
* Whorls (a): Most complex, and contain central pocket, double loop, and accidental 
* Loops (b): Radial or  ulnar, depending on whether direction of slope of pattern is towards inner arm bone (radius) or outer arm bone (ulna) 
* Arches (c): Can be plain or tented

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Fingerprints%20pattern.jpg 'Types of patterns')



# Equations
The footprint will be constructed with a spherical coordinate domain over a cylindrical coordinate domain.

The surface will be defined as a map of a rectangular region Omega where (u,v) will belong to Omega and the surface S will be defined as the image of the map r: Omega --> S

The map is defined by:

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/F2.jpg 'F2')

r0 is a parameter to be chosen close to the average radius of curvature of the pad. In addition we have a function r(u, v) denoting the surface distance. This construction guarantees a smooth surface (at least once differentiable) for all smooth r(u, v). The geometry of the pad can now be specified by choosing a certain function r(u, v). It is given by
the following expression: 

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/F3.jpg 'F3')




# Justification
### Why is it going to be done?
The biggest inspiration for this project comes from the work of Alan Turing's Patterns in Nature. Zebra stripes, cat coats, leopards and cheetahs are surprisingly unique, making stripes a tool to identify one animal from the rest, fingerprints are like our stripes.   


Turing’s theory was elegant and simple: any repeating natural pattern could be created by the interaction of two things — molecules, cells, whatever — with particular characteristics. Through a mathematical principle he called ‘reaction–diffusion’, these two components would spontaneously self-organise into spots, stripes, rings, swirls or dappled blobs.
"https://ideas.ted.com/how-the-zebra-got-its-stripes-with-alan-turing/"

# Limitations
Physics and mathematical theory of embryology deals with highly complex dynamics systems ,some of them non-linear,its important to mention that we do not pretend to model the actual physical process of ridges formation(fingerprints),However ,the paper that we are analyzing gives an alternative approach,it takes the principal properties ,that we will list below ,to replicate the fingerprint formation during embryological process through ,multivariable calculus tools ,vectors spaces,and numerical methods.

#  Goals
* Get a better understanding of embryological process of epidermial ridge formation
* Understand the problem domain 
* Implement a vector surface as close as possible to a finger (the domain)
* Compute a sphere 
* Simulate the closest thing to a fingerprint


____
# Hipothesis
* Anisotropic laws are true (locally)(inplace stress distribution)
* Stability in the solutions of the ecuations
Given that no person has the same attributes than another person, the expected result is that no two fingerprints analyzed will be the same.
* The stress field anticipates the direction of the ridge system and also predicts in what  areas buckling will take place first
* Von Kallman Ecuations will perform as planned to calculate the buckling patterns



![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Fingerprints%20examples.jpg 'Fingerprint models')

___
# Technologies

* [Python 3](https://www.python.org/)
* Linux Ubuntu    64-bit
* Linux Arch      64-bit
* [Github](https://www.github.com)
* Windows 10      64-bit
* Jupyter lab     3.2.9
* [Blender](https://www.blender.org/)

___
# Packages<br>
* [Pandas    version 1.4.1](https://pandas.pydata.org/)
* [Matplotlib version 3.2.2](https://matplotlib.org/)
* [Numpy      version 1.21.5](https://numpy.org/)  
* Linux console

___
# Results
![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Prueba1.jpg 'Prueba1')

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Prueba2.jpg 'Prueba2')

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Prueba3.jpg 'Prueba3')

![Alt text](https://github.com/JZRodriguez/fingerprints_project/blob/main/Crecimiento-diferencial.jpg 'Crecimiento-diferencial')


___
# References
Europhys. Lett., 68 (1), pp. 141–146 (2004)
DOI: 10.1209/epl/i2004-10161-2

Dubey, Deepika. Fingerprints; 30 May 2018.

Michael Kucken and Alan C. Newell. Fingerprint formation. Journal of Theoretical Biology, 235(13):71–83, 2005

https://github.com/asahidari/differentialgrowthsnliteb3d4

___


# License
Copyright © 2022 <mikezpresa@gmail.com,zujadiel@gmail.com,aaronnicruz@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
