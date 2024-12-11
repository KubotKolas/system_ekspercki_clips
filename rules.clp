(defrule q1_a1
?f<-(answer 1 1 ?x)
?q<-(question 1 ?y)
=>
(retract ?f)
(retract ?q)
(assert (question 2 "Do you have any web related skills?"))
)

(defrule q1_a2
?f<-(answer 1 2 ?x)
?q<-(question 1 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 1 "No idea, no dice."))
)