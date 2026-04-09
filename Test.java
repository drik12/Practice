class Test {
    void task1(){
        for(int i = 1; i <= 3; i ++){
        System.out.println("A");
        }
    }

    void task2(){
        for(int i = 1; i <= 3; i ++){
        System.out.println("B");
        }
    }

    public static void main(String[] args){
        Test t = new Test();
        t.task1();
        t.task2();
    }
}
