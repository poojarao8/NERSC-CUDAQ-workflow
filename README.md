# NERSC-CUDAQ-workflow

### One-Time Only Requirements ###
1. Pull the specified image using shifter

   
   `shifterimg pull nvcr.io/nvidia/nightly/cuda-quantum:cu12-latest` (requires Nvidia account)
   
   `shifterimg pull ghcr.io/nvidia/cuda-quantum:cu12-latest-base` (CUDA 11)
   
   `shifterimg pull ghcr.io/nvidia/cuda-quantum:cu11-latest-base` (CUDA 12)

2. Enter the shifter container interactively
   
   `shifter --image=docker:nvcr.io/nvidia/nightly/cuda-quantum:cu12-latest --module=nccl-2.18 /bin/bash` (Nvidia accounts)
   
   `shifter --image=docker:ghcr.io/nvidia/cuda-quantum:cu12-latest-base --module=nccl-2.18 /bin/bash` (CUDA 12)
   
   `shifter --image=docker:ghcr.io/nvidia/cuda-quantum:cu11-latest-base --module=nccl-2.15 /bin/bash` (CUDA 11)

3. Copy the distributed_interfaces folder over
   
   `cp -r /opt/nvidia/cudaq/distributed_interfaces/ $HOME/.`

5. Exit the container
   
   `exit`

6. Setup environment
   
   ```
   export MPI_PATH=$MPICH_DIR
   source distributed_interfaces/activate_custom_mpi.sh
   ```

### Everytime you login ###
1. Setup environment

   `export CUDAQ_MPI_COMM_LIB=**/path/to/** distributed_interfaces/libcudaq_distributed_interface_mpi.so`
