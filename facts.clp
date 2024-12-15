(deftemplate question
    (slot nr (type NUMBER))
    (slot text (type STRING))
    (multislot possible_answers (type STRING))
)

(deffacts init
    (init)
)