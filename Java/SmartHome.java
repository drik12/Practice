// Parent class
class SmartDevice {

    void turnOn() {
        System.out.println("Device is turning on");
    }
}

// Child class 1
class Light extends SmartDevice {

    @Override
    void turnOn() {
        System.out.println("Light is turned on");
    }
}

// Child class 2
class Fan extends SmartDevice {

    @Override
    void turnOn() {
        System.out.println("Fan is turned on");
    }
}

// Child class 3
class AirConditioner extends SmartDevice {

    @Override
    void turnOn() {
        System.out.println("Air Conditioner is turned on");
    }
}

// Main class
public class SmartHome {
    public static void main(String[] args) {

        SmartDevice d;

        d = new Light();
        d.turnOn();

        d = new Fan();
        d.turnOn();

        d = new AirConditioner();
        d.turnOn();
    }
}