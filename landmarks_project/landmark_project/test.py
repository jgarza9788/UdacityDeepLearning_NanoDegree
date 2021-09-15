# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'


import torch


use_cuda = torch.cuda.is_available()
print(use_cuda)

# import torch

# print(f"Is CUDA supported by this system? {torch.cuda.is_available()}")
# print(f"CUDA version: {torch.version.cuda}")

# # Storing ID of current CUDA device
# cuda_id = torch.cuda.current_device()
# print(f"ID of current CUDA device:{torch.cuda.current_device()}")
        
# print(f"Name of current CUDA device:{torch.cuda.get_device_name(cuda_id)}")