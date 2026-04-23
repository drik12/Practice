package Java.AS8;

interface MediaPlayer{
    void play();
}

class Audioplayer implements MediaPlayer{
    public void play(){
        System.out.println("Playing Audio...");
    }
}

class Videoplayer implements MediaPlayer{
    public void play(){
        System.out.println("Playing Video...");
    }
}

public class Main5 {
    public static void main(String[] args){
        MediaPlayer m1 = new Audioplayer();
        MediaPlayer m2 = new Videoplayer();

        m1.play();
        m2.play();
    }
}
