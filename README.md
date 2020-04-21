# Awake
Awake - A cli utility for keeping the system awake while you are away.

This tiny utility can help you with desktop session idle timeouts, screensavers, screen timeouts by moving the mouse cursor in certain interval.

usage: python awake.py [-arg ARGUMENT_VALUE] <br />
<br />
  &nbsp;&nbsp;-h, --help                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Show help message for usage. <br />
  &nbsp;&nbsp;-i IDLE, --idle IDLE      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Duration to takeover mouse actions. in seconds. default value is 7. <br />
  &nbsp;&nbsp;-x XAXIS, --xaxis XAXIS   &nbsp;&nbsp;&nbsp; The amount of pixes to be moved during the action in x-axis. in pixels. default value is 10. <br />
  &nbsp;&nbsp;-y YAXIS, --yaxis YAXIS   &nbsp;&nbsp;&nbsp;&nbsp; The amount of pixes to be moved during the action in y-axis. in pixels. default value is 0. <br />
  <br />
example usage : <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python awake.py (will take all default values) <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;or python awake.py -i 20 -x 15 -y 0 <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      or     python awake.py --idle 20 --xaxis 15 --yaxis 0 <br />
<br />
feedback : _anshuman.d3@gmail.com_
