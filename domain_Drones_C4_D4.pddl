(define (domain ConnectR_3D_Sparse_Axiomless_NoIntrusion)
	(:requirements :adl :typing)
	(:types coord - object agent - object)
	(:constants outC - coord s0 s1 s2 s3 - agent)

	(:predicates
		(at_agent ?r - agent ?x ?y ?z - coord)
		;;NOTE:IF MORE THAN ONE APERTURE NEEDED, NEED TO CREATE AN APERTURE OBJECT TO LINK THEM
		(at_aperture ?x ?y ?z - coord)
		(plus_four ?c1 ?c2 - coord)
		(plus_one ?c1 ?c2 - coord)
		(plus_three ?c1 ?c2 - coord)
	)
(:action insert
	:parameters (?rmov - agent ?x2 ?y2 ?z2 - coord)
	:precondition (and
		(at_agent ?rmov outC outC outC)
		(not (= ?x2 outC))
		(not (= ?y2 outC))
		(not (= ?z2 outC))
		;;agent has to be outside for insert
		;;aperture exists
		(at_aperture ?x2 ?y2 ?z2)
			(not (at_agent s0 ?x2 ?y2 ?z2))
			(not (at_agent s1 ?x2 ?y2 ?z2))
			(not (at_agent s2 ?x2 ?y2 ?z2))
			(not (at_agent s3 ?x2 ?y2 ?z2))
	)
	:effect (and
			(not (at_agent ?rmov ?x1 ?y1 ?z1))
			(at_agent ?rmov ?x2 ?y2 ?z2)
	)
)

	(:action walk_plusX
	:parameters (?rmov - agent ?x1 ?y1 ?z1 ?x2 ?y2 ?z2 - coord)
	:precondition (and
		(at_agent ?rmov ?x1 ?y1 ?z1)
			(not (at_agent s0 ?x2 ?y2 ?z2))
			(not (at_agent s1 ?x2 ?y2 ?z2))
			(not (at_agent s2 ?x2 ?y2 ?z2))
			(not (at_agent s3 ?x2 ?y2 ?z2))
		(= ?y2 ?y1)
		(= ?z2 ?z1)
		(plus_one ?x1 ?x2)
		)
	:effect (and
			(not (at_agent ?rmov ?x1 ?y1 ?z1))
			(at_agent ?rmov ?x2 ?y2 ?z2)
	)	
)

	(:action walk_minusX
	:parameters (?rmov - agent ?x1 ?y1 ?z1 ?x2 ?y2 ?z2 - coord)
	:precondition (and
		(at_agent ?rmov ?x1 ?y1 ?z1)
			(not (at_agent s0 ?x2 ?y2 ?z2))
			(not (at_agent s1 ?x2 ?y2 ?z2))
			(not (at_agent s2 ?x2 ?y2 ?z2))
			(not (at_agent s3 ?x2 ?y2 ?z2))
		(= ?y2 ?y1)
		(= ?z2 ?z1)
		(plus_one ?x2 ?x1)
		)
	:effect (and
			(not (at_agent ?rmov ?x1 ?y1 ?z1))
			(at_agent ?rmov ?x2 ?y2 ?z2)
	)	
)

	(:action walk_plusY
	:parameters (?rmov - agent ?x1 ?y1 ?z1 ?x2 ?y2 ?z2 - coord)
	:precondition (and
		(at_agent ?rmov ?x1 ?y1 ?z1)
			(not (at_agent s0 ?x2 ?y2 ?z2))
			(not (at_agent s1 ?x2 ?y2 ?z2))
			(not (at_agent s2 ?x2 ?y2 ?z2))
			(not (at_agent s3 ?x2 ?y2 ?z2))
		(= ?x2 ?x1)
		(= ?z2 ?z1)
		(plus_one ?y1 ?y2)
		)
	:effect (and
			(not (at_agent ?rmov ?x1 ?y1 ?z1))
			(at_agent ?rmov ?x2 ?y2 ?z2)
	)	
)

	(:action walk_minusY
	:parameters (?rmov - agent ?x1 ?y1 ?z1 ?x2 ?y2 ?z2 - coord)
	:precondition (and
		(at_agent ?rmov ?x1 ?y1 ?z1)
			(not (at_agent s0 ?x2 ?y2 ?z2))
			(not (at_agent s1 ?x2 ?y2 ?z2))
			(not (at_agent s2 ?x2 ?y2 ?z2))
			(not (at_agent s3 ?x2 ?y2 ?z2))
		(= ?x2 ?x1)
		(= ?z2 ?z1)
		(plus_one ?y2 ?y1)
		)
	:effect (and
			(not (at_agent ?rmov ?x1 ?y1 ?z1))
			(at_agent ?rmov ?x2 ?y2 ?z2)
	)	
)

	(:action walk_plusZ
	:parameters (?rmov - agent ?x1 ?y1 ?z1 ?x2 ?y2 ?z2 - coord)
	:precondition (and
		(at_agent ?rmov ?x1 ?y1 ?z1)
			(not (at_agent s0 ?x2 ?y2 ?z2))
			(not (at_agent s1 ?x2 ?y2 ?z2))
			(not (at_agent s2 ?x2 ?y2 ?z2))
			(not (at_agent s3 ?x2 ?y2 ?z2))
		(= ?x2 ?x1)
		(= ?y2 ?y1)
		(plus_one ?z1 ?z2)
		)
	:effect (and
			(not (at_agent ?rmov ?x1 ?y1 ?z1))
			(at_agent ?rmov ?x2 ?y2 ?z2)
	)	
)

	(:action walk_minusZ
	:parameters (?rmov - agent ?x1 ?y1 ?z1 ?x2 ?y2 ?z2 - coord)
	:precondition (and
		(at_agent ?rmov ?x1 ?y1 ?z1)
			(not (at_agent s0 ?x2 ?y2 ?z2))
			(not (at_agent s1 ?x2 ?y2 ?z2))
			(not (at_agent s2 ?x2 ?y2 ?z2))
			(not (at_agent s3 ?x2 ?y2 ?z2))
		(= ?x2 ?x1)
		(= ?y2 ?y1)
		(plus_one ?z2 ?z1)
		)
	:effect (and
			(not (at_agent ?rmov ?x1 ?y1 ?z1))
			(at_agent ?rmov ?x2 ?y2 ?z2)
	)	
)

)
