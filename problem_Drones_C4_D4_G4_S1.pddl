(define (problem problem_Drones_C4_D4_G4_S1) (:domain ConnectR_3D_Sparse_Axiomless_NoIntrusion)
  (:objects 
	c0 c1 c2 c3  - coord
)
  (:init

	(plus_one c0 c1) (plus_one c1 c2) (plus_one c2 c3) (plus_three c0 c3) 

	(at_aperture c0 c0 c0)
	(at_agent s0 outC outC outC)
	(at_agent s1 outC outC outC)
	(at_agent s2 outC outC outC)
	(at_agent s3 outC outC outC)
)
(:goal (and
	(at_agent s0 c1 c0 c2)
	(at_agent s1 c0 c3 c3)
	(at_agent s2 c3 c3 c1)
	(at_agent s3 c0 c3 c0)
))
)
