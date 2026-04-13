package impl;

import devices.SmartDevice;
import control.Controllable;
import monitor.Monitorable;

public class Fan extends SmartDevice implements Controllable, Monitorable {

    private boolean isOn;

    public Fan(String name) {
        super(name);
        isOn = false;
    }

    public void turnOn() {
        isOn = true;
        System.out.println(deviceName + " Fan ON");
    }

    public void turnOff() {
        isOn = false;
        System.out.println(deviceName + " Fan OFF");
    }

    public void getStatus() {
        System.out.println(deviceName + " Status: " + (isOn ? "ON" : "OFF"));
    }
}
