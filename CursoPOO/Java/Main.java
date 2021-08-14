package Java;

class Main{
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car("AMQ234", new Account("Oscar Chaparro", "CABO861221HDFHLS07"));
        car.passenger = 4;
        car.printDataCar();

        Car car2 =  new Car("LOL009", new Account("Eduardo Chaparro", "CAOE861221HDFHLS01"));
        car2.passenger = 6;
        car2.printDataCar();
    }
}