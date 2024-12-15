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



(defrule q2_a1
?f<-(answer 2 1 ?x)
?q<-(question 2 ?y)
=>
(retract ?f)
(retract ?q)
(assert (question 9 "Are you willing to learn?"))
)

(defrule q2_a2
?f<-(answer 2 2 ?x)
?q<-(question 2 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 2 "Whoa, that's oldschool! Sounds like it's time for an update."))
)

(defrule q2_a3
?f<-(answer 2 3 ?x)
?q<-(question 2 ?y)
=>
(retract ?f)
(retract ?q)
(assert (question 3 "What can you do?"))
)



(defrule q3_a_any
?f<-(answer 3 ?z ?x)
?q<-(question 3 ?y)
=>
(retract ?f)
(retract ?q)
(assert (question 4 "Sweet! Your're ready to build a site!"))
)



(defrule q4_a_any
?f<-(answer 4 ?z ?x)
?q<-(question 4 ?y)
=>
(retract ?f)
(retract ?q)
(assert (question 5 "Hold it. Just cuz you have the skill, doesn't mean ya got the chops."))
)



(defrule q5_a_any
?f<-(answer 5 ?z ?x)
?q<-(question 5 ?y)
=>
(retract ?f)
(retract ?q)
(assert (question 6 "What's your idea of good code?"))
)



(defrule q6_a1
?f<-(answer 6 1 ?x)
?q<-(question 6 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 3 "Yeah. You're gonna need a developer."))
)

(defrule q6_a2
?f<-(answer 6 2 ?x)
?q<-(question 6 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 3 "Yeah. You're gonna need a developer."))
)

(defrule q6_a3
?f<-(answer 6 3 ?x)
?q<-(question 6 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 3 "Yeah. You're gonna need a developer."))
)

(defrule q6_a4
?f<-(answer 6 4 ?x)
?q<-(question 6 ?y)
=>
(retract ?f)
(retract ?q)
(assert (question 7 "Great. What's your idea of good design?"))
)



(defrule q7_a1
?f<-(answer 7 1 ?x)
?q<-(question 7 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 4 "We're not letting you anywhere near photoshop."))
)

(defrule q7_a2
?f<-(answer 7 2 ?x)
?q<-(question 7 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 4 "We're not letting you anywhere near photoshop."))
)

(defrule q7_a3
?f<-(answer 7 3 ?x)
?q<-(question 7 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 4 "We're not letting you anywhere near photoshop."))
)

(defrule q7_a4
?f<-(answer 7 4 ?x)
?q<-(question 7 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 4 "We're not letting you anywhere near photoshop."))
)

(defrule q7_a5
?f<-(answer 7 5 ?x)
?q<-(question 7 ?y)
=>
(retract ?f)
(retract ?q)
(assert (question 8 "Great. What's your idea of a good social media strategy?"))
)



(defrule q8_a1
?f<-(answer 8 1 ?x)
?q<-(question 1 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 6 "You look great! Go forth with your website brave one!"))
)

(defrule q8_a2
?f<-(answer 8 2 ?x)
?q<-(question 2 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 6 "You look great! Go forth with your website brave one!"))
)

(defrule q8_a3
?f<-(answer 8 3 ?x)
?q<-(question 3 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 6 "You look great! Go forth with your website brave one!"))
)

(defrule q8_a3
?f<-(answer 8 3 ?x)
?q<-(question 3 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 5 "We're not convinced you know what social media is."))
)

(defrule q8_a4
?f<-(answer 8 4 ?x)
?q<-(question 4 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 5 "We're not convinced you know what social media is."))
)

(defrule q8_a5
?f<-(answer 8 5 ?x)
?q<-(question 5 ?y)
=>
(retract ?f)
(retract ?q)
(assert (result 5 "We're not convinced you know what social media is."))
)



;(defrule q_a
;?f<-(answer  ?x)
;?q<-(question  ?y)
;=>
;(retract ?f)
;(retract ?q)
;(assert ())
;)