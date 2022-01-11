;
; ********************************
; Death of Solar System Simulation
; Toby Skinner
; December 15, 2011
; ********************************
;
; Nomenclature note: The term "Orbital Velocity" is actually "Speed" 
; with a constant orbital direction
;
globals [OriginalMassSun MassSun MassSunM1 
         SizeSun SizeMercury SizeVenus SizeEarth SizeMars SizeJupiter SizeSaturn 
         SizeUranus SizeNeptune
         TrueOrbitalRadiusMercury TrueOrbitalRadiusVenus TrueOrbitalRadiusEarth 
         TrueOrbitalRadiusMars TrueOrbitalRadiusJupiter TrueOrbitalRadiusSaturn
         TrueOrbitalRadiusUranus TrueOrbitalRadiusNeptune
         DisplayOrbitalRadiusMercury DisplayOrbitalRadiusVenus 
         DisplayOrbitalRadiusEarth DisplayOrbitalRadiusMars 
         DisplayOrbitalRadiusJupiter DisplayOrbitalRadiusSaturn
         DisplayOrbitalRadiusUranus DisplayOrbitalRadiusNeptune
         DegreesMercury DegreesVenus DegreesEarth DegreesMars DegreesJupiter 
         DegreesSaturn DegreesUranus DegreesNeptune
         ColorSun ColorMercury ColorVenus ColorEarth ColorMars ColorJupiter 
         ColorSaturn ColorUranus ColorNeptune
         OrbitalVelocityMercury OrbitalVelocityVenus OrbitalVelocityEarth 
         OrbitalVelocityMars OrbitalVelocityJupiter OrbitalVelocitySaturn 
         OrbitalVelocityUranus OrbitalVelocityNeptune
         PlotOrbitalVelocityMercury PlotOrbitalVelocityVenus 
         PlotOrbitalVelocityEarth PlotOrbitalVelocityMars 
         PlotOrbitalVelocityJupiter PlotOrbitalVelocitySaturn 
         PlotOrbitalVelocityUranus PlotOrbitalVelocityNeptune
         IncDegreesMercury IncDegreesVenus IncDegreesEarth IncDegreesMars 
         IncDegreesJupiter IncDegreesSaturn IncDegreesUranus IncDegreesNeptune
         XCoordMercury XCoordVenus XCoordEarth XCoordMars XCoordJupiter XCoordSaturn 
         XCoordUranus XCoordNeptune
         YCoordMercury YCoordVenus YCoordEarth YCoordMars YCoordJupiter YCoordSaturn 
         YCoordUranus YCoordNeptune
         MinPlanetVelocityThreshold ScaleFactorPlanetSize ConstantG
         EarthYearsCounter LastPlanetErase]


to setup
;
; Initialize Solar Syatem 
    clear-all
;
; Initialize EarthYearsCounter to zero
    set EarthYearsCounter 0
;
; Initialize the beginning mass of the Sun
    set OriginalMassSun 2 * 10 ^ 30
    set MassSun OriginalMassSun
;
; Initialize the relative sizes, orbital radii, positions, and colors 
; for the Sun and the planets
    set SizeSun      40
    set SizeMercury   5
    set SizeVenus    12
    set SizeEarth    13
    set SizeMars      7
    set SizeJupiter 143
    set SizeSaturn  121
    set SizeUranus   51
    set SizeNeptune  49
;
; Scale sizes of planets to accomodate display
    set ScaleFactorPlanetSize (4 - 1) / (143 - 5)
    set SizeMercury SizeMercury * ScaleFactorPlanetSize + 2
    set SizeVenus   SizeVenus   * ScaleFactorPlanetSize + 2
    set SizeEarth   Sizeearth   * ScaleFactorPlanetSize + 2
    set SizeMars    SizeMars    * ScaleFactorPlanetSize + 2
    set SizeJupiter SizeJupiter * ScaleFactorPlanetSize + 2
    set SizeSaturn  SizeSaturn  * ScaleFactorPlanetSize + 2
    set SizeUranus  SizeUranus  * ScaleFactorPlanetSize + 2
    set SizeNeptune SizeNeptune * ScaleFactorPlanetSize + 2
;
; True orbital radii (m km)
; E.g., True orbital radius of Mercury = 58 x 10^9 m
    set TrueOrbitalRadiusMercury   58
    set TrueOrbitalRadiusVenus    108
    set TrueOrbitalRadiusEarth    150
    set TrueOrbitalRadiusMars     228
    set TrueOrbitalRadiusJupiter  778
    set TrueOrbitalRadiusSaturn  1427
    set TrueOrbitalRadiusUranus  2871
    set TrueOrbitalRadiusNeptune 4497
;
; Compress OrbitalRadii to accomodate display
    set DisplayOrbitalRadiusMercury log TrueOrbitalRadiusMercury 1.01    ; 408
    set DisplayOrbitalRadiusVenus   log TrueOrbitalRadiusVenus   1.01    ; 471
    set DisplayOrbitalRadiusEarth   log TrueOrbitalRadiusEarth   1.01    ; 504
    set DisplayOrbitalRadiusMars    log TrueOrbitalRadiusMars    1.01    ; 546
    set DisplayOrbitalRadiusJupiter log TrueOrbitalRadiusJupiter 1.01    ; 669
    set DisplayOrbitalRadiusSaturn  log TrueOrbitalRadiusSaturn  1.01    ; 730
    set DisplayOrbitalRadiusUranus  log TrueOrbitalRadiusUranus  1.01    ; 800
    set DisplayOrbitalRadiusNeptune log TrueOrbitalRadiusNeptune 1.01    ; 845
;
; Initialize orbital position degrees to zero
    set DegreesMercury 0
    set DegreesVenus   0
    set DegreesEarth   0
    set DegreesMars    0
    set DegreesJupiter 0
    set DegreesSaturn  0
    set DegreesUranus  0
    set DegreesNeptune 0
;
;Initialize orbital velocities to zero
    set OrbitalVelocityMercury 0 
    set OrbitalVelocityVenus   0
    set OrbitalVelocityEarth   0
    set OrbitalVelocityMars    0
    set OrbitalVelocityJupiter 0
    set OrbitalVelocitySaturn  0
    set OrbitalVelocityUranus  0
    set OrbitalVelocityNeptune 0
;    
; Create Sun and eight planets
    create-turtles 1     ; Sun
     [set color 45
      set xcor 0
      set ycor 0
      set shape "dot"
      set size SizeSun]
      create-turtles 1     ; Mercury
     [set color 24
      set xcor (max-pxcor) / 1000 * DisplayOrbitalRadiusMercury
      set ycor 0
      set shape "dot"
      set size SizeMercury
      set pen-size 0.0001
      pen-down]
      create-turtles 1     ; Venus
     [set color 35
      set xcor (max-pxcor) / 1000 * DisplayOrbitalRadiusVenus
      set ycor 0
      set shape "dot"
      set size SizeVenus
      set pen-size 0.0001
      pen-down]
    create-turtles 1     ; Earth
     [set color 73
      set xcor (max-pxcor) / 1000 * DisplayOrbitalRadiusEarth
      set ycor 0
      set shape "dot"
      set size SizeEarth
      set pen-size 0.0001
      pen-down]
      create-turtles 1     ; Mars
     [set color 15
      set xcor (max-pxcor) / 1000 * DisplayOrbitalRadiusMars
      set ycor 0
      set shape "dot"
      set size SizeMars
      set pen-size 0.0001
      pen-down]
      create-turtles 1     ; Jupiter
     [set color 33
      set xcor (max-pxcor) / 1000 * DisplayOrbitalRadiusJupiter
      set ycor 0
      set shape "dot"
      set size SizeJupiter
      set pen-size 0.0001
      pen-down]
      create-turtles 1     ; Saturn
     [set color 125
      set xcor (max-pxcor) / 1000 * DisplayOrbitalRadiusSaturn
      set ycor 0
      set shape "dot"
      set size SizeSaturn
      set pen-size 0.0001
      pen-down]
    create-turtles 1     ; Uranus
     [set color 95
      set xcor (max-pxcor) / 1000 * DisplayOrbitalRadiusUranus
      set ycor 0
      set shape "dot"
      set size SizeUranus
      set pen-size 0.0001
      pen-down]
      create-turtles 1     ; Neptune
     [set color 113
      set xcor (max-pxcor) / 1000 * DisplayOrbitalRadiusNeptune
      set ycor 0
      set shape "dot"
      set size SizeNeptune
      set pen-size 0.0001
      pen-down]
;
; Initialize flag for erasing the last planet
    set LastPlanetErase 0
;
; Set up Plots
    setup-plot
;
end


to rotateplanets
;  
; Update the simulation view - rotate the planets multiple Earth-years,
; until "paused" manually or "stopped" by the disappearance of all of the planets
  loop [
; 
; Don't update Sun size and mass during erasure of Mercury orbit
  if (LastPlanetErase = 0)
  [
;
; Update the mass of the Sun
    set MassSunM1 MassSun
    set MassSun (MassSun * (100 - AnnualSunMassLossPercent) / 100)
;
; Update display size of the Sun
; Size (radius) of Sun reduces as the cube-root of the mass (~volume) reduces
    set SizeSun SizeSun * ((MassSun ^ (1 / 3)) / (MassSunM1 ^ (1 / 3)))
    ask turtle 0 [set size SizeSun]
  ] 
;
; At 0% Sun mass loss, 360/IncDegreesEarth = 360/0.1139 = 3160 updates per revolution
;
    repeat 3160  ; 3160 angular increments per one revolution of the Earth 
                 ; (one present-day Earth-year)
    [
;
; Compute new orbital rotation velocities for each planet
; Velocity = sqrt ( G x MassSun / OrbitalRadius )     
; G = 6.67x10^-11  m^3/kgsec^2
; m/s = sqrt(m^2/s^2) = sqrt(((m^3)/(kg s^2))*(kg)/(m/s)))
;
    set ConstantG 6.67 * 10 ^ -11
;   
    set OrbitalVelocityMercury 
      sqrt ( ( ConstantG * MassSun ) / (TrueOrbitalRadiusMercury * 10 ^ 9) )
    set OrbitalVelocityVenus   
      sqrt ( ( ConstantG * MassSun ) / (TrueOrbitalRadiusVenus   * 10 ^ 9) )
    set OrbitalVelocityEarth   
      sqrt ( ( ConstantG * MassSun ) / (TrueOrbitalRadiusEarth   * 10 ^ 9) )
    set OrbitalVelocityMars    
      sqrt ( ( ConstantG * MassSun ) / (TrueOrbitalRadiusMars    * 10 ^ 9) )
    set OrbitalVelocityJupiter 
      sqrt ( ( ConstantG * MassSun ) / (TrueOrbitalRadiusJupiter * 10 ^ 9) )
    set OrbitalVelocitySaturn  
      sqrt ( ( ConstantG * MassSun ) / (TrueOrbitalRadiusSaturn  * 10 ^ 9) )
    set OrbitalVelocityUranus  
      sqrt ( ( ConstantG * MassSun ) / (TrueOrbitalRadiusUranus  * 10 ^ 9) )
    set OrbitalVelocityNeptune 
      sqrt ( ( ConstantG * MassSun ) / (TrueOrbitalRadiusNeptune * 10 ^ 9) )
;    
; Initialize "Plot" orbital velocities
    set PlotOrbitalVelocityMercury OrbitalVelocityMercury  
    set PlotOrbitalVelocityVenus   OrbitalVelocityVenus      
    set PlotOrbitalVelocityEarth   OrbitalVelocityEarth    
    set PlotOrbitalVelocityMars    OrbitalVelocityMars    
    set PlotOrbitalVelocityJupiter OrbitalVelocityJupiter 
    set PlotOrbitalVelocitySaturn  OrbitalVelocitySaturn  
    set PlotOrbitalVelocityUranus  OrbitalVelocityUranus  
    set PlotOrbitalVelocityNeptune OrbitalVelocityNeptune 
;   
; Check to see if any planets have exceeded their minimum orbital velocities
; Set flag to plot zero orbital velocity if below threshold    
; (Note: Each orbital velocity threshold is related to a corresponding centrifugal 
; force threshold, which has reached a minimum necessary to hold the planet.)
    if (OrbitalVelocityMercury <= 46759) 
       [set PlotOrbitalVelocityMercury 0]
    if (OrbitalVelocityVenus   <= 34337) 
       [set PlotOrbitalVelocityVenus   0]
    if (OrbitalVelocityEarth   <= 29195) 
       [set PlotOrbitalVelocityEarth   0]
    if (OrbitalVelocityMars    <= 23729) 
       [set PlotOrbitalVelocityMars    0]
    if (OrbitalVelocityJupiter <= 12872) 
       [set PlotOrbitalVelocityJupiter 0]
    if (OrbitalVelocitySaturn  <= 9524) 
       [set PlotOrbitalVelocitySaturn  0]
    if (OrbitalVelocityUranus  <= 6728) 
       [set PlotOrbitalVelocityUranus  0]
    if (OrbitalVelocityNeptune <= 5386) 
       [set PlotOrbitalVelocityNeptune 0]
;
; Configure for fast erase of orbit paths
    if (PlotOrbitalVelocityMercury = 0) 
       [set OrbitalVelocityMercury 10 * OrbitalVelocityMercury]
    if (PlotOrbitalVelocityVenus   = 0) 
       [set OrbitalVelocityVenus   10 * OrbitalVelocityMercury]
    if (PlotOrbitalVelocityEarth   = 0) 
       [set OrbitalVelocityEarth   10 * OrbitalVelocityMercury]
    if (PlotOrbitalVelocityMars    = 0) 
       [set OrbitalVelocityMars    10 * OrbitalVelocityMercury]
    if (PlotOrbitalVelocityJupiter = 0) 
       [set OrbitalVelocityJupiter 10 * OrbitalVelocityMercury]
    if (PlotOrbitalVelocitySaturn  = 0) 
       [set OrbitalVelocitySaturn  10 * OrbitalVelocityMercury]
    if (PlotOrbitalVelocityUranus  = 0) 
       [set OrbitalVelocityUranus  10 * OrbitalVelocityMercury]
    if (PlotOrbitalVelocityNeptune = 0) 
       [set OrbitalVelocityNeptune 10 * OrbitalVelocityMercury]
;
; Calculate incremental degrees of rotation for each planet, for each update
; Incremental Degrees = 360 / ( orbital circumference / orbital velocity ) 
    set IncDegreesMercury 360 / ((TrueOrbitalRadiusMercury * 10 ^ 9 * 2 * pi ) 
        / OrbitalVelocityMercury) 
    set IncDegreesVenus   360 / ((TrueOrbitalRadiusVenus   * 10 ^ 9 * 2 * pi ) 
        / OrbitalVelocityVenus)    
    set IncDegreesEarth   360 / ((TrueOrbitalRadiusEarth   * 10 ^ 9 * 2 * pi ) 
        / OrbitalVelocityEarth)   
    set IncDegreesMars    360 / ((TrueOrbitalRadiusMars    * 10 ^ 9 * 2 * pi ) 
        / OrbitalVelocityMars)   
    set IncDegreesJupiter 360 / ((TrueOrbitalRadiusJupiter * 10 ^ 9 * 2 * pi ) 
        / OrbitalVelocityJupiter)
    set IncDegreesSaturn  360 / ((TrueOrbitalRadiusSaturn  * 10 ^ 9 * 2 * pi ) 
        / OrbitalVelocitySaturn)
    set IncDegreesUranus  360 / ((TrueOrbitalRadiusUranus  * 10 ^ 9 * 2 * pi ) 
        / OrbitalVelocityUranus)
    set IncDegreesNeptune 360 / ((TrueOrbitalRadiusNeptune * 10 ^ 9 * 2 * pi ) 
        / OrbitalVelocityNeptune)
;
; Maintain smooth orbital paths, while speeding-up the simulation, 
; by decreasing the granularity of orbital graphs by a factor of 10^4
    set IncDegreesMercury IncDegreesMercury * 10 ^ 4
    set IncDegreesVenus   IncDegreesVenus   * 10 ^ 4
    set IncDegreesEarth   IncDegreesEarth   * 10 ^ 4
    set IncDegreesMars    IncDegreesMars    * 10 ^ 4
    set IncDegreesJupiter IncDegreesJupiter * 10 ^ 4
    set IncDegreesSaturn  IncDegreesSaturn  * 10 ^ 4
    set IncDegreesUranus  IncDegreesUranus  * 10 ^ 4
    set IncDegreesNeptune IncDegreesNeptune * 10 ^ 4
;
; Calculate update position for each planet
    set DegreesMercury DegreesMercury + IncDegreesMercury
    set XCoordMercury  DisplayOrbitalRadiusMercury  * cos ( DegreesMercury )
    set YCoordMercury  DisplayOrbitalRadiusMercury  * sin ( DegreesMercury )
    set DegreesVenus   DegreesVenus   + IncDegreesVenus
    set XCoordVenus    DisplayOrbitalRadiusVenus    * cos ( DegreesVenus )
    set YCoordVenus    DisplayOrbitalRadiusVenus    * sin ( DegreesVenus )
    set DegreesEarth   DegreesEarth   + IncDegreesEarth
    set XCoordEarth    DisplayOrbitalRadiusEarth    * cos ( DegreesEarth )
    set YCoordEarth    DisplayOrbitalRadiusEarth    * sin ( DegreesEarth )
    set DegreesMars    DegreesMars    + IncDegreesMars
    set XCoordMars     DisplayOrbitalRadiusMars     * cos ( DegreesMars )
    set YCoordMars     DisplayOrbitalRadiusMars     * sin ( DegreesMars )
    set DegreesJupiter DegreesJupiter + IncDegreesJupiter
    set XCoordJupiter  DisplayOrbitalRadiusJupiter  * cos ( DegreesJupiter )
    set YCoordJupiter  DisplayOrbitalRadiusJupiter  * sin ( DegreesJupiter )
    set DegreesSaturn  DegreesSaturn  + IncDegreesSaturn
    set XCoordSaturn   DisplayOrbitalRadiusSaturn   * cos ( DegreesSaturn )
    set YCoordSaturn   DisplayOrbitalRadiusSaturn   * sin ( DegreesSaturn )
    set DegreesUranus  DegreesUranus  + IncDegreesUranus
    set XCoordUranus   DisplayOrbitalRadiusUranus   * cos ( DegreesUranus )
    set YCoordUranus   DisplayOrbitalRadiusUranus   * sin ( DegreesUranus )
    set DegreesNeptune DegreesNeptune + IncDegreesNeptune
    set XCoordNeptune  DisplayOrbitalRadiusNeptune  * cos ( DegreesNeptune )
    set YCoordNeptune  DisplayOrbitalRadiusNeptune  * sin ( DegreesNeptune )
;
; Update the position of each planet; erase orbits of ejected planets
    ifelse (PlotOrbitalVelocityMercury   != 0)
      [ask turtle 1   [set xcor (max-pxcor / 1000) * XCoordMercury  
                       set ycor (max-pycor / 1000) * YCoordMercury]]
      [ask turtle 1   [set xcor (max-pxcor / 1000) * XCoordMercury  
                       set ycor (max-pycor / 1000) * YCoordMercury
                       pen-down set pen-size 2 set color 0]]
    ifelse (PlotOrbitalVelocityVenus     != 0)
      [ask turtle 2   [set xcor (max-pxcor / 1000) * XCoordVenus    
                       set ycor (max-pycor / 1000) * YCoordVenus]]
      [ask turtle 2   [set xcor (max-pxcor / 1000) * XCoordVenus    
                       set ycor (max-pycor / 1000) * YCoordVenus
                       pen-down set pen-size 2 set color 0]]                   
    ifelse (PlotOrbitalVelocityEarth     != 0)
      [ask turtle 3   [set xcor (max-pxcor / 1000) * XCoordEarth    
                       set ycor (max-pycor / 1000) * YCoordEarth]]
      [ask turtle 3   [set xcor (max-pxcor / 1000) * XCoordEarth    
                       set ycor (max-pycor / 1000) * YCoordEarth
                       pen-down set pen-size 2 set color 0]]
    ifelse (PlotOrbitalVelocityMars      != 0)
      [ask turtle 4   [set xcor (max-pxcor / 1000) * XCoordMars     
                       set ycor (max-pycor / 1000) * YCoordMars]]
      [ask turtle 4   [set xcor (max-pxcor / 1000) * XCoordMars     
                       set ycor (max-pycor / 1000) * YCoordMars
                       pen-down set pen-size 2 set color 0]]
    ifelse (PlotOrbitalVelocityJupiter   != 0)
      [ask turtle 5   [set xcor (max-pxcor / 1000) * XCoordJupiter  
                       set ycor (max-pycor / 1000) * YCoordJupiter]]
      [ask turtle 5   [set xcor (max-pxcor / 1000) * XCoordJupiter  
                       set ycor (max-pycor / 1000) * YCoordJupiter
                       pen-down set pen-size 2 set color 0]]
    ifelse (PlotOrbitalVelocitySaturn    != 0)
      [ask turtle 6   [set xcor (max-pxcor / 1000) * XCoordSaturn   
                       set ycor (max-pycor / 1000) * YCoordSaturn ]]
      [ask turtle 6   [set xcor (max-pxcor / 1000) * XCoordSaturn   
                       set ycor (max-pycor / 1000) * YCoordSaturn
                       pen-down set pen-size 2 set color 0]]
    ifelse (PlotOrbitalVelocityUranus    != 0)
      [ask turtle 7   [set xcor (max-pxcor / 1000) * XCoordUranus   
                       set ycor (max-pycor / 1000) * YCoordUranus]]
      [ask turtle 7   [set xcor (max-pxcor / 1000) * XCoordUranus   
                       set ycor (max-pycor / 1000) * YCoordUranus
                       pen-down set pen-size 2 set color 0]]
    ifelse (PlotOrbitalVelocityNeptune   != 0)
      [ask turtle 8   [set xcor (max-pxcor / 1000) * XCoordNeptune  
                       set ycor (max-pycor / 1000) * YCoordNeptune]]
      [ask turtle 8   [set xcor (max-pxcor / 1000) * XCoordNeptune  
                       set ycor (max-pycor / 1000) * YCoordNeptune
                       pen-down set pen-size 2 set color 0]]
;      
   ]  ; end of one present-day Earth-year revolution   
;
; Increment counter of Earth-years, if Mercury is still orbiting  
       if(PlotOrbitalVelocityMercury != 0) 
       [set EarthYearsCounter EarthYearsCounter + 1]
;
; Update plot
    update-plot  
;
; Check for pause
    if Pause [ stop ]

; Erase final planet, Mercury, orbit 
; and stop once all eight planets have left the Solar System
    if(PlotOrbitalVelocityMercury = 0) 
      [set LastPlanetErase LastPlanetErase + 1]
    if(LastPlanetErase > 1) [stop]    
;
  ]  ; end of loop
;
end

to setup-plot
  set-current-plot "Orbital Velocities"
  set-plot-x-range  0 100
  set-plot-y-range  0 100
end

to update-plot
; Plot Sun mass percentage, scaled x 1000  
  set-current-plot-pen "%Sunx1000"
  plot (MassSun / OriginalMassSun * 100) * 1000
; Plot planet velocities in km/s
  set-current-plot-pen "Mercury"
  plot PlotOrbitalVelocityMercury 
  set-current-plot-pen "Venus"
  plot PlotOrbitalVelocityVenus   
  set-current-plot-pen "Earth"
  plot PlotOrbitalVelocityEarth   
  set-current-plot-pen "Mars"     
  plot PlotOrbitalVelocityMars    
  set-current-plot-pen "Jupiter"
  plot PlotOrbitalVelocityJupiter 
  set-current-plot-pen "Saturn"
  plot PlotOrbitalVelocitySaturn  
  set-current-plot-pen "Uranus"
  plot PlotOrbitalVelocityUranus  
  set-current-plot-pen "Neptune"
  plot PlotOrbitalVelocityNeptune 
 
end
@#$#@#$#@
GRAPHICS-WINDOW
451
74
1073
717
32
32
9.42
1
10
1
1
1
0
0
0
1
-32
32
-32
32
0
0
1
ticks

BUTTON
154
155
280
226
Rotate Planets
RotatePlanets
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL

BUTTON
133
76
300
138
Create Solar System
Setup
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL

SLIDER
118
259
337
292
AnnualSunMassLossPercent
AnnualSunMassLossPercent
0
2
0.01
0.01
1
NIL
HORIZONTAL

PLOT
12
321
440
631
Orbital Velocities
Time (Earth-Years)
Velocity (m/s)
0.0
10.0
0.0
10.0
true
true
PENS
"Mercury" 1.0 0 -3844592 true
"Venus" 1.0 0 -6459832 true
"Earth" 1.0 0 -15637942 true
"Mars" 1.0 0 -2674135 true
"Jupiter" 1.0 0 -10402772 true
"Saturn" 1.0 0 -5825686 true
"Uranus" 1.0 0 -13791810 true
"Neptune" 1.0 0 -11783835 true
"%Sunx1000" 1.0 2 -4079321 true

MONITOR
166
655
296
708
Earth-Years Counter
EarthYearsCounter
0
1
13

SWITCH
453
29
556
62
Pause
Pause
1
1
-1000

@#$#@#$#@
WHAT IS IT?
-----------
This is a model for the eventual demise of our Solar System.  
Our Solar System is held in place by a delicate balance of opposing centripetal and centrifugal forces.  As our Sun generates energy by fusing its hydrogen, its loss of mass reduces the centripetal force, necessitating a reduction in the centrifugal force, as manifested by reduced orbital velocities for each of the planets.  As each planet’s orbital velocity falls below a threshold, it is ejected from the Solar System.  When all of the planets have left the confines of the Sun, our Solar System ceases to exist.  

HOW IT WORKS
------------
Each Earth-year, the Sun's mass is updated based on the selected annual percentage mass loss.  The (slower) orbital velocity for each of the planets is updated based on the Sun's new mass.  Planets whose orbital velocities have fallen below their thresholds are erased from the view.

HOW TO USE IT
-------------
The user:
  (1)  selects an annual percentage mass loss for the Sun using a "slider",
  (2)  creates the Solar System by pressing a "button", 
  (3)  sets the Solar system in motion, toward its demise, by pressing a second                "button". and
  (4)  when all of the planets have ejected, the simulation halts, with the final
       elapsed time in Earth-years displayed on a "monitor". 
It is recommended that the user select an annual percentage of Sun mass loss in the range from 0.01% to 1.0%.  Higher values execute instantaneously;  lower values execute in excessive amounts of time.

THINGS TO NOTICE
----------------
Three windows in the view provide real-time data on the progress of the simulation:  
1.  The main window shows the Solar System, with progressively shrink Sun and 
    slowing and ejecting planets.
2.  A "moniter" counts the passage of time in Earth-years.  
3.  A "plot" graphs the declining Sun mass and decreasing orbital velocities.

THINGS TO TRY
-------------
1.  Set the "Pause" slider to on, press the "Create Solar System" button, and then
    press the "Rotate Planets" button to see the relative orbital velocities portrayed,      after the Earth completes one revolution.
2.  Set the "AnnualSunMassLossPercent" slider to different values and engage the
    simulation, to observe the relationship between the rate at which the Sun loses
    mass, and the number of years remaining for our Solar System.
3.  Set the "AnnualSunMassLossPercent" slider to an initial value, engage the
    simulation, and change the sliders value during execution (faster or slower) to
    observe non-linear relationships between the rate at which the Sun loses mass, and
    the number of years remaining for our Solar System.

EXTENDING THE MODEL
-------------------
1.  Add the terminal special effects of the Sun’s gaseous radius extending beyond the 
    inner planets, in the final millions of years, to create a hybrid theoretical view  
    of the end of the Solar System.
2.  Conduct simulation experiments with non-linear rates of annual Sun mass loss, and
    observe the effects on Solar System longevities.
3.  Learn or develop some physics for the selection of the orbital velocity ejection
    thresholds, and incorporate that knowledge into the model.

NETLOGO FEATURES
----------------
Standard.

RELATED MODELS
--------------
None.

CREDITS AND REFERENCES
----------------------
Created by Toby Skinner, at Portland State University, for CS-346, Fall 2011.
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250

airplane
true
0
Polygon -7500403 true true 150 0 135 15 120 60 120 105 15 165 15 195 120 180 135 240 105 270 120 285 150 270 180 285 210 270 165 240 180 180 285 195 285 165 180 105 180 60 165 15

arrow
true
0
Polygon -7500403 true true 150 0 0 150 105 150 105 293 195 293 195 150 300 150

box
false
0
Polygon -7500403 true true 150 285 285 225 285 75 150 135
Polygon -7500403 true true 150 135 15 75 150 15 285 75
Polygon -7500403 true true 15 75 15 225 150 285 150 135
Line -16777216 false 150 285 150 135
Line -16777216 false 150 135 15 75
Line -16777216 false 150 135 285 75

bug
true
0
Circle -7500403 true true 96 182 108
Circle -7500403 true true 110 127 80
Circle -7500403 true true 110 75 80
Line -7500403 true 150 100 80 30
Line -7500403 true 150 100 220 30

butterfly
true
0
Polygon -7500403 true true 150 165 209 199 225 225 225 255 195 270 165 255 150 240
Polygon -7500403 true true 150 165 89 198 75 225 75 255 105 270 135 255 150 240
Polygon -7500403 true true 139 148 100 105 55 90 25 90 10 105 10 135 25 180 40 195 85 194 139 163
Polygon -7500403 true true 162 150 200 105 245 90 275 90 290 105 290 135 275 180 260 195 215 195 162 165
Polygon -16777216 true false 150 255 135 225 120 150 135 120 150 105 165 120 180 150 165 225
Circle -16777216 true false 135 90 30
Line -16777216 false 150 105 195 60
Line -16777216 false 150 105 105 60

car
false
0
Polygon -7500403 true true 300 180 279 164 261 144 240 135 226 132 213 106 203 84 185 63 159 50 135 50 75 60 0 150 0 165 0 225 300 225 300 180
Circle -16777216 true false 180 180 90
Circle -16777216 true false 30 180 90
Polygon -16777216 true false 162 80 132 78 134 135 209 135 194 105 189 96 180 89
Circle -7500403 true true 47 195 58
Circle -7500403 true true 195 195 58

circle
false
0
Circle -7500403 true true 0 0 300

circle 2
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240

cow
false
0
Polygon -7500403 true true 200 193 197 249 179 249 177 196 166 187 140 189 93 191 78 179 72 211 49 209 48 181 37 149 25 120 25 89 45 72 103 84 179 75 198 76 252 64 272 81 293 103 285 121 255 121 242 118 224 167
Polygon -7500403 true true 73 210 86 251 62 249 48 208
Polygon -7500403 true true 25 114 16 195 9 204 23 213 25 200 39 123

cylinder
false
0
Circle -7500403 true true 0 0 300

dot
false
0
Circle -7500403 true true 90 90 120

face happy
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 255 90 239 62 213 47 191 67 179 90 203 109 218 150 225 192 218 210 203 227 181 251 194 236 217 212 240

face neutral
false
0
Circle -7500403 true true 8 7 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Rectangle -16777216 true false 60 195 240 225

face sad
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 168 90 184 62 210 47 232 67 244 90 220 109 205 150 198 192 205 210 220 227 242 251 229 236 206 212 183

fish
false
0
Polygon -1 true false 44 131 21 87 15 86 0 120 15 150 0 180 13 214 20 212 45 166
Polygon -1 true false 135 195 119 235 95 218 76 210 46 204 60 165
Polygon -1 true false 75 45 83 77 71 103 86 114 166 78 135 60
Polygon -7500403 true true 30 136 151 77 226 81 280 119 292 146 292 160 287 170 270 195 195 210 151 212 30 166
Circle -16777216 true false 215 106 30

flag
false
0
Rectangle -7500403 true true 60 15 75 300
Polygon -7500403 true true 90 150 270 90 90 30
Line -7500403 true 75 135 90 135
Line -7500403 true 75 45 90 45

flower
false
0
Polygon -10899396 true false 135 120 165 165 180 210 180 240 150 300 165 300 195 240 195 195 165 135
Circle -7500403 true true 85 132 38
Circle -7500403 true true 130 147 38
Circle -7500403 true true 192 85 38
Circle -7500403 true true 85 40 38
Circle -7500403 true true 177 40 38
Circle -7500403 true true 177 132 38
Circle -7500403 true true 70 85 38
Circle -7500403 true true 130 25 38
Circle -7500403 true true 96 51 108
Circle -16777216 true false 113 68 74
Polygon -10899396 true false 189 233 219 188 249 173 279 188 234 218
Polygon -10899396 true false 180 255 150 210 105 210 75 240 135 240

house
false
0
Rectangle -7500403 true true 45 120 255 285
Rectangle -16777216 true false 120 210 180 285
Polygon -7500403 true true 15 120 150 15 285 120
Line -16777216 false 30 120 270 120

leaf
false
0
Polygon -7500403 true true 150 210 135 195 120 210 60 210 30 195 60 180 60 165 15 135 30 120 15 105 40 104 45 90 60 90 90 105 105 120 120 120 105 60 120 60 135 30 150 15 165 30 180 60 195 60 180 120 195 120 210 105 240 90 255 90 263 104 285 105 270 120 285 135 240 165 240 180 270 195 240 210 180 210 165 195
Polygon -7500403 true true 135 195 135 240 120 255 105 255 105 285 135 285 165 240 165 195

line
true
0
Line -7500403 true 150 0 150 300

line half
true
0
Line -7500403 true 150 0 150 150

pentagon
false
0
Polygon -7500403 true true 150 15 15 120 60 285 240 285 285 120

person
false
0
Circle -7500403 true true 110 5 80
Polygon -7500403 true true 105 90 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 195 90
Rectangle -7500403 true true 127 79 172 94
Polygon -7500403 true true 195 90 240 150 225 180 165 105
Polygon -7500403 true true 105 90 60 150 75 180 135 105

plant
false
0
Rectangle -7500403 true true 135 90 165 300
Polygon -7500403 true true 135 255 90 210 45 195 75 255 135 285
Polygon -7500403 true true 165 255 210 210 255 195 225 255 165 285
Polygon -7500403 true true 135 180 90 135 45 120 75 180 135 210
Polygon -7500403 true true 165 180 165 210 225 180 255 120 210 135
Polygon -7500403 true true 135 105 90 60 45 45 75 105 135 135
Polygon -7500403 true true 165 105 165 135 225 105 255 45 210 60
Polygon -7500403 true true 135 90 120 45 150 15 180 45 165 90

square
false
0
Rectangle -7500403 true true 30 30 270 270

square 2
false
0
Rectangle -7500403 true true 30 30 270 270
Rectangle -16777216 true false 60 60 240 240

star
false
0
Polygon -7500403 true true 151 1 185 108 298 108 207 175 242 282 151 216 59 282 94 175 3 108 116 108

target
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240
Circle -7500403 true true 60 60 180
Circle -16777216 true false 90 90 120
Circle -7500403 true true 120 120 60

tree
false
0
Circle -7500403 true true 118 3 94
Rectangle -6459832 true false 120 195 180 300
Circle -7500403 true true 65 21 108
Circle -7500403 true true 116 41 127
Circle -7500403 true true 45 90 120
Circle -7500403 true true 104 74 152

triangle
false
0
Polygon -7500403 true true 150 30 15 255 285 255

triangle 2
false
0
Polygon -7500403 true true 150 30 15 255 285 255
Polygon -16777216 true false 151 99 225 223 75 224

truck
false
0
Rectangle -7500403 true true 4 45 195 187
Polygon -7500403 true true 296 193 296 150 259 134 244 104 208 104 207 194
Rectangle -1 true false 195 60 195 105
Polygon -16777216 true false 238 112 252 141 219 141 218 112
Circle -16777216 true false 234 174 42
Rectangle -7500403 true true 181 185 214 194
Circle -16777216 true false 144 174 42
Circle -16777216 true false 24 174 42
Circle -7500403 false true 24 174 42
Circle -7500403 false true 144 174 42
Circle -7500403 false true 234 174 42

turtle
true
0
Polygon -10899396 true false 215 204 240 233 246 254 228 266 215 252 193 210
Polygon -10899396 true false 195 90 225 75 245 75 260 89 269 108 261 124 240 105 225 105 210 105
Polygon -10899396 true false 105 90 75 75 55 75 40 89 31 108 39 124 60 105 75 105 90 105
Polygon -10899396 true false 132 85 134 64 107 51 108 17 150 2 192 18 192 52 169 65 172 87
Polygon -10899396 true false 85 204 60 233 54 254 72 266 85 252 107 210
Polygon -7500403 true true 119 75 179 75 209 101 224 135 220 225 175 261 128 261 81 224 74 135 88 99

wheel
false
0
Circle -7500403 true true 3 3 294
Circle -16777216 true false 30 30 240
Line -7500403 true 150 285 150 15
Line -7500403 true 15 150 285 150
Circle -7500403 true true 120 120 60
Line -7500403 true 216 40 79 269
Line -7500403 true 40 84 269 221
Line -7500403 true 40 216 269 79
Line -7500403 true 84 40 221 269

x
false
0
Polygon -7500403 true true 270 75 225 30 30 225 75 270
Polygon -7500403 true true 30 75 75 30 270 225 225 270

@#$#@#$#@
NetLogo 4.1.3
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
default
0.0
-0.2 0 0.0 1.0
0.0 1 1.0 0.0
0.2 0 0.0 1.0
link direction
true
0
Line -7500403 true 150 150 90 180
Line -7500403 true 150 150 210 180

@#$#@#$#@
0
@#$#@#$#@
