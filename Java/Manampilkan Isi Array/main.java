import java.util.Arrays;

public class Main {
    
   static int Nim [] = {11,22,33,44,55};
 
   static String Nama [] = {
        "Adi",
        "Budi",
        "Citra",
        "Yoga",
        " Wildan"
   };
   
    static String Ukm [] = {
        "Kepanitiaan",
        "Olahraga",
        "Musik",
        "Kepanitiaan",
        "Olahraga"
   };
   
   static int n = 5;

   public static void main(String[] args) {
    
    find("NAM","Adi",11);
   
   }    
   
    public static void printByNim(int NIM) {
         boolean status= false;
         for (int i = 0; i < n; i++) {
         // Jika kategori yang diberikan adalah nim dan nilai pada elemen array pada indeks kategori sama dengan kunci yang diberikan
         if (Nim[i]==NIM) {
            // Menampilkan nim, nama, dan UKM dari elemen tersebut
            status=true;
            System.out.println("STATUS : " + status + " NIM : " + Nim[i] + " NAMA : " + Nama[i] + " UKM : " + Ukm[i]);
            
         }
         
         
         
      }
      if(status==false){
            System.out.println("data tidak ditemukan");
      }
    }
    
    public static void printByNama(String kategori) {
         for (int i = 0; i < n; i++) {
         // Jika kategori yang diberikan adalah nim dan nilai pada elemen array pada indeks kategori sama dengan kunci yang diberikan
         if (Nama[i].equals(kategori)) {
            // Menampilkan nim, nama, dan UKM dari elemen tersebut
             System.out.println("NIM : " + Nim[i] + " NAMA : " + Nama[i] + " UKM : " + Ukm[i]);
         }
         
      }
    }
    
    public static void printByUkm(String kategori) {
         for (int i = 0; i < n; i++) {
         // Jika kategori yang diberikan adalah nim dan nilai pada elemen array pada indeks kategori sama dengan kunci yang diberikan
         if (Ukm[i].equals(kategori)) {
            // Menampilkan nim, nama, dan UKM dari elemen tersebut
             System.out.println("NIM : " + Nim[i] + " NAMA : " + Nama[i] + " UKM : " + Ukm[i]);
         }
         
      }
    }
    
    public static void find(String findBy, String key , int keyNim) {
         boolean status= false;
         if(findBy=="UKM"){
             
            for (int i = 0; i < n; i++) {
                 if (Ukm[i].equals(key) && Nim[i]==keyNim) {
                    status=true;
                    System.out.println("STATUS : " + status + " NIM : " + Nim[i] + " NAMA : " + Nama[i] + " UKM : " + Ukm[i]);
                 }
             }
       }
       
       if(findBy=="NAMA"){
            for (int i = 0; i < n; i++) {
                 if (Nama[i].equals(key) && Nim[i]==keyNim) {
                    status=true;
                    System.out.println("STATUS : " + status + " NIM : " + Nim[i] + " NAMA : " + Nama[i] + " UKM : " + Ukm[i]);
                 }
             }
       }
       
       if(findBy=="NIM"){
            for (int i = 0; i < n; i++) {
                 if (Nim[i]==keyNim) {
                    status=true;
                    System.out.println("STATUS : " + status + " NIM : " + Nim[i] + " NAMA : " + Nama[i] + " UKM : " + Ukm[i]);
                 }
             }
       }
        if(status==false){
            System.out.println("data tidak ditemukan");
        }
    }
    
 }