import tensorflow as tf 
import os
from tensorflow.python.client import device_lib

from tensorflow.python.client import device_lib

# device_lib.list_local_devices()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print(device_lib.list_local_devices())

# if tf.test.gpu_device_name(): 
#     print(f'Default GPU Device:{tf.test.gpu_device_name()}')
# else:
#    print("Please install GPU version of TF")


# def get_available_gpus():
#     local_device_protos = device_lib.list_local_devices()
#     return [x.name for x in local_device_protos if x.device_type == 'GPU']

# print('list of gpu ', get_available_gpus())