
import crd as test  # using the python file for testing

test.newKeyValue("India",200)

test.newKeyValue("Australia",500,60)

test.readKey("India")

test.readKey("Australia")

#After 1 minute , ttl = 60seconds for Australia
test.readKey("Australia")

test.deleteKey("India")

test.newKeyValue("Zimbabwe",800)

test.newKeyValue("Aravind99",600)  #Testing with numericals in key name

test.newKeyValue("Zimbabwe",700)   #Creating same key with different value

test.updateValue("Zimbabwe",700)   #Update function for updating existing key in db

test.readKey("Zimbabwe")      #Checking if update function reflected

test.readKey("India")      #Checking if deleted key still exists


# We can also add threads to execute this operation

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #based on the operation chosen by user
t1.start()
t1.sleep()

t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #based on the operation chosen by user
t2.start()
t2.sleep()
# We can extend upto n threads
