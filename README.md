# TMG
Tuner GUI for Openpilot

Tested on OP 0.8.10

Installation:
1) download to /data/ folder (/data/TMG/)
2) run ```python /data/TMG/install.py```

The GUI will not have any entries unless you add them in openpilot files, or patches are made. Example, we edit OP to register as example:
```ret.lateralTuning.lqr.scale = TMGClass.get("lqr_scale", ret.lateralTuning.lqr.scale)```
This will register the variable in params, so a reboot it required (reboot 1), a second reboot is needed after so it appears in the GUI.

Has ability to open Settings (for up to 30 seconds), giving you time to set settings, like enabling bluetooth, settings will close after 30 seconds and return back to openpilot.
On-screen lsusb support, displays the peripherals on your comma device.
