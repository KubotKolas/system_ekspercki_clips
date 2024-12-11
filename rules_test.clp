(defrule test
?f<-(init ?x)
=>
(retract ?f)
(assert (res ?x))
)