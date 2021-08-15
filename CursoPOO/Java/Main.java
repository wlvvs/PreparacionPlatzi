package Java;

class Main{
    public static void main(String[] args){
        System.out.println("Hola Mundo");
        UberX uberX = new UberX("AMQ234", new Account("Oscar Chaparro", "CABO861221HDFHLS07"), "Chevrolet", "Sonic");
        //UberX.passenger = 4; Esto ya no se usa con el setter - getter
        uberX.setPassenger(4);
        uberX.printDataCar();

        UberVan uberVan = new UberVan("ASD653", new Account("Pancho Lopez", "LOCP861221HDFHLS02"));
        uberVan.setPassenger(6);
        uberVan.printDataCar();

        /*Car car2 =  new Car("LOL009", new Account("Eduardo Chaparro", "CAOE861221HDFHLS01"));
        car2.passenger = 6;
        car2.printDataCar();*/
    }
}