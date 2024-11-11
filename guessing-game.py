import qiskit
from qiskit import IBMQ
import math

"""
I implement the random number generator at the bottom!

The following RANDOM NUMBER GENERATOR:
                                      is from https://github.com/ozaner/qRNG

qRNG is an open-source quantum random number generator written in python.
It achieves this by using IBM's QISKit API to communicate with any one of their publicly accessible quantum computers:

"""
_circuit = None
_bitCache = ''
def set_provider_as_IBMQ(token: str = None):
    """
    Sets the backend provider to IBMQ with the given account token. Will fall back to a local (simulated) provider if no token is given.
    Parameters:
        token (string): Account token on IBMQ. If no token is given, will fall back to a local provider.
    """
    global provider
    if token == None or '':
        provider = qiskit.BasicAer 
    else: 
        IBMQ.save_account(token)
        IBMQ.load_account()
        provider = IBMQ.get_provider('ibm-q')
 
def _set_qubits(n):
    global _circuit
    qr = qiskit.QuantumRegister(n)
    cr = qiskit.ClassicalRegister(n)
    _circuit = qiskit.QuantumCircuit(qr, cr)
    _circuit.h(qr) # Apply Hadamard gate to qubits
    _circuit.measure(qr,cr) # Collapses qubit to either 1 or 0 w/ equal prob.

_set_qubits(5)
 
def set_backend(backend: str = 'qasm_simulator'):
    """
    Sets the backend to one of the provider's available backends (quantum computers/simulators).
    Parameters:
        backend (string): Codename for the backend. If no backend is given, a default (simulated) backend will be used.
    """
    global _backend
    global provider
    available_backends = provider.backends(backend, filters = lambda x: x.status().operational == True)
    if (backend != '') and (backend in str(available_backends)):
        _backend = provider.get_backend(backend)
    else:
        print(str(backend)+' is not available. Backend is set to qasm_simulator.')
        _backend = qiskit.BasicAer.get_backend('qasm_simulator')
    _set_qubits(_backend.configuration().n_qubits)

# Strips QISKit output to just a bitstring.
def _bit_from_counts(counts):
    return [k for k, v in counts.items() if v == 1][0]

# Populates the bitCache with at least n more bits.
def _request_bits(n):
    global _bitCache
    iterations = math.ceil(n/_circuit.width()*2)
    for _ in range(iterations):
        # Create new job and run the quantum circuit
        job = qiskit.execute(_circuit, _backend, shots=1)
        _bitCache += _bit_from_counts(job.result().get_counts())

def get_bit_string(n: int) -> str:
    """
    Returns a random n-bit bitstring.
    Parameters:
        n (int): Account token on IBMQ. If no token is given, will fall back to a local provider.
    """
    global _bitCache
    if len(_bitCache) < n:
        _request_bits(n-len(_bitCache))
    bitString = _bitCache[0:n]
    _bitCache = _bitCache[n:]
    return bitString

# Running time is probabalistic but complexity is still O(n)
def get_random_int(min: int, max: int) -> int:
    """
    Returns a random int from [min, max] (bounds are inclusive).
    Parameters:
        min (int): The minimum possible returned integer.
        max (int): The maximum possible returned integer.
    """
    delta = max-min
    n = math.floor(math.log(delta,2))+1
    result = int(get_bit_string(n),2)
    while(result > delta):
        result = int(get_bit_string(n),2)
    result += min
    return result



"""
    **********MY CODE STARTS HERE**********    
"""


# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = get_random_int(lower, upper)
print("\n\tYou've only ",round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ", count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")