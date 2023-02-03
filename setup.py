from setuptools import setup

setup(
    name='imu_gnss_fusion',
    version='0.1',
    description='IMU/GNSS fusion using Extended Kalman Filter',
    author='Saurav Uprety',
    url='https://github.com/vehicle-trace-echo/imu_gnss_fusion',
    install_requires=['numpy==1.23.4',
                    'math'],
    packages=['imu_gnss_fusion'],
)