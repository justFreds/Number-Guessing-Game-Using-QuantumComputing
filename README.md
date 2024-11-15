# Qiskit Aer


[![License](https://img.shields.io/github/license/Qiskit/qiskit-aer.svg?style=popout-square)](https://opensource.org/licenses/Apache-2.0)


**Qiskit** is an open-source framework for working with noisy quantum computers at the level of pulses, circuits, and algorithms.


Qiskit is made up of elements that each work together to enable quantum computing. This element is **Aer**, which provides high-performance quantum computing simulators with realistic noise models.


## Installation


We encourage installing Qiskit via the pip tool (a python package manager). The following command installs the core Qiskit components, including Aer.


```bash
pip install qiskit qiskit-aer
```


Pip will handle all dependencies automatically for us and you will always install the latest (and well-tested) version.


To install from source, follow the instructions in the [contribution guidelines](CONTRIBUTING.md).


## Installing GPU support


In order to install and run the GPU supported simulators on Linux, you need CUDA&reg; 10.1 or newer previously installed.
CUDA&reg; itself would require a set of specific GPU drivers. Please follow CUDA&reg; installation procedure in the NVIDIA&reg; [web](https://www.nvidia.com/drivers).


If you want to install our GPU supported simulators, you have to install this other package:


```bash
pip install qiskit-aer-gpu
```


## Simulating your first quantum program with Qiskit Aer
Now that you have Qiskit Aer installed, you can start simulating quantum circuits with noise. Here is a basic example:


```
$ python
```

```python
import qiskit
from qiskit import IBMQ
from qiskit_aer import AerSimulator

# Generate 3-qubit GHZ state
circ = qiskit.QuantumCircuit(3)
circ.h(0)
circ.cx(0, 1)
circ.cx(1, 2)
circ.measure_all()

# Construct an ideal simulator
aersim = AerSimulator()

# Perform an ideal simulation
result_ideal = qiskit.execute(circ, aersim).result()
counts_ideal = result_ideal.get_counts(0)
print('Counts(ideal):', counts_ideal)
# Counts(ideal): {'000': 493, '111': 531}

# Construct a noisy simulator backend from an IBMQ backend
# This simulator backend will be automatically configured
# using the device configuration and noise model 
provider = IBMQ.load_account()
backend = provider.get_backend('ibmq_athens')
aersim_backend = AerSimulator.from_backend(backend)

# Perform noisy simulation
result_noise = qiskit.execute(circ, aersim_backend).result()
counts_noise = result_noise.get_counts(0)

print('Counts(noise):', counts_noise)
# Counts(noise): {'000': 492, '001': 6, '010': 8, '011': 14, '100': 3, '101': 14, '110': 18, '111': 469}
```

## Authors and Citation

Qiskit Aer is the work of [many people](https://github.com/Qiskit/qiskit-aer/graphs/contributors) who contribute
to the project at different levels. If you use Qiskit, please cite as per the included [BibTeX file](https://github.com/Qiskit/qiskit/blob/master/Qiskit.bib).

## License

[Apache License 2.0](LICENSE.txt)
#   N u m b e r - G u e s s i n g - G a m e - U s i n g - Q u a n t u m C o m p u t i n g 
 
 
