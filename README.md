# TMG
Tuner GUI for Openpilot

Tested on OP 0.8.10

Installation:
1) download to /data/ folder (/data/TMG/)
2) run ```python /data/TMG/install.py```

The GUI will not have any entries unless you add them in openpilot files, or patches are made. Example, we edit OP to register as example:
```ret.lateralTuning.lqr.scale = TMGClass.get("lqr_scale", ret.lateralTuning.lqr.scale)```
This will register the variable in params, so a reboot it required (reboot 1), a second reboot is needed after so it appears in the GUI.
Make sure you put it where OP regularly updates and checks the key, so tuning can be live. Ex. Don't put it in interface.py where it is loaded only once per ignition start, you won't be able to tune live that way.. 


Has ability to open Settings (for up to 30 seconds), giving you time to set settings, like enabling bluetooth, settings will close after 30 seconds and return back to openpilot.

On-screen lsusb support, displays the peripherals on your comma device.

Tuning of values can be done by percent (1% ->15%) or by value (0.1, 0.01, 0.001), Selectable via drop down combobox

If openpilot variable supports self-dynamic updating (like steerRatio), you can choose to let it do it dynamically, or set a static value for it.
```ret.steerRatio = TMGClass.get("steer_ratio", ret.steerRatio, True)``` Just append "True" argument to the call.
The quoted key name can be anything you want to reference your variable, just to identify what you will be tuning.
