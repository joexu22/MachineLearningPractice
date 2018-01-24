# My Machine Learning Repository
* The plan is to have a whole bunch of machine learning code here
* Currently a whole bunch of practice problems

# Holy Cow - It's Alive
* I Frankansteined My Workflow, but I can now comfortably code from the comfort of my main Windows 10 computer
* Installing this on Windows was not "FUN"
* <Having The Photoshop/DAW Tools> a couple clicks might be worth it though

# Instructions - For Windows 10 (Cause I'm Too Crazy/Lazy To Just Dual Boot Ubuntu On My Main PC)
* **Linux Subsystem on Windows 10 does not currently allow NVIDIA GPU use**
* The Current Method is subject to depreciation I'll probably upgrade at some point
* From Nvidia:
  - Install Cuda Toolkit 9.0
  - Install CUDNN 7
  - Copy Files From CUDNN over to C:\Program Files\NVIDIA GUP Computing Toolkit\Cuda\v9.0

* From Google:
  - [Attempt To Build tensorflow From Source...]
  - [Or] Aquire tensorflow-gpu.whl from https://pypi.python.org/pypi/tensorflow-gpu

* From Anaconda/Python:
  - Download and Install Anaconda https://www.anaconda.com/download/
  - Set up Anaconda virtual env
  - Build tensorflow in Anaconda virtual env

* Configure Visual Studio execute from virtual env folder
  - Create Custom Environment with currect locations
  - <path_to_anaconda>\Anaconda3\env\<env_name>
  - Set Custom Environment to default for VS

* Sacrifice A Young Animal
* Pray to Cthulhu

* Start Some Machine Learning Excercises On Windows 10