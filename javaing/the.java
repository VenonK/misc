public class the {
    static int Hotel(int hashKey,int numOfSlots){
        int hashValue = hashKey % numOfSlots;
        return hashValue;
    }
    public static void main(String[] args) {
        int returning = the.Hotel(31971, 48);
        System.out.println(returning);
    }
}
