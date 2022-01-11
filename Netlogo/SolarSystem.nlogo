breeds [planets]
turtles-own [mass xvelocity yvelocity accx accy newx newy radius avg-radius radius-ratio oldy orbitcount mylabel]
globals [sun earth mars mercury venus jupiter saturn time scale G display_on NearPlanet dist2jupiter dist2saturn jupiterplot saturnplot]

to setup
    display
    ca
    cc
    set display_on true
    set NearPlanet false
    set Zoom 15 
    set scale 1
    set scale Zoom * screen-edge-x / 150
    set time Speed
    set G 1.205 * 10 ^ (0 - 10)     ;Gravitation constant in units of newton*m^2/kg^2 converted to units of Astronomical Units, 
                                    ;AU and earth masses, Me, giving units of AU^3/(Me sec^2)
    crt 1
    create-planets 7                ;the seventh planet is processed as turtle 7, and is an extra orbiting body, i.e. "comet",
                                    ; that might be affected by other planets, if it gets close enough
    ask planets [set color green]
    set sun turtle 0
    ask sun [
        set color red
        set mass 329390 
        set mylabel "Sun "
        ]
    ask turtles [set shape "circle"]
    set mercury turtle 1
    ask mercury [
        set mass .0549 
        set avg-radius 0.388 
        set mylabel "Mer "
        ]
    set venus turtle 2
    ask venus [
        set mass .8073 
        set avg-radius .722 
        set mylabel "V "
        ]
    set earth turtle 3
    ask earth [
        set mass 1 
        set avg-radius 1.00 
        set mylabel "E "
        set color yellow
        ]
    set mars turtle 4
    ask mars [
        set mass .1065 
        set avg-radius 1.53 
        set mylabel "Mar "
        ]
    set jupiter turtle 5
    ask jupiter [
        set mass 314.5 
        set avg-radius 5.2 
        set mylabel "J "
        ]
    set saturn turtle 6
    ask saturn [
        set mass 94.07 
        set avg-radius 9.54 
        set mylabel "Sat "
        ]

    ask turtle 7 [
        set mass .00001 
        set avg-radius Comet_Start         
        set color white 
        set mylabel "Com "
        set newx avg-radius 
        set newy 0                        ;sets comet at y distance of zero, and at distance from sun specified by the slider
        ]
                            
   ;planets are randomly positioned, except for the comet, but at the correct distance from the sun, in Astromonical Units.  Masses are in earth-masses.
   ;calculations are done with newx and newy as actual coordinates, then translated into NetLogo screen units scaled to show more or fewer planets orbiting, as desired

    ask planets with [who < 7][
                ifelse random 2 = 0 
                    [set newx random avg-radius]
                    [set newx 0 - random avg-radius] 
                ifelse random 2 = 0 
                    [set newy sqrt (avg-radius ^ 2 - newx ^ 2)]
                    [set newy 0 - sqrt (avg-radius ^ 2 - newx ^ 2)]
            ]
    ask planets [
                ifelse abs (newx * scale) > screen-edge-x or abs (newy * scale) > screen-edge-x 
                    [set hidden? true setxy newx * scale newy * scale]
                    [set hidden? false setxy newx * scale newy * scale]
                ] 

    ask planets [set radius sqrt(newx ^ 2 + newy ^ 2) ]
    ifelse ViewLabels = false 
        [ask turtles [set label no-label]]
        [ask planets [set label mylabel]]

    ;Compute the initial velocity in x and y directions to produce an approximate circular orbit of radius calculated above regardless of where start point is.
    ;This comes from a = v^2/r for tangential velocity and a = -G*M/r^2. Solve for v at x = r.  Then v = -sqrt(G*M/r).  Then compute v in x and y directions.
    ;Using sin ((towards-nowrap sun) - 180) and cos ((towards-nowrap sun) - 180) to compute y and x components of velocity, respectively, gives the correct 
    ;sign for the resulting value regardless of which quadrant the planets are located.
    
    ask planets with [who < 7][
        set yvelocity sqrt ((mass-of sun * G) / radius) * sin ((towards-nowrap sun) - 180)
        set xvelocity 0 - sqrt ((mass-of sun * G) / radius) * cos ((towards-nowrap sun) - 180)
         ]
         
    ask turtle 7 [
        set xvelocity 0
                    ;;The higher the Comet_Ellipticity setting the lower the initial velocity relative to that needed for a circular orbit, so the orbit is more elliptical
                    ;;Since the comet can be initially off-screen the towards-nowrap primitive cannot be used.  Since it is always at -90 degrees with xvelocity = 0,
                    ;;the value sin ((towards-nowrap sun) - 180) is always sin (-270).
        set yvelocity sqrt ((mass-of sun * G) / radius) * sin (-270) * ((100 - Comet_Ellipticity) / 100)
            ]
         
        ;compute acceleration in x and y directions due to sun's gravity only
    ask planets [
        set accx 0 - ((newx * mass-of sun * G) / radius ^ 3) 
        set accy 0 - ((newy * mass-of sun * G) / radius ^ 3)
         ]
         
        ;compute acceleration in x and y directions due to gravities of other planets - each planet computes influence of other planets excluding itself
        ;and combine accelerations due to sun and other planets
    if Sun_only = false          ;;switch allows turning off effects of other planets and use gravity of sun only  
                [ask planets [
                    ask planets with [who != who-of myself] [
                        set accx-of myself accx-of myself - (((mass * G ) * (newx-of myself - newx))/(sqrt ( (newx - newx-of myself ) ^ 2 + (newy - newy-of myself) ^ 2)) ^ 3)
                        set accy-of myself accy-of myself - (((mass * G ) * (newy-of myself - newy))/(sqrt ( (newx - newx-of myself ) ^ 2 + (newy - newy-of myself) ^ 2)) ^ 3)
                                                            ]
                            ]
                 ]
        ;compute the average velocity that will apply for the time period used to compute the next position, estimated by computing velocity at one half the time period
        ;and applying it for the entire time period.  The new velocity is the initial velocity plus the acceleration applied over t/2 seconds.
    ask planets [
                set xvelocity xvelocity + accx * time / 2 
                set yvelocity yvelocity + accy * time / 2
                ]
                
    setup-plots
end


to go
   orbit-sun
end


to orbit-sun
    set scale Zoom * screen-edge-x / 150
    ask planets [                                ;;compute new positions for all orbiting bodies
                set newx newx + xvelocity * time  
                set newy newy + yvelocity * time
     ;;hide any turtle whose new position is off-screen
                ifelse abs (newx * scale) > screen-edge-x or abs (newy * scale) > screen-edge-x 
                    [set hidden? true]
                    [set hidden? false 
                     setxy newx * scale newy * scale]
                set radius sqrt(newx ^ 2 + newy ^ 2)
     ;;compute new accelerations for all orbiting bodies based on sun's gravity.  Equations are the same as in setup.
                set accx 0 - ((newx * mass-of sun * G) / radius ^ 3) 
                set accy 0 - ((newy * mass-of sun * G) / radius ^ 3)
   
    if Sun_only = false    ;;unless only the sun's gravity is to be considered, each orbiting body asks all other orbiting bodies for their contribution to its acceleration
                     [ask planets with [who != who-of myself] [
                         set accx-of myself accx-of myself - (((mass * G) * (newx-of myself - newx))/(sqrt ( (newx - newx-of myself ) ^ 2 + (newy - newy-of myself) ^ 2)) ^ 3)
                         set accy-of myself accy-of myself - (((mass * G) * (newy-of myself - newy))/(sqrt ( (newx - newx-of myself ) ^ 2 + (newy - newy-of myself) ^ 2)) ^ 3)
                                                             ]
                      ]
         ]
 
    ask planets [        ;;compute new velocities
                set xvelocity xvelocity + accx * time 
                set yvelocity yvelocity + accy * time
                ]
                
    ifelse ViewLabels = false 
        [ask turtles [set label no-label]]
        [ask planets [set label mylabel]]
        
    ;;If comet comes within .2 AU of Jupiter or Saturn and the display is off, set variable NearPlanet to true, which
    ;;causes the display to be turned on with the comet and planets in their updated positions and then held there for
    ;;two seconds so you can see what has happened and begin following the comet. 
    ;;Also, whether the display is on or not, while the comet is within the specified distance of either Jupiter or
    ;;Saturn, the distance between either or both and the comet is plotted.
       
    ask turtle 7 [
        ;;compute distance between comet and jupiter and saturn
        set dist2jupiter sqrt((newx - newx-of jupiter) ^ 2 + (newy - newy-of jupiter) ^ 2)
        set dist2saturn sqrt((newx - newx-of saturn) ^ 2 + (newy - newy-of saturn) ^ 2)    
            
        ifelse (dist2jupiter) < Comet-Jupiter                          ;if comet is within range of jupiter -
            [if display_on = false                                     ;if display was off, set flag to turn it on below
                [set NearPlanet true]
            if jupiterplot = 0 and saturnplot = 0                      ;if no plot for either Jupiter or Saturn is in progress
              [set-current-plot "Comet - Closest Planet Distance"      ;clear the current plot
               clear-plot
               set jupiterplot 1                                       ;set flag indicating a plot is in progress
               ]
             set-current-plot "Comet - Closest Planet Distance"
             set-current-plot-pen "Jupiter"                            ;plot distance from comet to Jupiter
             plot dist2jupiter
            ]
            [set jupiterplot 0                                         ;if comet is out of range, set flag indicating no plot in progress
            ]
        ifelse (dist2saturn)  < Comet-Saturn                           ;procedure below is same for Saturn as Jupiter
            [if display_on = false
                  [set NearPlanet true]
            if saturnplot = 0 and jupiterplot = 0
              [set-current-plot "Comet - Closest Planet Distance"
               clear-plot
               set saturnplot 1
               ]
             set-current-plot "Comet - Closest Planet Distance"
             set-current-plot-pen "Saturn"
             plot dist2saturn
            ]
            [set saturnplot 0
            ]
                 ]
    if NearPlanet = true                                                ;check flag to see if display is to be turned on
        [set NearPlanet false                                           ;after a two second delay
         ToggleDisplay
         wait 2]
            
    ask planets [                ;;keep track of number of orbits each planet makes
        if oldy < 0 and newy > 0 
            [set orbitcount orbitcount + 1]
             set oldy newy
                ]
                
    ;ask planets [set oldy newy]
    
    ;;keep track of ratio of current radius to initial average radius for both earth and comet so they can be plotted
    ask earth [set radius-ratio ((radius  / (avg-radius)))]
    ask turtle 7 [set radius-ratio ((radius  / (avg-radius)))]

    if Plotting = true [do-plot]
end         
            
to do-plot
  set-current-plot "Earth - Sun Distance"
  ask earth [set-current-plot-pen "radius-ratio earth"]
  ask earth [plot radius-ratio]
  set-current-plot "Comet - Sun Distance"
  ask turtle 7 [set-current-plot-pen "radius-ratio turtle 7"]
  ask turtle 7 [plot radius-ratio]
end


to setup-plots
  set-current-plot "Comet - Sun Distance"
  set-plot-y-range .8 1.2
  set-plot-x-range 0 1000
  set-current-plot "Earth - Sun Distance"
  ifelse Sun_Only = true    ;;scale the earth orbit plot based on anticipated ranges.  Determined by previous observations
      [set-plot-y-range precision (1 - (time)/ 10000) 4 precision (1 + (2 * time)/ 10000) 4]
      [set-plot-y-range precision (1 - (2 * sqrt(time))/ 1000) 4 precision (1 + (2 * sqrt(time))/ 1000) 4]
  set-plot-x-range 0 1000
  set-current-plot "Comet - Closest Planet Distance"
  set-plot-y-range 0 1
  set-plot-x-range 0 1000
end

to ToggleDisplay               
    ifelse display_on = true
        [no-display set display_on false]
        [display set display_on true]
end
               


@#$#@#$#@
GRAPHICS-WINDOW
423
10
1037
645
75
75
4.0
1
10
1
1

CC-WINDOW
697
656
1008
793
Command Center

BUTTON
44
52
125
85
Setup
Setup
NIL
1
T
OBSERVER

BUTTON
236
55
317
88
Go
Go
T
1
T
OBSERVER

PLOT
10
655
296
879
Comet - Sun Distance
Time
Distance/Init. Distance
0.0
10.0
0.5
1.2
true
false
PENS
"radius-ratio turtle 7" 1.0 0 -16777216 true

MONITOR
14
367
162
416
Earth years
orbitcount-of earth
0
1

SWITCH
237
275
365
308
ViewLabels
ViewLabels
1
1
-1000

SLIDER
235
142
407
175
Zoom
Zoom
1
100
15
1
1
NIL

SLIDER
7
103
168
136
Speed
Speed
1
10
10
1
1
NIL

SWITCH
237
188
340
221
Plotting
Plotting
0
1
-1000

PLOT
11
428
295
643
Earth - Sun Distance
Time
Distance/Init. Distance
0.0
10.0
0.995
1.005
true
false
PENS
"radius-ratio earth" 1.0 0 -16777216 true

SWITCH
237
233
350
266
Sun_only
Sun_only
1
1
-1000

SLIDER
9
188
181
221
Comet_Ellipticity
Comet_Ellipticity
0
100
10
1
1
NIL

SLIDER
8
147
180
180
Comet_Start
Comet_Start
1
40
7.8
0.1
1
NIL

BUTTON
236
97
357
130
Display On/Off
ToggleDisplay
NIL
1
T
OBSERVER

PLOT
316
654
647
877
Comet - Closest Planet Distance
Time
AU
0.0
100.0
0.0
1.0
true
true
PENS
"Jupiter" 1.0 0 -44544 true
"Saturn" 1.0 0 -8716033 true

SLIDER
238
321
410
354
Comet-Jupiter
Comet-Jupiter
0
3
3.0
0.2
1
NIL

SLIDER
236
368
408
401
Comet-Saturn
Comet-Saturn
0
3
3.0
0.2
1
NIL

@#$#@#$#@
This model mimics the solar system.  Setup creates the sun, five planets, and a "comet".  Unlike in the real solar system, 
these orbiting bodies are in the same plane, and setup distributes the planets randomly.  However, the planets are at the 
correct relative distances from the sun and have correct relative masses.  The comet can be placed up to 100 AU (an AU is 
the distance from earth to sun, or Astronomical Unit) from the sun and assigned an "ellipticity" which adjusts its initial 
velocity to result in a orbit that can range from a circle to an extreme ellipse.

As the model is run, the ratio of the current distance from the sun to the initial distance can be plotted for earth and
the comet.  If the gravitational effects of all planets, in addition to the sun, are computed, earth's orbit can be seen to
vary slightly in ellipticity.  If only the sun's gravity is considered, earth's orbit is still elliptical, but does not vary.
The orbit of the comet can vary greatly, depending upon how close and at what speed it approaches other planets or the sun.
Depending upon the initial positions of the planets and comet, and the comet's ellipticity, the comet could orbit indefinitely,
immediately be ejected from the solar system, or be knocked around into other orbits before being ejected.

The third plot, "Comet - Closest Planet Distance" plots the distance from the comet to Jupiter and/or Saturn when the distance 
between them is within the range set on the sliders "Comet-Jupiter" and "Comet-Saturn" in AU.  Whenever the comet comes within 
this range of either planet, if a plot for neither planet was already in progress, the previous plot is cleared and a new one 
started.  This can give a good view of how the comet is moving with respect to these planets, and how close it actually gets, 
when within the specified ranges.

To Run the Model

	Just press Setup to use the default speed, distance of comet to sun, and comet orbit ellipticity.  Other settings can be
	changed during the run.  Setup resets Zoom to 15, so setting it to another value initially isn't useful.  

	Press Go

	Notes:

	If you want a different speed, initial comet position, and/or ellipticity, make these changes before pressing Setup.  Changing
	these later has no effect. 

	The speed adjustment actually changes the size of time intervals at which the new planet positions are updated. This affects
	the accuracy of the orbits.  At a speed setting of 10 there are about 1000 updates of the position of the earth per
	revolution of the sun, but only about 250 for Mercury.  At a speed setting of 1 there are ten times as many updates per 
	revolution.  The effects of speed settings on the orbit calculations can be seen by setting the Sun_Only switch to "on" and
	observing the orbital plots for both earth and comet at different speed settings.  The ellipticity of the earth's orbit 
	decreases as the number of updates per year increases.  At higher ellipticity settings for the comet, which bring it closer
	to the sun, its orbit should be repetitive if the Sun_Only switch is on, but at higher speed settings it may vary and even
	become unstable due to insufficient updates where the comet's orbital path is making sharp turns.  Note that when the Sun_Only
	switch is "off" so that gravitational effects of the planets as well as the sun on the comet are computed, the comet may 
	come close enough to any planet, or the sun, to cause sufficiently abrupt changes in orbital direction that the time interval 
	represented by higher speed settings may be too large to compute its orbit correctly.  Also, no provision has been made to 
	note the "collision" of the comet with a planet or the sun, so the resulting acceleration will almost certainly fling the 
	comet out of the solar system.

	Setting the comet's initial distance from the sun to be near that of Saturn or Jupiter makes it easy to see the effects of these
	large planets on the comet's orbit.  The farther out the comet starts, the longer it is likely to take to see an obvious 
	interaction with a planet.

	The Earth - Sun Distance plot is scaled according to whether the Sun_Only switch is on and the current Speed setting, so that
	the changes are easily visible.  The scaling is based on trial and error observation.

While the Model is Running

	To increase the speed of execution without affecting computation accuracy, turn the display off by pressing Display On/Off.
	This is a toggle which alternately stops the display from showing the changing planet positions, or resumes showing their
	positions.  When the display is off, you can follow the progress by looking at the "earth years" monitor which tracks the
	number of orbits earth has made, and by looking at the plots of the earth's and comet's orbits.

	You can change the distance between the comet and Jupiter and the comet and Saturn, with sliders "Comet-Jupiter" and 
	"Comet-Saturn", which will trigger the following:

		If the display is off and the comet approaches within the slider set distances of either Jupiter or Saturn, 
		the display is turned on and execution is stopped for two seconds to aid in starting to visually track the comet's 
		orbit from that point.

		The "Comet - Closest Planet Distance" plot will show the distance between comet and Jupiter and/or comet and Saturn,
		either, or both as long as the distance is less than the slider setting.  If the distance to either planet comes
		within range and a plot is not already in progress, the previous plot is cleared and a new one started.  This is
		independent of whether the display was on or off.

	To follow a comet's orbit when it goes off-screen, lower the Zoom value.  Otherwise, when any orbiting body passes off-
	screen, it is hidden until it comes back on-screen.  Also, if you increase the Zoom setting so that you view fewer planets,
	say only through Mars, execution speed increases.

	The Plotting On/Off switch is obvious.

	The Labels On/Off switch, can be used to display a label for each object in the solar system.  The model then runs much slower.

	The Sun_Only switch can be used to observe how the planets' orbits behave when all gravitational interactions are computed, or
	when only the sun's gravitational pull is computed.  For example, the comet's orbit will not be affected by close encounters
	with any of the planets when the Sun_Only switch is "on".

Calculations
	
	Computing the acceleration of object #1 towards object #2 due to gravity:

		From F = ma = -GMm/r^2 and solving for the x and y components of acceleration a we get accx = -GMx/r^3 and accy = -GMy/r^3
		where accx and accy are the accelerations in the x and y directions, x and y are the distances in x and y directions between
		the objects #1 and #2, M is the mass of object #2 (the mass m of object #1 cancels out), G is the gravitational constant, and 
		r = sqrt(x^2 + y^2). G is expressed in terms of Astronomical Units, AU and earth masses, Me, giving units of AU^3/(Me sec^2).

	Computing the inital conditions

		After the planets are randomly placed at their proper orbiting distances from the sun, the initial velocities are computed
		from the equation v = -sqrt(G*M/r) where v = tangential velocity.  The velocities in the x and y directions are then
		x-velocity = v * sin (angle) and y-velocity = v * cos (angle) where angle is reported from (towards-nowrap sun - 180).		

		The initial accelerations are computed as described above, with each planet having the effects of the sun's and all the other 
		planets' gravity on itself computed.

		At each time interval a new x and y position for each planet and the comet is computed based on the x and y velocities for
		that time period.  Since the velocities at the beginning of the time interval increase by (acceleration * time) the
		average velocity for each time period is used.  For the first time period this is computed by adding to the initial velocity
		the acceleration * time/2.

	Updating planets' and comet's positions

		This is just a matter of repeating the computations above of new accelerations added to current velocities in x and y
		directions.






@#$#@#$#@
default
true
0
Polygon -7566196 true true 150 5 40 250 150 205 260 250

ant
true
0
Polygon -7566196 true true 136 61 129 46 144 30 119 45 124 60 114 82 97 37 132 10 93 36 111 84 127 105 172 105 189 84 208 35 171 11 202 35 204 37 186 82 177 60 180 44 159 32 170 44 165 60
Polygon -7566196 true true 150 95 135 103 139 117 125 149 137 180 135 196 150 204 166 195 161 180 174 150 158 116 164 102
Polygon -7566196 true true 149 186 128 197 114 232 134 270 149 282 166 270 185 232 171 195 149 186 149 186
Polygon -7566196 true true 225 66 230 107 159 122 161 127 234 111 236 106
Polygon -7566196 true true 78 58 99 116 139 123 137 128 95 119
Polygon -7566196 true true 48 103 90 147 129 147 130 151 86 151
Polygon -7566196 true true 65 224 92 171 134 160 135 164 95 175
Polygon -7566196 true true 235 222 210 170 163 162 161 166 208 174
Polygon -7566196 true true 249 107 211 147 168 147 168 150 213 150
Polygon -7566196 true true 270 14
Polygon -7566196 true true 276 21

arrow
true
0
Polygon -7566196 true true 150 0 0 150 105 150 105 293 195 293 195 150 300 150

bee
true
0
Polygon -256 true false 151 152 137 77 105 67 89 67 66 74 48 85 36 100 24 116 14 134 0 151 15 167 22 182 40 206 58 220 82 226 105 226 134 222
Polygon -16777216 true false 151 150 149 128 149 114 155 98 178 80 197 80 217 81 233 95 242 117 246 141 247 151 245 177 234 195 218 207 206 211 184 211 161 204 151 189 148 171
Polygon -7566196 true true 246 151 241 119 240 96 250 81 261 78 275 87 282 103 277 115 287 121 299 150 286 180 277 189 283 197 281 210 270 222 256 222 243 212 242 192
Polygon -16777216 true false 115 70 129 74 128 223 114 224
Polygon -16777216 true false 89 67 74 71 74 224 89 225 89 67
Polygon -16777216 true false 43 91 31 106 31 195 45 211
Line -1 false 200 144 213 70
Line -1 false 213 70 213 45
Line -1 false 214 45 203 26
Line -1 false 204 26 185 22
Line -1 false 185 22 170 25
Line -1 false 169 26 159 37
Line -1 false 159 37 156 55
Line -1 false 157 55 199 143
Line -1 false 200 141 162 227
Line -1 false 162 227 163 241
Line -1 false 163 241 171 249
Line -1 false 171 249 190 254
Line -1 false 192 253 203 248
Line -1 false 205 249 218 235
Line -1 false 218 235 200 144

bird1
false
0
Polygon -7566196 true true 2 6 2 39 270 298 297 298 299 271 187 160 279 75 276 22 100 67 31 0

bird2
false
0
Polygon -7566196 true true 2 4 33 4 298 270 298 298 272 298 155 184 117 289 61 295 61 105 0 43

boat1
false
0
Polygon -1 true false 63 162 90 207 223 207 290 162
Rectangle -6524078 true false 150 32 157 162
Polygon -16776961 true false 150 34 131 49 145 47 147 48 149 49
Polygon -7566196 true true 158 33 230 157 182 150 169 151 157 156
Polygon -7566196 true true 149 55 88 143 103 139 111 136 117 139 126 145 130 147 139 147 146 146 149 55

boat2
false
0
Polygon -1 true false 63 162 90 207 223 207 290 162
Rectangle -6524078 true false 150 32 157 162
Polygon -16776961 true false 150 34 131 49 145 47 147 48 149 49
Polygon -7566196 true true 157 54 175 79 174 96 185 102 178 112 194 124 196 131 190 139 192 146 211 151 216 154 157 154
Polygon -7566196 true true 150 74 146 91 139 99 143 114 141 123 137 126 131 129 132 139 142 136 126 142 119 147 148 147

boat3
false
0
Polygon -1 true false 63 162 90 207 223 207 290 162
Rectangle -6524078 true false 150 32 157 162
Polygon -16776961 true false 150 34 131 49 145 47 147 48 149 49
Polygon -7566196 true true 158 37 172 45 188 59 202 79 217 109 220 130 218 147 204 156 158 156 161 142 170 123 170 102 169 88 165 62
Polygon -7566196 true true 149 66 142 78 139 96 141 111 146 139 148 147 110 147 113 131 118 106 126 71

box
true
0
Polygon -7566196 true true 45 255 255 255 255 45 45 45

butterfly1
true
0
Polygon -16777216 true false 151 76 138 91 138 284 150 296 162 286 162 91
Polygon -7566196 true true 164 106 184 79 205 61 236 48 259 53 279 86 287 119 289 158 278 177 256 182 164 181
Polygon -7566196 true true 136 110 119 82 110 71 85 61 59 48 36 56 17 88 6 115 2 147 15 178 134 178
Polygon -7566196 true true 46 181 28 227 50 255 77 273 112 283 135 274 135 180
Polygon -7566196 true true 165 185 254 184 272 224 255 251 236 267 191 283 164 276
Line -7566196 true 167 47 159 82
Line -7566196 true 136 47 145 81
Circle -7566196 true true 165 45 8
Circle -7566196 true true 134 45 6
Circle -7566196 true true 133 44 7
Circle -7566196 true true 133 43 8

circle
false
0
Circle -7566196 true true 35 35 230

person
false
0
Circle -7566196 true true 155 20 63
Rectangle -7566196 true true 158 79 217 164
Polygon -7566196 true true 158 81 110 129 131 143 158 109 165 110
Polygon -7566196 true true 216 83 267 123 248 143 215 107
Polygon -7566196 true true 167 163 145 234 183 234 183 163
Polygon -7566196 true true 195 163 195 233 227 233 206 159

sheep
false
15
Rectangle -1 true true 90 75 270 225
Circle -1 true true 15 75 150
Rectangle -16777216 true false 81 225 134 286
Rectangle -16777216 true false 180 225 238 285
Circle -16777216 true false 1 88 92

spacecraft
true
0
Polygon -7566196 true true 150 0 180 135 255 255 225 240 150 180 75 240 45 255 120 135

thin-arrow
true
0
Polygon -7566196 true true 150 0 0 150 120 150 120 293 180 293 180 150 300 150

truck-down
false
0
Polygon -7566196 true true 225 30 225 270 120 270 105 210 60 180 45 30 105 60 105 30
Polygon -8716033 true false 195 75 195 120 240 120 240 75
Polygon -8716033 true false 195 225 195 180 240 180 240 225

truck-left
false
0
Polygon -7566196 true true 120 135 225 135 225 210 75 210 75 165 105 165
Polygon -8716033 true false 90 210 105 225 120 210
Polygon -8716033 true false 180 210 195 225 210 210

truck-right
false
0
Polygon -7566196 true true 180 135 75 135 75 210 225 210 225 165 195 165
Polygon -8716033 true false 210 210 195 225 180 210
Polygon -8716033 true false 120 210 105 225 90 210

turtle
true
0
Polygon -7566196 true true 138 75 162 75 165 105 225 105 225 142 195 135 195 187 225 195 225 225 195 217 195 202 105 202 105 217 75 225 75 195 105 187 105 135 75 142 75 105 135 105

wolf
false
0
Rectangle -7566196 true true 15 105 105 165
Rectangle -7566196 true true 45 90 105 105
Polygon -7566196 true true 60 90 83 44 104 90
Polygon -16777216 true false 67 90 82 59 97 89
Rectangle -1 true false 48 93 59 105
Rectangle -16777216 true false 51 96 55 101
Rectangle -16777216 true false 0 121 15 135
Rectangle -16777216 true false 15 136 60 151
Polygon -1 true false 15 136 23 149 31 136
Polygon -1 true false 30 151 37 136 43 151
Rectangle -7566196 true true 105 120 263 195
Rectangle -7566196 true true 108 195 259 201
Rectangle -7566196 true true 114 201 252 210
Rectangle -7566196 true true 120 210 243 214
Rectangle -7566196 true true 115 114 255 120
Rectangle -7566196 true true 128 108 248 114
Rectangle -7566196 true true 150 105 225 108
Rectangle -7566196 true true 132 214 155 270
Rectangle -7566196 true true 110 260 132 270
Rectangle -7566196 true true 210 214 232 270
Rectangle -7566196 true true 189 260 210 270
Line -7566196 true 263 127 281 155
Line -7566196 true 281 155 281 192

wolf-left
false
3
Polygon -6524078 true true 117 97 91 74 66 74 60 85 36 85 38 92 44 97 62 97 81 117 84 134 92 147 109 152 136 144 174 144 174 103 143 103 134 97
Polygon -6524078 true true 87 80 79 55 76 79
Polygon -6524078 true true 81 75 70 58 73 82
Polygon -6524078 true true 99 131 76 152 76 163 96 182 104 182 109 173 102 167 99 173 87 159 104 140
Polygon -6524078 true true 107 138 107 186 98 190 99 196 112 196 115 190
Polygon -6524078 true true 116 140 114 189 105 137
Rectangle -6524078 true true 109 150 114 192
Rectangle -6524078 true true 111 143 116 191
Polygon -6524078 true true 168 106 184 98 205 98 218 115 218 137 186 164 196 176 195 194 178 195 178 183 188 183 169 164 173 144
Polygon -6524078 true true 207 140 200 163 206 175 207 192 193 189 192 177 198 176 185 150
Polygon -6524078 true true 214 134 203 168 192 148
Polygon -6524078 true true 204 151 203 176 193 148
Polygon -6524078 true true 207 103 221 98 236 101 243 115 243 128 256 142 239 143 233 133 225 115 214 114

wolf-right
false
3
Polygon -6524078 true true 170 127 200 93 231 93 237 103 262 103 261 113 253 119 231 119 215 143 213 160 208 173 189 187 169 190 154 190 126 180 106 171 72 171 73 126 122 126 144 123 159 123
Polygon -6524078 true true 201 99 214 69 215 99
Polygon -6524078 true true 207 98 223 71 220 101
Polygon -6524078 true true 184 172 189 234 203 238 203 246 187 247 180 239 171 180
Polygon -6524078 true true 197 174 204 220 218 224 219 234 201 232 195 225 179 179
Polygon -6524078 true true 78 167 95 187 95 208 79 220 92 234 98 235 100 249 81 246 76 241 61 212 65 195 52 170 45 150 44 128 55 121 69 121 81 135
Polygon -6524078 true true 48 143 58 141
Polygon -6524078 true true 46 136 68 137
Polygon -6524078 true true 46 130
Polygon -6524078 true true 45 129 35 142 37 159 53 192 47 210 62 238 80 237
Line -16777216 false 74 237 59 213
Line -16777216 false 59 213 59 212
Line -16777216 false 58 211 67 192
Polygon -6524078 true true 38 138 66 149
Polygon -6524078 true true 46 128 33 120 21 118 11 123 3 138 5 160 13 178 9 192 0 199 20 196 25 179 24 161 25 148 45 140
Polygon -6524078 true true 67 122 96 126 63 144

@#$#@#$#@
NetLogo 1.2beta2
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
