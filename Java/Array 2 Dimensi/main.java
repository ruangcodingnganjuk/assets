public class Main {
   
   public static int nim = 0;
   public static int nama = 1;
   public static int ukm = 2;

   
   static String[][] array = {
      {"11", "Adi", "Kepanitiaan"},
      {"22", "Budi", "Olahraga"},
      {"33", "Citra", "Musik"},
      {"44", "Dedi", "Kepanitiaan"},
      {"55", "Eka", "Olahraga"},
      {"66", "Fajar", "Musik"},
      {"77", "Galih", "Kepanitiaan"},
      {"88", "Hasan", "Olahraga"},
      {"99", "Irma", "Musik"},
      {"100", "Jaka", "Kepanitiaan"}
   };

   static int n = 10;

   public static void main(String[] args) {

    find("NIM","101", 100);
   }

   public static void printByNim(int Nim) {
       for (int i = 0; i < n; i++) {
        
         int data = Integer.parseInt(array[i][0]);
         
         if (data == Nim ) {
            System.out.println("NIM: " + array[i][0] + System.lineSeparator() + "NAMA: " + array[i][1] + System.lineSeparator() + "UKM: " + array[i][2] + System.lineSeparator());
         }
       }
   }
   
   public static void printByUkm(String Ukm) {
       for (int i = 0; i < n; i++) {
         if (array[i][2] == Ukm ) {
            System.out.println("NIM   :" + array[i][0] + System.lineSeparator() + "NAMA: " + array[i][1] + System.lineSeparator() + "UKM: " + array[i][2] + System.lineSeparator());
         }
       }
   } 
   
   
   public static void printByNama(String Nama) {
       for (int i = 0; i < n; i++) {
         if (array[i][1] == Nama ) {
            System.out.println("NIM  : " + array[i][0] + System.lineSeparator() + "NAMA: " + array[i][1] + System.lineSeparator() + "UKM: " + array[i][2] + System.lineSeparator());
         }
       }
   } 
   
   public static void find(String findBy, String key, int inputNim){
       boolean status= false;
       if(findBy=="NAMA"){
          for (int i = 0; i < n; i++) {
              
                 int data = Integer.parseInt(array[i][0]);
                 if (data == inputNim && array[i][1] == key ) {
                    status = true;
                    System.out.println("NIM  : " + array[i][0] + System.lineSeparator() + "NAMA: " + array[i][1] + System.lineSeparator() + "UKM: " + array[i][2] + System.lineSeparator());
                 }
          }
       }
       
       if(findBy=="UKM"){
          for (int i = 0; i < n; i++) {
                 int data = Integer.parseInt(array[i][0]);
                 if (data == inputNim && array[i][2] == key ) {
                    status = true;
                    System.out.println("NIM  : " + array[i][0] + System.lineSeparator() + "NAMA: " + array[i][1] + System.lineSeparator() + "UKM: " + array[i][2] + System.lineSeparator());
                 }
          }
       }
       
       if(findBy=="NIM"){
          for (int i = 0; i < n; i++) {
                 int data = Integer.parseInt(array[i][0]);
                 if (data == inputNim ) {
                    status = true;
                    System.out.println("NIM  : " + array[i][0] + System.lineSeparator() + "NAMA: " + array[i][1] + System.lineSeparator() + "UKM: " + array[i][2] + System.lineSeparator());
                 }
          }
       }

       if(!status){
          System.out.println("data tidak di temukan" );
       }
   }
   
   
}