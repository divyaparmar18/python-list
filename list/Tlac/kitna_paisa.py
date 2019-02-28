kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
counter = 0
crorepati = 0
lakhpati=0
dilwale=0
print len(kitna_paisa_hai)
while counter < len(kitna_paisa_hai):
    if kitna_paisa_hai[counter] >= 10000000:
        crorepati=crorepati+1
    elif kitna_paisa_hai[counter]<= 100000:
        lakhpati=lakhpati+1
    else:
        dilwale=dilwale+1
    counter=counter+1
print "There are " + str(crorepati) + " crorepati in the list"
print "There are " + str(lakhpati) + " lakhpati in the list"
print "There are " + str(dilwale) + " dilwale in the list"