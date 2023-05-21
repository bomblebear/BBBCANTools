###    **How to use socketcan with the command line in linux**

1. first you need to make the `caninit_loopbackon` file excutable:
  `chmod u+x caninit_loopbackon`
2. then you can excute this file to initialize can configurations:
  `./caninit_loopbackon`
3. you can check that your can is online with `ifconfig`
4. send can message in can0 with can ID:0x300
  `cansend can0 300#00.11.22.33.44.55.66.77`
5. receive can message in another terminal with
  `candump any` or `candump can0`
