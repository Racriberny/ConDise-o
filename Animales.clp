(deffacts hechos-iniciales
 (tiene-pelos)
 (tiene-pezugnas)
 (tiene-cuello-largo))

(defrule mamifero-1
 (tiene-pelos)
 =>
 (assert (es-mamifero)))

(defrule mamifero-2
 (da-lecha)
 =>
 (assert (es-mamifero)))

 (defrule ungulado-1
 (es-mamifero)
 (tiene-pezugnas)
 =>
 (assert (es-ungulado)))

 (defrule ungulado-2
 (rumia)
 (tiene-pezugnas)
 =>
 (assert (es-ungulado)))

 (defrule jirafa
 (es-ungulado)
 (tiene-cuello-largo)
 =>
 (printout t "Es una jirafa" crlf))

 (defrule cebra
 (es-ungulado)
 (tiene-rayas-negras)
 =>
 (printout t "Es una cebra" crlf))

 (deftemplate persona
    (slot edad (type INTEGER)))


