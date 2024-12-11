(defrule test
?f<-(init ?x)
=>
(retract ?f)
(printout t "fact: " ?x crlf)
)