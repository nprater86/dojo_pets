import pets
import ninjas

Rosy = pets.Dog('Rosy','dog','roll over')
Orea = pets.Cat('Oreo','cat','jump')
Snek = pets.Pet('Snek','snake','dig')
Nathan = ninjas.Ninja('Nathan','Prater',Rosy,'peanut butter','kibble')
Aly = ninjas.Ninja('Alyson','Prater',Orea,'catnip','tuna')
Troy = ninjas.Ninja('Troy','Prater',Snek,'chick','mice')

Nathan.feed().walk().bathe()
Aly.feed().walk().bathe()
Troy.feed().walk().bathe()
