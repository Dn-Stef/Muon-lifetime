# Project Overview
Muons are subatomic particles similar to electrons but much heavier, produced when cosmic rays collide with molecules in Earth’s atmosphere. These high-energy particles travel vast distances, reaching the ground and passing through matter with minimal interaction. To detect muons, cylindrical detectors are often used, where sensitive materials within the detector capture particle interactions. However, not all collisions within the detector correspond to muons; geometric factors, angular acceptance, and detection efficiency reduce the usable area. This concept is called the effective area, which represents the portion of the detector’s surface that reliably measures muons. Using the effective area, the muon flux has been calculated(the rate of particles passing through a unit area), a critical step in determining their lifetime. This calculation was part of a university experiment, with results detailed in the lab report included in this repository.
## Repository Contents
This repository contains three components:
1. `Muon Lifetime.pdf`: A lab report detailing the measurement of the lifetime of muons, conducted as part of a university project.
2. `MC_AREA.py`: A Python script used to calculate the effective area of the muon detector, using a Monte Carlo simulation. Additionally, the script shows the convergence of the effective area. 
3. `MC_DETECTOR_3D.py`: A second Python script that provides a visual representation of muon generation. The top orange circle represents the muon generation point, while the red lines illustrate the trajectories of the generated muons.

Requirements:
```
numpy 2.2.0
matplotlib 3.6.1
```




