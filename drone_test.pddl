(define (problem drone_test) (:domain derived_drone)
	(objects: 
c0 c1 c2 c3 c4 c5 c6 c7 c8  - coord
)
  (:init
	(plus_one c0 c1) (plus_one c1 c2) (plus_one c2 c3) (plus_one c3 c4) (plus_one c4 c5) (plus_one c5 c6) (plus_one c6 c7) (plus_one c7 c8) 
(plus_three c0 c3) (plus_three c1 c4) (plus_three c2 c5) (plus_three c3 c6) (plus_three c4 c7) (plus_three c5 c8) 
(plus_four c0 c4) (plus_four c1 c5) (plus_four c2 c6) (plus_four c3 c7) (plus_four c4 c8) 
		(at_aperture c2 c0 c2) 
	(at_agent s0 outC outC outC)
	(at_agent s1 outC outC outC)
	(at_agent s2 outC outC outC)
	(at_agent s3 outC outC outC)
	(at_agent s4 outC outC outC)
	(at_agent s5 outC outC outC)
)
(:goal (and
		(at_agent s0 c2 c0 c7) ))
)
