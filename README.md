# scara_cpe

+ This package is a starter kit for the scara_cpe robot practical work.

+ Packages dependencies:
  - dynamixel_motor
  - serial (from source only)
  
+ Check robot motor connection :
  ```{r, engine='bash', count_lines} 
  rosrun dynamixel_driver info_dump.py -p /dev/ttyACM0 -b 200000 1 2
  ```
  
  If you have the following error...
  ```{r, engine='bash', count_lines} 
  Failed to set custom baud rate: 200000
  ```
  ...please execute the following command in a bash (once and for all)
  ```{r, engine='bash', count_lines} 
  svn co http://pyserial.svn.sourceforge.net/svnroot/pyserial/trunk pyserial
  cd pyserial/pyserial
  python setup.py install --user
  ```
