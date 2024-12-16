(deftemplate question
    (slot nr (type NUMBER))
    (slot text (type STRING))
    (multislot possible_answers (type STRING))
)

(deffacts init
    (init)
)

(defrule init
?f<-(init)
=>
(retract ?f)
(assert (question (nr 1) (text "So, you've got an awesome idea for a website?") (possible_answers "Sure do!" "Nope.")))
)

(defrule q1_a1
?f<-(answer 1 1 ?)
?q<-(question (nr 1))
=>
(retract ?f)
(retract ?q)
(assert (question (nr 2) (text "Do you have any web related skills?") (possible_answers "Nope." "I know a little dreamweaver!" "Yeah totally.")))
)

(defrule q1_a2
?f<-(answer 1 2 ?)
?q<-(question (nr 1))
=>
(retract ?f)
(retract ?q)
(assert (result 1 "No idea, no dice."))
)



(defrule q2_a1
?f<-(answer 2 1 ?)
?q<-(question (nr 2))
=>
(retract ?f)
(retract ?q)
(assert (question (nr 9) (text "Are you willing to learn?") (possible_answers "Nope." "Yeah totally.")))
)

(defrule q2_a2
?f<-(answer 2 2 ?)
?q<-(question (nr 2))
=>
(retract ?f)
(retract ?q)
(assert (result 2 "Whoa, that's oldschool! Sounds like it's time for an update."))
)

(defrule q2_a3
?f<-(answer 2 3 ?)
?q<-(question (nr 2))
=>
(retract ?f)
(retract ?q)
(assert (question (nr 3) (text "What can you do?") (possible_answers "I can code!" "I can design!" "I'm a social media genius!")))
)



(defrule q3_a_any
?f<-(answer 3 ? ?)
?q<-(question (nr 3))
=>
(retract ?f)
(retract ?q)
(assert (question (nr 4) (text "Sweet! Your're ready to build a site!") (possible_answers "Nice!")))
)



(defrule q4_a_any
?f<-(answer 4 ? ?)
?q<-(question (nr 4))
=>
(retract ?f)
(retract ?q)
(assert (question (nr 5) (text "Hold it. Just cuz you have the skill, doesn't mean ya got the chops.") (possible_answers "Huh?")))
)



(defrule q5_a_any
?f<-(answer 5 ? ?)
?q<-(question (nr 5))
=>
(retract ?f)
(retract ?q)
(assert (question (nr 6) (text "What's your idea of good code?") (possible_answers "Naming variables after my pets." "Copy and paste from Stack Overflow." "Lots and lots of nested tables." "Scalable, well-commented. seamlessly integrated")))
)



(defrule q6_a1
?f<-(answer 6 1 ?)
?q<-(question (nr 6))
=>
(retract ?f)
(retract ?q)
(assert (result 3 "Yeah. You're gonna need a developer."))
)

(defrule q6_a2
?f<-(answer 6 2 ?)
?q<-(question (nr 6))
=>
(retract ?f)
(retract ?q)
(assert (result 3 "Yeah. You're gonna need a developer."))
)

(defrule q6_a3
?f<-(answer 6 3 ?)
?q<-(question (nr 6))
=>
(retract ?f)
(retract ?q)
(assert (result 3 "Yeah. You're gonna need a developer."))
)

(defrule q6_a4
?f<-(answer 6 4 ?)
?q<-(question (nr 6))
=>
(retract ?f)
(retract ?q)
(assert (question (nr 7) (text "Great. What's your idea of good design?") (possible_answers "Rounded corners and plenty of gloss." "The more fonts, the merrier." "I dream of geocities." "Starbursts and drop shadows." "Clear hierarchy, beautiful interactions, thoughtful styling")))
)



(defrule q7_a1
?f<-(answer 7 1 ?)
?q<-(question (nr 7))
=>
(retract ?f)
(retract ?q)
(assert (result 4 "We're not letting you anywhere near photoshop."))
)

(defrule q7_a2
?f<-(answer 7 2 ?)
?q<-(question (nr 7))
=>
(retract ?f)
(retract ?q)
(assert (result 4 "We're not letting you anywhere near photoshop."))
)

(defrule q7_a3
?f<-(answer 7 3 ?)
?q<-(question (nr 7))
=>
(retract ?f)
(retract ?q)
(assert (result 4 "We're not letting you anywhere near photoshop."))
)

(defrule q7_a4
?f<-(answer 7 4 ?)
?q<-(question (nr 7))
=>
(retract ?f)
(retract ?q)
(assert (result 4 "We're not letting you anywhere near photoshop."))
)

(defrule q7_a5
?f<-(answer 7 5 ?)
?q<-(question (nr 7))
=>
(retract ?f)
(retract ?q)
(assert (question (nr 8) (text "Great. What's your idea of a good social media strategy?") (possible_answers "Finding and seeding brand content in appropriate channels." "Building engaging conversations around my launch." "Just feel every page with share buttons." "Spamming followers with sponsored links." "Making lots of twitter accounts to retweet myself.")))
)



(defrule q8_a1
?f<-(answer 8 1 ?)
?q<-(question (nr 8))
=>
(retract ?f)
(retract ?q)
(assert (result 6 "You look great! Go forth with your website brave one!"))
)

(defrule q8_a2
?f<-(answer 8 2 ?)
?q<-(question (nr 8))
=>
(retract ?f)
(retract ?q)
(assert (result 6 "You look great! Go forth with your website brave one!"))
)

(defrule q8_a3
?f<-(answer 8 3 ?)
?q<-(question (nr 8))
=>
(retract ?f)
(retract ?q)
(assert (result 5 "We're not convinced you know what social media is."))
)

(defrule q8_a4
?f<-(answer 8 4 ?)
?q<-(question (nr 8))
=>
(retract ?f)
(retract ?q)
(assert (result 5 "We're not convinced you know what social media is."))
)

(defrule q8_a5
?f<-(answer 8 5 ?)
?q<-(question (nr 8))
=>
(retract ?f)
(retract ?q)
(assert (result 5 "We're not convinced you know what social media is."))
)