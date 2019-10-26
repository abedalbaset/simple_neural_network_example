#this code modified of 9 line codes from this site
#https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1
#these codes modified to use normal for loop instead of matrix process

from numpy import exp, array, random, dot


def nonlin(x, deriv=False):
  if(deriv==True):
     return (x*(1-x))
  return 1/(1+exp(-x))

training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
numinputs=3

#training_set_outputs = array([[0, 1, 1, 0]]).T
training_set_outputs = array([[0, 1, 1, 0]]).T


#print("training_set_outputs =",training_set_outputs[0])
#print("training_set_outputs =",training_set_outputs[1])


#ss=random.seed(1)

synaptic_weights = 2 * random.random((3, 1)) - 1


for reset in range(0,len(synaptic_weights)):
    synaptic_weights[reset]=0.5


print("synaptic_weights =",synaptic_weights)

#def clcoutputs(weightsarr,inputsarr):




for iteration in range(300):
    #output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    output=[0, 0, 0, 0]
    for cnt in range(0,len(training_set_outputs)):
        output[cnt]=0
        for cnin in range(0,numinputs):
            #output[cnt]=output[cnt]+1 / (1 + exp(-((training_set_inputs[cnt][cnin]*synaptic_weights[cnin]))))
            output[cnt]=training_set_inputs[cnt][cnin]*synaptic_weights[cnin]+output[cnt]
        output[cnt]=nonlin(output[cnt])

        err= training_set_outputs[cnt] - output[cnt]

        for cnin in range(0,numinputs):
            #synaptic_weights[cnin]=synaptic_weights[cnin]+training_set_inputs[cnt][cnin]*err[cnt]
            synaptic_weights[cnin]=synaptic_weights[cnin]+training_set_inputs[cnt][cnin]*err


        #print("output[cnt] =",output[cnt])
        #output[cnt]=sumtmp

    #output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))


        #synaptic_weights[cnin] +=sumweights


    #synaptic_weights += dot(training_set_inputs.T,delta_v)


print("final weights =",synaptic_weights)
print(" ----------------------------------- ")

print(1 / (1 + exp(-(dot(array([0, 1, 1]), synaptic_weights))))) #0
print(1 / (1 + exp(-(dot(array([1, 0, 1]), synaptic_weights))))) #1
print(1 / (1 + exp(-(dot(array([1, 1, 1]), synaptic_weights))))) #1
print(1 / (1 + exp(-(dot(array([0, 0, 1]), synaptic_weights))))) #0
