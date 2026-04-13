package main;

import impl.Light;
import impl.Fan;

public class Main {
    public static void main(String[] args) {

        Light light = new Light("Living Room");
        Fan fan = new Fan("Bedroom");

        light.turnOn();
        light.getStatus();

        fan.turnOn();
        fan.getStatus();

        fan.turnOff();
        fan.getStatus();
    }
}